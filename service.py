# STUDENT FEEST - TECHNO
# Auteur: Gökhan Öztürk

# SERVICE LAGER
import time
import repository
import re
from datetime import datetime

# 1) LOGIN
"""
LIJST VAN VEELVOORKOMENDE EXCEPTIONS (Hata Tipleri Listesi):
--------------------------------------------------------------------------------
1. ValueError      : De waarde is van het juiste type, maar de inhoud is ongeldig.
                     (Değer tipi doğru ama içeriği geçersiz.)

2. TypeError       : Een bewerking wordt toegepast op een object van een onjuist type.
                     (Yanlış veri tipi üzerinde işlem yapılmaya çalışıldığında.)

3. PermissionError : De gebruiker heeft niet de juiste rechten voor de actie.
                     (Kullanıcının işlem için gerekli yetkisi olmadığında.)

4. IndexError      : Er wordt verwezen naar een index die buiten het bereik van een lijst valt.
                     (Listenin sınırları dışında bir indekse erişilmeye çalışıldığında.)

5. KeyError        : Een gezochte sleutel (key) wordt niet gevonden in een dictionary.
                     (Sözlükte aranan anahtar bulunamadığında.)

6. FileNotFoundError: Het opgevraagde bestand kan niet worden gevonden op het systeem.
                     (Sistemde aranan dosya bulunamadığında.)
--------------------------------------------------------------------------------------------
"""
def login(student_id, gebruiker_naam):
    # Probeert een student in te loggen op basis van ID en gebruikersnaam.
    # Werpt een Exception als de gegevens niet kloppen.
    student = repository.get_student_met_email(student_id, gebruiker_naam)

    # Controle 1: Bestaat de student?
    if student is None:
        raise ValueError(f"Student niet gevonden met Gebruiker Naam:'\033[1m\033[4m\033[31m{gebruiker_naam}\033[0m' in de database.")
        # \033[ = start van een ANSI-opdracht (dit opent een stijl)
        # \033[1m = zet vetgedrukt aan
        # \033[31m = rode
        # \033[4m = zet onderstreept aan
        # \033[0m = reset de opmaak (anders rest van de tekst draagt nog de stijl

    # Controle 2: Komt het id overeen?
    if student[0] != student_id:
        raise PermissionError(f"\033[1m\033[4m\033[31mOngeldig-ID:{student_id}\033[0m hoort niet bij deze gebruiker.")

    # Als alles goed is, geven we het student-object terug
    # print(f"Opgehaalde student uit database: {student}")
    return student

def toon_login():
    lijn = "=" * 48
    print()
    print(lijn)
    print("  🎉  STUDENTENFEEST — INLOGGEN  🎉")
    print(lijn)
    print("  Voer uw gegevens in om in te loggen.")
    print("-" * 48)
    print(f"U kunt altijd \033[1m\033[4m\033[31m'stop'\033[0m typen om te stoppen")

    student_id     = input("  👤  Student ID      : ")
    if student_id == 'stop':
        gebruiker_naam = 'stop'
        return student_id, gebruiker_naam

    gebruiker_naam = input("  ✉️   Gebruikersnaam : ")
    print(lijn)
    if gebruiker_naam == 'stop':
        student_id = 'stop'
        return student_id ,gebruiker_naam

    return student_id, gebruiker_naam


# 2) MENU SCHERM
def toon_menu(student):
    naam = f"{student[1]} {student[3]}"
    lijn = "=" * 48
    dun  = "-" * 48

    print()
    print(lijn)
    print("  🎉  STUDENTENFEEST — HOOFDMENU  🎉")
    print(lijn)
    print(f"  \033[1m\033[32mWelkom, {naam}\033[0m")
    print(dun)
    print("  1.  👤  Student Toevoegen")
    print("  2.  🍺  Deelname & Consumptie Registreren")
    print("  3.  📊  Bierconsumptie Rapportage Tonen")
    print("  4.  🎫  Toegangkaartje Verwijderen")
    print("  5.  💳  Vriendenpas Verwijderen")
    print("  6.  📝  Consumptie Updaten")
    print("  7.  🚪  Uitloggen / Afsluiten")
    print(lijn)

