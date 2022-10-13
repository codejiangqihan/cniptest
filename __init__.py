import requests
def ip():
    ip = requests.get("https://4.ipw.cn").text
    return ip
def ipv6():
    ip = requests.get("https://6.ipw.cn").text
    return ip