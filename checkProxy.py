def checkProxy(proxyUrl):
    #proxyUrl:   http://10.1.22.20:8080
    ip = proxyUrl[proxyUrl.find('//') + 2:proxyUrl.rfind(':')]
    port = proxyUrl[proxyUrl.rfind(':') + 1:]

    data = {'data': ip, 'type': 'proxycheck', 'arg': 'p=' + str(port) + "_t=1_o=3"}
    rq = requests.post(proxycheck, data= data,
                       headers=getCheckHeaders())
    if rq.status_code == 200:
        jsonText = rq.json()
        jsonData = jsonText['data'][0]
        if jsonData.find(u'失败') > 0:
            return False
        print 'success: ',ip,port
        return True
    return False