def toon_student(student):
    lijn = "=" * 48
    dun  = "-" * 48
    geboortedatum = student[4].strftime('%d-%m-%Y') if hasattr(student[4], 'strftime') else student[4]

    print()
    print(lijn)
    print("  ✅  STUDENT SUCCESVOL AANGEMAAKT!")
    print(dun)
    print(f"  ID            : {student[0]}")
    print(f"  Voornaam      : {student[1]}")
    print(f"  Tussenvoegsel : {student[2] if student[2] else '-'}")# Python turnery heel gebruikelijk
    print(f"  Achternaam    : {student[3]}")
    print(f"  Geboortedatum : {geboortedatum}")
    print(f"  E-mail        : {student[5]}")
    print(lijn)

def toon_feesten_menu():
    feesten = []
    feesten_ids = []
    for feest in repository.get_alle_feesten():
        feesten.append(feest)
        feesten_ids.append(feest[0])

    lijn = "=" * 52
    dun  = "-" * 52

    print()
    print(lijn)
    print("  🎪  FEESTENLIJST — LAATSTE 4 MAANDEN")
    print(lijn)
    print(f"  {'ID':<5} {'FEEST':<22} {'DATUM':<13} PRIJS")
    print(dun)

    for f in feesten:
        # f[0]: id, f[1]: isim, f[2]: tarih, f[3]: entree prijs
        #         # Met .strftime kun je de datum mooier formatteren: f[2].strftime('%d-%m-%Y')
        datum = f[2].strftime('%d-%m-%Y') if hasattr(f[2], 'strftime') else f[2]
        print(f"  🎫 {f[0]:<4} {f[1]:<21} {datum:<13} €{f[3]}")

    print(lijn)
    return feesten, feesten_ids

def toon_afscheid(ingelogde_student):
    naam = ingelogde_student[1]
    lijn = "=" * 48
    print()
    print(lijn)
    print("  🚪  UITLOGGEN...")
    print(lijn)
    print()
    time.sleep(0.5)
    print(f"\n        Tot ziens, {naam}! 👋\n")
    time.sleep(0.5)
    print()
    print(lijn)
    print("  ✅  Sessie afgesloten. Dag! 😊")
    print(lijn)
    print()

def menu_doorverwijzing_animatie(menu_naam):
    print(f"U word doorverwezen naar \033[1m\033[4m\033[34m{menu_naam.upper()}\033[0m....🔄️")
    time.sleep(1.5)

