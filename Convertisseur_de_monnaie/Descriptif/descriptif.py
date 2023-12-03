
from forex_python.converter import CurrencyRates

def convertir(quantité, origine_devise, destination_devise):
    c = CurrencyRates()
    try: 
        résultat = c.convert(origine_devise, destination_devise, quantité)
        return résultat
    except:
        return None
    
def enregistrer_conversation(quantité, origine_devise, destination_devise, résultat):
    pass # nous avons décidé de ne pas implémenter la logique pour enrégistrer la conversion dans un fichier ou base de donnés

def main():
    quantité = float(input("Inserez le montant à convertir: "))
    origine_devise = input("Inserez la devise d'origine: ")
    destination_devise = input("Inserez la devi de destination: ")

    résultat = convertir(quantité, origine_devise, destination_devise)

    if résultat is not None:
        print(f"{quantité} {origine_devise} {destination_devise} {résultat}")
        enregistrer_conversation(quantité, origine_devise, destination_devise, résultat)
    else:
        print("La conversation n'est pas possible")

if __name__ == "__main__":
    main()