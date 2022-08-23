import json
import requests


def get_proxy_ip():

    # 使用代理给服务器发送请求
    try:
        response = requests.get("http://juchacha.cn:8585/get_ip")
        response = json.loads(response.text)
        if response['data']['ip']:
            proxies = {"https": "https://{}".format(response['data']['ip']), "http": "http://{}".format(response['data']['ip'])}
            return proxies
        else:
            get_proxy_ip()
    except:
        get_proxy_ip()


if __name__ == '__main__':

    proxys = get_proxy_ip()

    res =requests.get('http://httpbin.org/get', proxies=proxys)
    print(res.text)