def main_menu(ingelogde_student):
    while True:
        toon_menu(ingelogde_student)
        print(f"U kunt altijd \033[1m\033[31m'stop'\033[0m typen om te stoppen")
        keuze = input("\033[1m\033[34mMaak een keuze uit het menu:\033[0m ")
        if keuze.isdigit():
            keuze = int(keuze)
            if keuze not in range(1,8):#[1, 2, 3, 4, 5, 6, 7]
                print(f"❌ {keuze} moet een getaal tussen 1-7: ")
                time.sleep(2)
                continue
        elif keuze == 'stop':
            toon_afscheid(ingelogde_student)
            break
        else:
            print(f"❌ {keuze} is een ongeldige invoer! voer alstublieft een positief getaal: ")
            time.sleep(2)
            continue
        if keuze == 1:
            menu_doorverwijzing_animatie('STUDENT TOEVOEGEN')
            nieuwe_student = save_student()
            # terug = False
            while True:
                if nieuwe_student == "terug": # het breekt de deze while moet ik nog een andere flag toevoegen om hoofd menu terug te keren
                    break
                elif nieuwe_student:
                    toon_student(nieuwe_student)
                    break
                else:
                    print("❌ Ongeldige invoer! Voer alstublieft \033[1m\033[31m'terug'\033[0m in.")
        elif keuze == 2:
            menu_doorverwijzing_animatie('DEELNAME & CONSUMPTIE REGISTREREN')
        # WELKE FEESTEN GEWEEST
            feesten_ids = toon_feesten_menu()[1]
            gekozen_feesten = []
            print(f"U kunt altijd \033[1m\033[31m'terug'\033[0m typen om hoofdmenu terug te keren")
            print(f"Als u de feesten heeft gekozen type \033[1m\033[31m'klaar'\033[0m")
            terug = False
            while True:
                feest_keuze = input("Welke feesten bent u geweest? typ \033[1m\033[34m'Feest ID'\033[0m "
                                    "of typ \033[1m\033[34m'klaar'\033[0m: ")
                if feest_keuze.lower() == 'klaar':
                    if not gekozen_feesten: # Deze checkt of gebruiker eerste klaar schrijft
                        # want als het eerste klaar dan word de gebruiker doorverwezen naar hoofdmenu
                        menu_doorverwijzing_animatie('hoofdmenu')
                        break
                    print(f"\n")
                    print(f"U moet nu aantal bieren geven per feest..... 🔄")
                    time.sleep(2) # wacht 2 seconden daarna voer de break
                    break
                elif feest_keuze.lower() == 'terug':
                    menu_doorverwijzing_animatie('hoofdmenu')
                    terug = True
                    break

                if feest_keuze.isdigit():
                    feest_id = int(feest_keuze)
                    if feest_id in feesten_ids:
                        if feest_id in gekozen_feesten:
                            print(f"⚠️ Je hebt feest met ID {feest_id} al toegevoegd!")
                        else:
                            gekozen_feesten.append(feest_id)
                            print(f"✅ Toegevoegd: {gekozen_feesten}\n")
                    else:
                        print(f"❌ ID {feest_id} staat niet in het menu.")
                else:
                    print("🚫Typ een positief \033[1m\033[31m'getal'\033[0m voor de feest of \033[1m\033[31m'terug'\033[0m voor de hoofdmenu")
            if terug: # terug naar hoofdmenu break de eerste while in menu-2
                continue
            # HOEVEEL BIER GECONSUMEERD IN DEZE FEESTEN
            is_gelukt = False
            terug = False
            for feestid in gekozen_feesten:
                kaartje = repository.get_kaartje(ingelogde_student[0], feestid)
                # om te voorkomen de dubbele kaartje en deelname voor een feestje
                if kaartje:
                    # Heeft al een kaartje, update alleen consumptie
                    print(f"✅ Feest-{feestid}: je hebt al een registratie.")
                    while True:
                        nieuwe_aantal_bieren = input(f"Nieuw aantal biertjes voor het feest-{feestid}: ")
                        if nieuwe_aantal_bieren.lower() == 'terug':
                            terug = True
                            break
                        if nieuwe_aantal_bieren.isdigit():
                            break
                        print("❌ Ongeldige invoer! Voer alstublieft alleen positieve cijfers in.")
                    if terug:
                        break
                    print(f"Wij zijn bezig met het creeern nieuwe kaart-deelname-consumptie voor u...🔄")
                    time.sleep(2)
                    is_gelukt = consumptie_wijzigen(kaartje[0][0], int(nieuwe_aantal_bieren))
                else:
                    # Heeft geen kaartje voor de feest -- creeert alles
                    print(f"✅ Feest-{feestid}: je hebt geen registratie.")
                    terug = False
                    while True:
                        aantal_bieren = input(f"Hoeveel bier bij het feest-{feestid} voor registratie: ")
                        if aantal_bieren.lower() == 'terug':
                            terug = True
                            break
                        if aantal_bieren.isdigit():
                            break
                        print(f"❌ Alleen positieve getallen.")
                    if terug:# voor "for" : stopt de "for" loop
                        break
                    print(f"Wij zijn bezig met het creeern nieuwe kaart-deelname-consumptie voor u...🔄")
                    time.sleep(2)
                    is_gelukt = registreer_kaart_deelname(ingelogde_student[0], feestid, int(aantal_bieren))
            if terug: # terug naar hoofdmenu break de eerste while in menu-2
                continue
            if is_gelukt:
                print(f"✅WIJZIGINGEN voor de feesten-{gekozen_feesten} SUCCESVOL OPGESLAGEN✅")
                # menu_doorverwijzing_animatie('hoofdmenu')
        elif keuze == 3:
            menu_doorverwijzing_animatie("BIERCONSUMPTIE RAPPORTAGE TONEN")
            print(f"\n\n")
            toon_rapportage(ingelogde_student[0])
            while True:
                keuze = input(f"Typ \033[1m\033[31m'terug'\033[0m voor het menu: ")
                if keuze == 'terug':
                    menu_doorverwijzing_animatie('hoofdmenu')# wacht drie seconden daarna voer de break
                    break
                else:
                    print("❌ Ongeldige invoer! Voer alstublieft \033[1m\033[31m'terug'\033[0m in.")
        elif keuze == 4:
            menu_doorverwijzing_animatie("TOEGANGKAARTJE VERWIJDEREN")
            while True:
                kaart_nmr = input(f"Typ \033[1m\033[31m'terug'\033[0m voor het hoofdmenu \nof \033[1m\033[32m'Kaart ID'\033[0m in om te verwijderen: ")
                if kaart_nmr.isdigit():
                    kaart_nmr_int = int(kaart_nmr)
                    result = repository.delete_toegangkaartje(kaart_nmr_int)
                    print(f"Kaart:{kaart_nmr_int} word verwijderen.....🔄")
                    time.sleep(1.5)
                    print(f"result : {result}")
                    if "bestaat niet" in result:
                        print("❌😬",result)
                    else:
                        # print(f"Toegangkaartje met id {kaart_nmr} is verwijderd")
                        menu_doorverwijzing_animatie('hoofdmenu')
                        break
                elif kaart_nmr.lower() == "terug":
                    menu_doorverwijzing_animatie('hoofdmenu') # wacht drie seconden daarna voer de break
                    break
                else:
                    print("❌ Ongeldige invoer! Voer alstublieft een getal in.")
        elif keuze == 5:
            menu_doorverwijzing_animatie("VRIENDENPAS VERWIJDEREN")
            while True:
                pas_nmr = input(f"Voer de \033[1m\033[32m'pas💳 nummer'\033[0m in om te verwijderen of typ \033[1m\033[31m'terug'\033[0m voor het menu :")
                if pas_nmr.isdigit():
                    pas_nmr_int = int(pas_nmr)
                    result = repository.delete_vriendenpas(pas_nmr_int)
                    print(f"result : {result}")
                    if "bestaat niet" in result:
                        print("❌😬",result)
                    else:
                        print(f"Vriendenpas met id \033[1m\033[4m\033[32m{pas_nmr}\033[0m is verwijderd")
                        menu_doorverwijzing_animatie('hoofdmenu')
                        break
                elif pas_nmr.lower() == "terug":
                    menu_doorverwijzing_animatie('hoofdmenu') # wacht drie seconden daarna voer de break
                    break
                else:
                    print("❌ Ongeldige invoer! Voer alstublieft een getal in.")
        elif keuze == 6:
            print(f"U kunt altijd \033[1m\033[4m\033[31m'terug'\033[0m typen voor het hoofdmenu")
            while True:
                kaart_nmr = input(f"Geef \033[1m\033[4m\033[34m'Kaart-ID'\033[0m alstublieft om aantal bieren te updaten: ")
                if kaart_nmr == 'terug':
                    wilt_u_terug_naar_menu(kaart_nmr)
                    break
                if kaart_nmr.isdigit() and int(kaart_nmr) > 0:# kart nummer moet een getal en positief
                    kaart = repository.get_kaartje_met_kaart_id(int(kaart_nmr))
                    if kaart:
                        nieuwe_aantal_bieren = input("Geef nieuwe \033[1m\033[4m\033[34maantal bieren:\033[0m ")
                        if nieuwe_aantal_bieren.isdigit():
                            # print(f"Aantal bieren van de feest met Kaart-ID:{kaart_nmr} word geüpdatet....🔄 ")
                            consumptie_alleen_update(int(kaart_nmr), int(nieuwe_aantal_bieren))
                            time.sleep(2)
                            break
                        else:
                            print("❌  \033[1m\033[4m\033[31mOngeldige invoer!\033[0m Voer alstublieft een getal in.")
                    else:
                        print(F"❌ \033[1m\033[4m\033[31mKaart met ID:{kaart_nmr}\033[0m bestaan niet voer juiste kaart id!!!")
                else:
                    print("❌ type \033[1m\033[4m\033[31m'terug'\033[0m of \033[1m\033[4m\033[31mOngeldige invoer!\033[0m Voer alstublieft een getal in.")
        elif keuze == 7:
            toon_afscheid(ingelogde_student)
            break


