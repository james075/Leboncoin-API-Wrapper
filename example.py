from Leboncoin.Leboncoin import  Leboncoin as LBC


lbc = LBC()
lbc.searchFor("iphone", True)
lbc.setLimit(10)
lbc.maxPrice(2000)
lbc.setDepartement("tarn")
results = lbc.execute()

results.print()
