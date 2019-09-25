def get_auth_url():
    weibo_auth_url = "https://api.weibo.com/oauth2/authorize"
    redirect_url = "http://148.70.221.132:8000/complete/weibo/"
    auth_url = weibo_auth_url+"?client_id={client_id}&redirect_uri={re_url}".format(client_id=484291611,re_url=redirect_url)
    print(auth_url)


def get_access_token(code="5c0afc1097a7584d74493ca825e3e71d"):
    access_token_url = "https://api.weibo.com/oauth2/access_token"
    import requests
    re_dict = requests.post(access_token_url,data={
        "client_id":"484291611",
        "client_secret":"33c0c3cbf9535a89a92b20c418579c3a",
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":"http://148.70.221.132:8000/complete/weibo/"
    })
    pass


#"access_token":"2.00uZLX8G0B4CmWaf18761a9eAo7URB"

def get_user_info(access_token="2.00uZLX8G0B4CmWaf18761a9eAo7URB",uid="5903667398"):
    user_url = "https://api.weibo.com/2/users/show.json?access_token={token}&uid={uid}".format(token=access_token,uid=uid)
    print(user_url)


if __name__ == "__main__":
    # get_auth_url()
    # get_access_token(code="5c0afc1097a7584d74493ca825e3e71d")
    get_user_info(access_token="2.00uZLX8G0B4CmWaf18761a9eAo7URB",uid="5903667398")