# 3) STUDENT TOEVOEGEN VOOR DE SITUATIES BENEDEN;
#     A) TERWIJL INLOGGEN
#     B) ALS KEUZE-1 IN MENU
def save_student():
    is_created = False
    nieuwe_student = []
    print(f"U kunt altijd \033[1m\033[31m'terug'\033[0m typen om hoofdmenu terug te keren")
    while not is_created:
        try:
            naam = set_juiste_naam()
            if wilt_u_terug_naar_menu(naam):
                return naam
            tussenvoegsel = set_juiste_tussenvoegsel()
            if wilt_u_terug_naar_menu(tussenvoegsel):
                return tussenvoegsel
            achternaam = set_juiste_achternaam()
            if wilt_u_terug_naar_menu(achternaam):
                return achternaam
            geboortedatum = set_juiste_geboortedatum()
            if wilt_u_terug_naar_menu(geboortedatum):
                return geboortedatum
            while True:
                email = set_juiste_email()
                if wilt_u_terug_naar_menu(email):
                    return email
                try:
                    student = repository.create_student(naam, tussenvoegsel, achternaam, geboortedatum, email)
                    nieuwe_student = student
                    is_created = True
                    toon_student(student)
                    return student
                except Exception as e:
                    if "1062" in str(e):
                        print(f"❌ Dit e-mailadres is al in gebruik! Probeer een ander e-mailadres.")
                else:
                    raise
        except Exception as e:
            print(f"Fout: {e}")
    return nieuwe_student
