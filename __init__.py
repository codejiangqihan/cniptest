import requests
def ip():
    try:
        ip = requests.get("https://4.ipw.cn").text
        return ip
    except:
        return "Error:Unreachable"
def ipv6():
    try:
        ip = requests.get("https://6.ipw.cn").text
        return ip
    except:
        return "Error:Unreachable"
def test():
    try:
        ip = requests.get("https://test.ipw.cn").text
        return ip
    except:
        return "Error:Unreachable"
def bjv4():
    try:
        ip = requests.get("https://bjv4.ipw.cn").text
        return ip
    except:
        return "Error:Unreachable"
def bjv6():
    try:
        ip = requests.get("https://bjv6.ipw.cn").text
        return ip
    except:
        return "Error:Unreachable"
def njv4():
    try:
        ip = requests.get("https://njv4.ipw.cn").text
        return ip
    except:
        return "Error:Unreachable"
def njv6():
    try:
        ip = requests.get("https://njv6.ipw.cn").text
        return ip
    except:
        return "Error:Unreachable"