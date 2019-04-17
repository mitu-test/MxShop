def get_auth_url():
    weibo_auth_url = "https://api.weobo.com/oauth2/authorize"
    redirect_url = ""
    auth_url = weibo_auth_url+"?client_id={client_id}&redirect_url={re_url}".format(client_id=2333,re_url=redirect_url)
    print(auth_url)


def get_access_token(code="436468707eeeeeeeeeeeeey"):
    access_token_url = "http://"
    import requests
    re_dict = requests.post(access_token_url,data={
        "client_id":"",
        "client_secret":"",
        "grant_type":"",
        "code":code,
        "redirect_uri":"http://"
    })
    pass


def get_user_info(access_token=""):
    user_url = "http://"

    print(user_url)


if __name__ == "__main__":
    get_auth_url()
    get_access_token(code="32427537dgfdj")
    get_user_info(access_token="ggg",uid="474889889898")