# Terwijl student worden gecreëerd deze zijn
# belangrijk. Ze controlleren de input en
# zetten de geboortedatum-input in juiste
# DATE format anders geeft database foutje
# Ik heb hier dit probleem gehandeld met deze
# twee functie in service.
def set_juiste_naam():
    while True:
        try:
            naam =input("\033[1m\033[4m\033[34mNaam:\033[0m ").strip() # dit strip haal de gatjes van alle kanten weg.
            # Als de gebruiker niks invult, is de waarde een lege string ("")
            if naam == "":
                print("❌ Naam is verplicht! Probeer het opnieuw.")
                continue
            return naam
        except Exception as e:
            print(f"Fout: {e}")

def set_juiste_tussenvoegsel():
    while True:
        try:
            tussenvoegsel = input("\033[1m\033[4m\033[34mTussenvoegsel:\033[0m ")
            if tussenvoegsel.strip() == "":
                tussenvoegsel = None  # Dit wordt vertaald naar NULL in SQL
            else:
                tussenvoegsel = tussenvoegsel
            return tussenvoegsel
        except Exception as e:
            print(f"Fout: {e}")

def set_juiste_achternaam():
    while True:
        try:
            achternaam =input("\033[1m\033[4m\033[34mAchternaam:\033[0m ").strip() # dit strip haal de gatjes van alle kanten weg.
            # Als de gebruiker niks invult, is de waarde een lege string ("")
            if achternaam == "":
                print("❌ Achternaam is verplicht! Probeer het opnieuw.")
                continue
            return achternaam
        except Exception as e:
            print(f"Fout: {e}")

def set_juiste_geboortedatum():
    while True:
        try:
            geboortedatum= input("\033[1m\033[4m\033[34mGeboortedatum YYYY-MM-DD:\033[0m ")
            # Als geboorte datum juist werden ingevoerd teruggeeft True:
            if geboortedatum.strip() == "terug": #geeft terug als gebruiker typet in deze regel "terug"
                return "terug"
            elif valideer_database_datum(geboortedatum):
                return geboortedatum
            break # als het niet gevalideerd datum en niet "terug" dan het betekent dat het ongeldige datum invoer
        except Exception as e:
            print(f"Fout: {e}")
            print("Voer geboortedatum in juiste format YYYY-MM-DD")

def valideer_database_datum(datum_string):
    """
    Controleert of de datum EXACT het formaat YYYY-MM-DD heeft.
    De symbolen met een procentteken (%) noemen we format specifiers (indelingsteken).
    Ze vertellen Python hoe een datum-string gelezen of geschreven moet worden.
    """
    formaat = "%Y-%m-%d"
    try:
        # Eğer tarih bu formata uymuyorsa veya geçersizse (örn: 2026-02-30) ValueError fırlatır
        # Visuele weergave van het proces:
        # INVOER (String)   : "2026-05-14"
        # FORMAT (Sjabloon) : "%Y-%m-%d"
        # RESULTAAT (Object): datetime.datetime(2026, 5, 14, 0, 0)
        datetime.strptime(datum_string, formaat)
        return True
    except ValueError:
        raise ValueError("Ongeldige datum of onjuist formaat. Gebruik YYYY-MM-DD.")

def set_juiste_email():
    while True:
        try:
            # Vraag de gebruiker om een e-mailadres dat voldoet aan de eisen
            email= input("\033[1m\033[4m\033[34mEmail (@ad.hva.nl / @vu.nl):\033[0m ").strip()
            # Voer de validatie uit vóórdat de data naar de database gaat
            if email == 'terug':
                return email
            elif valideer_email(email):
                return email
            # break
        except ValueError as e:
            print(f"Fout: {e}")
            print("Voer email in juiste format (@ad.hva.nl / @vu.nl):")
