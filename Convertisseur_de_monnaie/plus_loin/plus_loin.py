
from forex_python.converter import CurrencyRates

def convertir_dev(montant, origine_dev, destination_dev):
    c = CurrencyRates()
    résultat = c.convert(origine_dev, destination_dev, montant)
    return résultat

def ajouter_dev(dévise, taux):
    c = CurrencyRates()
    c.add_rate("USD", dévise, taux)

montant = 17000
origine_dev = "USD"
destination_dev = "EUR"

résultat = convertir_dev(montant, origine_dev, destination_dev)
print(f"{montant} {origine_dev} est égal à {résultat} {destination_dev}")
