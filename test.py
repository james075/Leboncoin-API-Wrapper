from Payload.Payload import Payload
import json


pl = Payload()
pl.setLimit(1)
pl.maxPrice(200)
pl.setDepartement("tarn")

# Cherche les produits avec google home dans le titre
pl.searchFor("google home", True)  # Mettre à false pour cherche partout ailleurs(description...)
resultat = pl.build()

with open("resultat.json", "w+") as jsonFile:
    jsonFile.write(json.dumps(resultat))
