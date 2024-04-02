Etudiants = [['hamza', 'admis'], ['med', 'admis'], ['ayoub', 'ajournee'], ['hossam', 'admis'], ['rayan', 'ajournee']]
Etudiants_Admis = []
Etudiants_Ajournees = []
size = len(Etudiants)
i = 0
while i < size:
    if Etudiants[i][1] != 'admis':
        Etudiants_Ajournees.append(Etudiants[i][0])
    else:
        Etudiants_Admis.append(Etudiants[i][0])
    i = i + 1
print(Etudiants_Admis)
print(Etudiants_Ajournees)