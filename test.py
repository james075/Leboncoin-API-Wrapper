from Payload.Payload import Payload
from Response.Response import *


pl = Payload()
pl.setLimit(1)
pl.maxPrice(200)
pl.setDepartement("tarn")
pl.searchFor("google home", True)
response = Response(**pl.build())

print(response.total)