# Terwijl student worden gecreëerd deze zijn
# belangrijk. Ze controlleren de input en
# zetten de email-input in juiste
# regex die als een constrait in student tabel zijn.
# anders geeft database foutje
# Ik heb hier dit probleem gehandeld met deze
# twee functie in service.
def valideer_email(email_string):
    # Het RegEx-patroon dat exact gelijk is aan de database CHECK-constraint
    patroon = r"^[a-zA-Z0-9._%+-]+@(ad\.hva\.nl|vu\.nl)$"

    # re.match() controleert of de string volledig overeenkomt met het patroon
    if not re.match(patroon, email_string):
        raise ValueError("Ongeldig domein of formaat. Gebruik @ad.hva.nl of @vu.nl.")
    return True

def wilt_u_terug_naar_menu(invoer):
    if invoer == "terug":
        menu_doorverwijzing_animatie('Hoofdmenu')
        return invoer


# 4) DEELNAME EN CONSUMPTIE REGISTREREN
    # Wij doen deze in menu keuze 2 en maken daarvoor gebruik
    #  van deze functie
def registreer_kaart_deelname(student_id, feest_id, aantal_bieren):
    # Als er GEEN bestaande 'toegangkaartje' dan creeeren wij eerst
    # een toegangkaartje hier:
    # Nieuwe opslaan
    kaartje_result = repository.create_toegangkaartje(student_id, feest_id)
    if isinstance(kaartje_result, str): #create toegangkaartje geeft string als het fout is.
        print(f"❌ {kaartje_result}")
        return False
    kaart_id = kaartje_result[0][0]


    # Daarna creeeren wij een deelname gerelateerd met de toegangkaartje die
    # hierboven werd gecreëerd
    deelname_result = repository.create_deelname(kaart_id)
    deelname_id = deelname_result[0][0]

    consumptie = repository.create_consumptie(deelname_id, aantal_bieren)
    consumptie_id = consumptie[0][0]
    toon_consumptie_na_de_wijziging(kaart_id, deelname_id, consumptie_id, aantal_bieren, "(Kaart + Deelname + Consumptie)-Creëren")
    # print("\n" + "="*50)
    # print(f"🎉 SUCCESS: Kaart-Deelname succesvol geregistreerd! 🚀")
    # print("="*50)
    # print(f"🎫 Toegangskaart ID : {kaart_id}")
    # print(f"🆔 Deelname ID      : {deelname_id}")
    # print(f"🍻 Aantal bieren   : {aantal_bieren} consumptie(s)")
    # print("="*50 + "\n")
    return True


# 5) BIERCONSUMPTIE RAPPORTAGE TONEN
def bepaaldureavond(aantal_biertjes):
    if aantal_biertjes > 30:
        return True
    else:
        return False

def toon_rapportage(student_id):
    rows = repository.get_kosten_voor_student(student_id)
    beoordeling = repository.get_beoordeling_met_id(student_id)

    lijn = "=" * 52
    dun  = "-" * 52

    print()
    print(lijn)
    print("  📊  BIERCONSUMPTIE RAPPORTAGE")
    print(lijn)

    if not rows:
        print("Geen registraties gevonden.")
        print(lijn)
        return

    print(f"\n{'FEEST':<25} {'BIER':>4}  {'KOSTEN':<50}")

    print("-" * 52)

    totaal_bieren = 0
    for rij in rows:
        naam, datum, thema, bieren, kosten = rij #"Tuple Unpacking:
        # Hiermee kun je een rij met data in één keer uitpakken
        # en aan verschillende variabelen toewijzen."
        # print(f"rij: {rij}")
        totaal_bieren += bieren
        duur = " 🔥dure avond!" if bepaaldureavond(kosten) else ""
        print(f"🍺   {thema:<15} {bieren:>7}  {kosten:>7.2f}{duur}")
        # Dit is turnery syntax for python:
        # waarde = [resultaat_als_waar] if [voorwaarde] else [resultaat_als_niet_waar]

    gemiddeld = round(totaal_bieren / len(rows),2)
    print(lijn)
    print(f"  Totaal bieren  : {totaal_bieren}")
    print(f"  Gemiddeld      : {gemiddeld} per feest")
    print(dun)
    beoordeling_tekst = beoordeling[0] if beoordeling else "Geen beoordeling" #Beordeling kan 'None' teruggeven
    print(f"  Beoordeling    : {beoordeling_tekst}")
    print(lijn)

    # print(f"\nJe hebt in totaal {totaal_bieren} biertjes gedronken.")
    # print(f"Dat is gemiddeld {gemiddeld} per feest.")
    # print(f"Beoordeling van ons:{beoordeling[0]}")


