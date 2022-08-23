import time

import requests


def get_proxy_ip():
    try:
        url = "http://103.72.145.213:12408/home/ip-proxy"
        requests.adapters.DEFAULT_RETRIES = 5
        sess = requests.Session()
        # sess.keep_alive = False
        data = {
            "proxy": "e319baa5c6bcc7e1a4905c2d49b94de9",

        }
        resp = sess.post(url, data=data)
        return {'socks5':resp.json().get("data").get("proxy")}
    except:
        time.sleep(3)
        get_proxy_ip()

if __name__ == '__main__':
    proxy = get_proxy_ip()
    print(proxy)