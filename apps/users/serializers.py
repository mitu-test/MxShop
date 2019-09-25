from rest_framework import serializers
import re
from django.contrib.auth import get_user_model
from MxShop.settings import REGEX_MOBILE
from datetime import datetime
from datetime import timedelta
from .models import VerifyCode
from rest_framework.validators import UniqueValidator
User = get_user_model()


class SmsSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=11)

    def validate_mobile(self, mobile):
        """
        验证手机号码
        :param data:
        :return:
        """

        # 手机是否注册
        if User.objects.filter(mobile=mobile).count():
            raise serializers.ValidationError("用户已经存在")

        # 验证手机号码是否合法
        if not re.match(REGEX_MOBILE, mobile):
            raise serializers.ValidationError("手机号码非法")

        # 验证码发送频率
        one_mintes_ago = datetime.now() - timedelta(hours=0, minutes=1, seconds=0)
        if VerifyCode.objects.filter(add_time__gt=one_mintes_ago, mobile=mobile).count():
            raise serializers.ValidationError("距离上一次发送未超过60s")

        return mobile


class UserDetailSerializer(serializers.ModelSerializer):
    """
    用户详情序列化
    """
    class Meta:
        model = User
        fields = ("name","gender","birthday","email","mobile")


class UserRegSerializer(serializers.ModelSerializer):
    #注意write_only=True是必须的，这样返回前端时就不会序列化，否则会出现userProfile中没有code字段的错误，应为后面被删了
    code = serializers.CharField(required=True,write_only=True,max_length=4,min_length=4,label="验证码",
                                 error_messages={
                                     "blank": "请输入验证码",
                                     "required": "请输入验证码",
                                     "max_length": "验证码格式错误",
                                     "min_length": "验证码格式错误"
                                 },
                                 help_text="验证码")
    #验证username是否存在，validators（验证器）验证username是否唯一，比如用户发送验证码成功，后面又修改了手机，验证手机是否存在，验证失败的话，messages消息提示
    username = serializers.CharField(label="用户名", help_text="用户名", required=True, allow_blank=False,
                                     validators=[UniqueValidator(queryset=User.objects.all(), message="用户已经存在")])
    #style设置为密文
    password = serializers.CharField(
        style={'input_type':'password'},label="密码",write_only=True,
    )
    #以下注释代码解决序列化后密码没有加密的问题
    def create(self, validated_data):
        user = super(UserRegSerializer, self).create(validated_data=validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

    def validate_code(self,code):
        verify_records = VerifyCode.objects.filter(mobile=self.initial_data["username"]).order_by("-add_time")
        if verify_records:
            last_record = verify_records[0]
            five_mintes_ago = datetime.now() - timedelta(hours=0, minutes=5, seconds=0)
            if five_mintes_ago > last_record.add_time:
                raise serializers.ValidationError("验证码过期")
            if last_record != code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")

    def validate(self, attrs):
        attrs["mobile"] = attrs["username"]
        del attrs["code"]
        return attrs

    class Meta:
        model = User
        fields = ("username","code","mobile","password")