# 6) CONSUMPTIE UPDATE - GEBRUIKT IN MENU KEUZE-2
def consumptie_wijzigen(kaart_id, aantal_bieren):
    consumptie = repository.get_consumptie_met_kaart_id(kaart_id)
    if consumptie is None:
        # Geen deelname? → deelname aanmaken + consumptie aanmaken
        # Eerst creëert deelname
        deelname = repository.create_deelname(kaart_id)
        if isinstance(deelname, str):#We willen vaststellen of het een string is.
            print(deelname) # dan drukken we af die string want die string is foutmelding
            return False # gaat niet meer beneden
        deelname_id = deelname[0][0]
        # Daarna creëert consumptie
        result = repository.create_consumptie(deelname_id, aantal_bieren)
        consumptie_id = result[0][0]
        # print(repository.create_consumptie(deelname_id, aantal_bieren))
        # if not result[0]:
        #     print(f"Een probleen ontstaan binnen service.consumptie_wijzigen() : {result} ")
        toon_consumptie_na_de_wijziging(kaart_id, deelname_id, consumptie_id, aantal_bieren, "(Deelname + Consumptie)-Creëren")
        is_gelukt = True
    elif consumptie[1] is None: #consumptie[1] ====> consumptie_id
        # Deelname bestaat, consumptie nog niet → alleen consumptie aanmaken
        deelname_id = consumptie[0]
        # print(repository.create_consumptie(deelname_id, aantal_bieren))
        result = repository.create_consumptie(deelname_id, aantal_bieren)
        consumptie_id = result[0][0]
        toon_consumptie_na_de_wijziging(kaart_id, deelname_id, consumptie_id, aantal_bieren, "Consumptie-Creëren")
        is_gelukt = True
        # if not is_gelukt:
        #     print(f"Een probleen ontstaan binnen service.consumptie_wijzigen() : {is_gelukt[1]} ")
    else:
        # Beide bestaan → update consumptie
        consumptie_id = consumptie[1]
        deelname_id = consumptie[0] #consumptie[1] ====> consumptie_id
        # print(repository.update_consumptie_aantal_bieren(consumptie_id, aantal_bieren))
        result = repository.update_consumptie_aantal_bieren(consumptie_id, aantal_bieren)
        print(result)
        toon_consumptie_na_de_wijziging(kaart_id, deelname_id, consumptie_id, aantal_bieren, "Consumptie-Wijzigen (menu-2)")
        is_gelukt = True if "gewijzigd naar" in result else False
    return is_gelukt

def toon_consumptie_na_de_wijziging(kaart_id, deelname_id, consumptie_id, aantal_bieren, operatie):
    print("\n" + "="*50)
    print(f"🎉 SUCCESS: {operatie} succesvol uitgevoerd! 🚀")
    print("="*50)
    print(f"🎫 Toegangskaart ID : {kaart_id}")
    print(f"🆔 Deelname ID      : {deelname_id}")
    print(f"🍺 Consumptie ID    : {consumptie_id}")
    print(f"🍻 Aantal bieren    : {aantal_bieren} consumptie(s)")
    print("="*50 + "\n")

# 7) CONSUMPTIE UPDATE - GEBRUIKT IN MENU KEUZE-6
def consumptie_alleen_update(kaart_id, aantal_bieren):
    consumptie = repository.get_consumptie_met_kaart_id(kaart_id)

    if consumptie is None or consumptie[1] is None:
        # Is er geen Deelname of consumptie→ er is niks te updaten
        print(f"❌ Geen consumptie gevonden voor kaartje met ID:{kaart_id}.")
        return

    # Consumptie bestaat → alleen update
    consumptie_id = consumptie[1]
    deelname_id = consumptie[0]
    repository.update_consumptie_aantal_bieren(consumptie_id, aantal_bieren)
    toon_consumptie_na_de_wijziging(kaart_id, deelname_id, consumptie_id, aantal_bieren,"consumptie-wijzigen (menu-6)")










