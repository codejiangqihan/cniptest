import requests
def ip():
    try:
        ip = requests.get("https://4.ipw.cn").text
        return ip
    except:
        return "error"
def ipv6():
    try:
        ip = requests.get("https://6.ipw.cn").text
        return ip
    except:
        return "error"
def test():
    try:
        ip = requests.get("https://test.ipw.cn").text
        return ip
    except:
        return "error"
def bjv4():
    try:
        ip = requests.get("https://bjv4.ipw.cn").text
        return ip
    except:
        return "error"
def bjv6():
    try:
        ip = requests.get("https://bjv6.ipw.cn").text
        return ip
    except:
        return "error"
def njv4():
    try:
        ip = requests.get("https://njv4.ipw.cn").text
        return ip
    except:
        return "error"
def njv6():
    try:
        ip = requests.get("https://njv6.ipw.cn").text
        return ip
    except:
        return "error"