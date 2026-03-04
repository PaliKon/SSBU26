

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



if __name__ == '__main__':
    print_hi('PyCharm')

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
    ["Pavol",  "Chripka"],
    ["Peter", "Teplota"],
    ["Martina", "Zimnica"],
    ["Stefan", "Zltacka"]

]
# writing to a file
with open("data/patients.csv", "w+") as file:
    file.write("name,diagnosis\n") # writing a header

    for patient in pacienti:
        file.write(patient[0] + "," + patient[1] + "\n")





