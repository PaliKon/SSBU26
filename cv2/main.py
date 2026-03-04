import pandas as pd
from PIL import Image

#ULOHA 1
#Vstupom do funkcie je parameter ages, čo je štruktúra list obsahujúca vek niekoľkých pacientov.
ages = [12, 25, 70, 45, 16, 80]

def patients(ages):
    dictionary = {
        "minor": 0,
        "adult": 0,
        "senior": 0
    }
    for age in ages:
        if age < 18:
            dictionary["minor"] += 1
        elif age >= 18 and age <= 65:
            dictionary["adult"] += 1
        else:
            dictionary["senior"] += 1
    return dictionary
print(patients(ages)) #vypisanie pacientov v kategoriach v strukture

#Úloha 2: Spracovanie súborov s údajmi o pacientoch
#Zapište údaje o pacientoch (meno, diagnóza) do súboru s názvom data/patients.csv.

pacienti = [
    ["Pavol", "Chripka"],
    ["Peter", "Teplota"],
    ["Martina", "Zimnica"],
    ["Stefan", "Zltacka"],
    ["Jana", "Chripka"],
    ["Marek", "Kasel"],
    ["Lucia", "Teplota"],
    ["Tomas", "Nadcha"],
    ["Katarina", "Alergia"],
    ["Michal", "Kasel"],
    ["Veronika", "Chripka"],
    ["Daniel", "Teplota"],
    ["Zuzana", "Bolest_hlavy"],
    ["Robert", "Nadcha"],
    ["Ivana", "Zimnica"],
    ["Martin", "Alergia"],
    ["Patrik", "Kasel"],
    ["Andrea", "Chripka"],
    ["Juraj", "Teplota"],
    ["Lenka", "Bolest_hrdla"]
]
# writing to a file
with open("data/patients.csv", "w+") as file:
    file.write("name,diagnosis\n") # writing a header

    for patient in pacienti:
        file.write(patient[0] + "," + patient[1] + "\n")


#Úloha 3: Načítanie údajov do štruktúry DataFrame a ich vizualizácia

#Načítajte údaje zo súboru data/patients.csv do štruktúry DataFrame (knižnica Pandas).
df = pd.read_csv("data/patients.csv")

#Vytvorte hlavičku pre tento DataFrame (pridajte názvy stĺpcov - name a diagnosis)
df.columns = ["name", "diagnosis"]

#Pridajte do štruktúry DataFrame nový stĺpec s názvom "ID". hodnoty tohto stĺpca tvorí sekvencia čísel od 0 do 19.
df["ID"] = range(0, 20)
#Vypíšte hodnoty v stĺpci diagnosis a počet hodnôt pre jednotlivé diagnózy.
print(df["diagnosis"])
print(df["diagnosis"].value_counts())


#Úloha 4: Práca s obrazom
#Načítajte obrázok data/microscope_g.jpg a vykonajte na ňom operáciu priblíženia a orezania, tak aby na obrázku boli viditeľné iba bunky, nie okulár mikroskopu. (Použite súradnice (300, 550, 1000, 1250) - (left, top, right, bottom)) Nakoniec obrázok zobrazte.

#Použite funkcie knižnice PIL:

#Image.open() - Dokumentácia open
img = Image.open("data/microscope.jpg")
#Image.resize() - Dokumentácia resize
img.resize((800,800))
#Image.crop() - Dokumentácia crop
img.crop((300, 550, 1000, 1250))
#Image.show() - Dokumentácia show
img.show()

#Úloha 5: Vytvorenie triedy a analýza pacientov
#Vytvorte triedu PatientData, ktorá načíta údaje zo CSV súboru do DataFrame a umožní základnú analýzu.
class PatientData:
#Načítanie CSV súboru v konštruktore (použite súbor data/patients.csv) a uloženie do atribútu typu DataFrame.
    def __init__(self):
        self.df = pd.read_csv("data/patients.csv")
        self.df.columns = ["name", "diagnosis"]
#Metóda count_diagnoses(), ktorá vráti počet pacientov s jednotlivými diagnózami.
    def count_diagnoses(self):
        return self.df["diagnosis"].value_counts()
#Metóda get_most_common_diagnosis(n), ktorá vráti n najčastejších diagnóz.
    def get_most_common_diagnosis(self,n):
        return self.df["diagnosis"].value_counts().head(n)
#Metóda display_summary(), ktorá zobrazí základné štatistiky.
    def display_summary(self):
        print("Pocet pacientov:", len(self.df))
        print("\nPocty diagnoz:")
        print(self.count_diagnoses())


patients = PatientData()

print(patients.count_diagnoses())

print("\nNajcastejsie diagnozy:")
print(patients.get_most_common_diagnosis(3))

print("\nSummary:")
patients.display_summary()