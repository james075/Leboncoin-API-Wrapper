from leboncoin_api_wrapper import Leboncoin

lbc = Leboncoin()
lbc.searchFor("iphone", True)
lbc.setLimit(10)
lbc.maxPrice(2000)
lbc.setDepartement("tarn")
results = lbc.execute()

results.print()
