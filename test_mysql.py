import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    port= 3306,
    password="Ardahan75.",
    database="basketbal"
)

print(mydb)

if mydb.is_connected():
    print("Bağlandı")

mycursor = mydb.cursor()

query = "SELECT * FROM sporthal"
# voer de query uit m.b.v. de cursor
mycursor.execute(query)

# haal het resultaat van de query op
# en toon alle records op het scherm
rows = mycursor.fetchall()
for row in rows:
    print(row)

# toon het aantal records dat de query heeft opgelever
print(mycursor.rowcount)

# Toon o.a. de attribute
print(mycursor.description)

# toon de inhoud het 3e element van het 4e record
print(rows)
print(rows[3][2])

# INSERT TEST DATA
# nieuwe_sporthal = ("mijn_sporthal", "mijn_plaats", 4)
# query = ("insert into sporthal (sporthalnaam, sporthalplaats, aantalvelden) "
#          "values (%s, %s, %s)")
# mycursor.execute(query, nieuwe_sporthal)
# # De gegevens zijn nu naar de database gestuurd, maar nog niet opgeslagen
# # Om de gegevens daadwerkelijk op te slaan moeten we de functie commit() aanroepen
# mydb.commit()

# UPDATE TEST DATA
# aangepaste_sporthal = ("mijn_sporthal", "mijn_plaats", 6)
# query = "update sporthal set aantalvelden = %s where sporthalnaam = %s"
# # De variabelen die we nodig hebben in de update query zijn:
# # - het nieuwe aantal velden: aangepaste_sporthal[2]
# # - de naam van onze sporthal: aangepaste_sporthal[0]
# # NB ondanks dat aantalvelden een integer is nemen we deze op met %s in de query
# mycursor.execute(query, (aangepaste_sporthal[2], aangepaste_sporthal[0]))
# mydb.commit()


verwijder_sporthal = ("mijn_sporthal", "mijn_plaats", 6)
query = "delete from sporthal where sporthalnaam = %s"
mycursor.execute(query, (verwijder_sporthal[0],))
mydb.commit()

