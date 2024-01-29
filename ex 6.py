annee = input ("Entrez une année:")

annee = int(annee)

if annee%4==0 or annee%400==0:
        print ("Cette année est bissextile")
else:
        print("Cette année n'est pas bissextile")

