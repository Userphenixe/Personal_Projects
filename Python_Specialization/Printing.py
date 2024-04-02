produit = "Aspi Deluxe"
code = "as0003"
prix = 253.99
garantie = 2
tva = prix * 0.20
print(f"produit du mois : {produit}")
print(f"le code du produit: {code} - garanti 2 ans")
print(" "*10 + f"{produit}-{code}")
print(f"{code}- {produit}: {prix} HT")
print(f"{code}- {produit}: {prix + tva} TTC")
print(f"{code}- {produit}: {(prix + tva):010.2f} TTC")
