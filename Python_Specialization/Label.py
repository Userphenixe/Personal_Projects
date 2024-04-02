def label(prenom, note):
    if (note >= 10) and (note <= 16):
        print(f"{prenom} est recu")
    elif (note >= 16) and (note <= 20):
        print(f"Felicitations a {prenom}")
    elif (note >= 0) and (note <= 10):
        print(f"{prenom} est recale")
    else:
        print("erreur de saisie:")
    return 0
label('Remi', 10)
label('Marie', 17)
label('Kevin', 8)
