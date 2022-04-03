import win32com.client

# Create object
instStockChart = win32com.client.Dispatch("CpSysDib.StockChart")

# SetInputValue
instStockChart.SetInputValue(0, "A031820")
instStockChart.SetInputValue(1, ord('2'))
instStockChart.SetInputValue(4, 30)
instStockChart.SetInputValue(5, (0, 2, 3, 4, 5, 8))
instStockChart.SetInputValue(6, ord('D'))
instStockChart.SetInputValue(9, ord('1'))

# BlockRequest
instStockChart.BlockRequest()

# GetHeaderValue
numData = instStockChart.GetHeaderValue(3)
numField = instStockChart.GetHeaderValue(1)

# GetDataValue
for i in range(numData):
    for j in range(numField):
        print(instStockChart.GetDataValue(j, i), end=" ")
    print("")