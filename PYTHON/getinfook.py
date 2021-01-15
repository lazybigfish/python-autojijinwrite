import getAllinfo


#获取基金净值
def getInfo(fundCode):
    #空列表准备置放净值集合
    infolist = []
    #空列表准备置放净值详细集合
    dataList = []
    #开始遍历基金代码，获取对应的净值，并插入datalist
    for i in fundCode:
        fundCode = i
        #拼接地址
        baseURL = getAllinfo.getBaseUrl(fundCode)
        #获取数据开始解析
        data = getAllinfo.getHtml(baseURL)
        #去除多余数据
        data = data.split(('"'))
        dataList.append(data[7])
        dataList.append(data[14])
        dataList.append(data[15])
        infolist.append(data[15])
        #print(data)
        # print(''.join(dataList))
    # print("需要叠加的个数：%s" % y)
    # print("基金净值的详细情况：%s" % dataList)
    # print("基金净值的情况：%s" % infolist)

    return infolist