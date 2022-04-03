import win32com.client
instCpStockCode = win32com.client.Dispatch("CpUtil.CpStockCode")
stockNum = instCpStockCode.GetCount()

print("##Name Find##")
for i in range(stockNum):
    if instCpStockCode.GetData(1, i) == 'NAVER':
        print(instCpStockCode.GetData(0,i))
        print(instCpStockCode.GetData(1,i))
        print(i)
 
print("##Name to Code##")
naverCode = instCpStockCode.NameToCode('NAVER')
naverIndex = instCpStockCode.CodeToIndex(naverCode)
print(naverCode)
print(naverIndex)

print("##Dispaly All Stock##")
for i in range(0, stockNum):
    print(instCpStockCode.GetData(0,i),instCpStockCode.GetData(1,i))
