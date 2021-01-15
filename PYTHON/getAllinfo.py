import urllib.request

#拼接报文地址
def getBaseUrl(fundCode):
    base = "http://fundgz.1234567.com.cn/js/"
    base = base + fundCode
    base = base +".js?rt=1463558676006"
    return base

#获取报文
def getHtml(url):
    header = {
        "User-Agent": "",
        "Referer": "",
        "Cookie":""
    }
    data = ""
    request = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(request)
    data = response.read().decode("utf-8")
    return data

#解析数据
def Json(html):
    html = html.replace('}', '')
    html = html.replace('{', '')
    html = html.replace('(','')
    html = html.replace(')','')
    html = json.loads(html)
    return html
