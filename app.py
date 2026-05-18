# STUDENT FEEST - TECHNO
# Auteur: Gökhan Öztürk


import time
import traceback
import service
import repository
def app():
    ingelogd = False
    ingelogde_student = None
    while not ingelogd:
        try:
                # Probeer in te loggen
                # Vraag de gebruiker om input
                # CRUCIALE CONTROLE: Is de invoer wel een geldig getal?
                # (Girdinin sayı olup olmadığını kontrol eden kritik adım)
            student_id, gebruiker_naam = service.toon_login() # "unpacking" heel goede manier
            if student_id == "stop" or gebruiker_naam == "stop":
                print(f"\n        Tot ziens ! 👋\n")
                time.sleep(0.5)
                break
            elif not student_id.isdigit():
                print("❌ Fout: Het student-ID mag alleen uit positieve cijfers bestaan! Probeer het opnieuw.")
                continue # Start de hoofdlus opnieuw vanaf het begin

            # if gebruiker_naam.lower() == 'stop':
            #     print("Tot ziens...")
            #     break
            else:
                # boven heb ik isdigit() gebruikt, daardoor moest student_id daar string blijven.
                # maar daarna in database om tegen geen probleem te komen heb ik heb hier
                # type-casting gedaan met "int(student_id)"
                ingelogde_student = service.login(int(student_id), gebruiker_naam)
                # Als we hier komen, is het inloggen geslaagd
                # met de combinatie (windows + .) kunnen wij emoji toevoegen.
                print(f"\n🔐 Gegevens controleren... ⏳")
                time.sleep(1.25)
                print(f"🚀 Inloggen voltooid! Een ogenblik geduld... ⏳")
                time.sleep(1.25)
                print(f"Ingelogd✅  Welkom {ingelogde_student[1]}!")
                # print(f"Uw e-mail: {ingelogde_student[5]}")
                print(f"\n\n\n")
                ingelogd = True # Stop de loop

        except ValueError as e:
            # Fout: Student niet gevonden
            print(f"❌ Fout: {e}")
            # Vraag of de gebruiker een nieuw account wil aanmaken
            while True:
                keuze = input("\033[1m\033[34mWilt u een nieuwe student aanmaken? (ja/nee):\033[0m ")
                if keuze.lower() == 'ja':
                    print("Schakelen naar \033[1m\033[4m\033[34m'CREATE STUDENT'\033[0m module...🔄️")
                    time.sleep(2)
                    # Hier create_student functie aanroepen
                    nieuwe_student = service.save_student()
                    if nieuwe_student == "terug":
                        break
                    # ingelogde_student = service.login(nieuwe_student[0], gebruiker_naam)
                    # Als we hier komen, is het inloggen geslaagd
                    # met de combinatie (windows + .) kunnen wij emoji toevoegen.
                    print(f"✅ Ingeschreven Welkom {nieuwe_student[1]}! nu Kunt u "
                          f"\033[1m\033[4m\033[34m'met id:'\033[0m \033[1m\033[4m\033[33m{nieuwe_student[0]}\033[0m en "
                          f"met de \033[1m\033[4m\033[34m'gebruiker naam:'\033[0m \033[1m\033[4m\033[33m{nieuwe_student[5].split('@')[0]} \033[0m inloggen")
                    break # Stop de login loop na doorverwijzen
                elif keuze.lower() == 'nee':
                    print("U word doorgestuurd naar het hoofdmenu...")
                    # ingelogd = True
                    break
                else:
                    print("u moet alleen maar 'ja' of 'nee' invoeren!!!")
        except PermissionError as e:
            # Fout: ID klopt niet (maar student bestaat)
            print(f"🚫 Toegang geweigerd: {e}")
            print("Probeer het opnieuw.")
        except Exception as e:
            # Voor onverwachte of algemene fouten
            traceback.print_exc()
            print(f"⚠️ Er is een onbekende fout opgetreden: {e}")

    # print(f"inlogde student: {ingelogde_student}")
    if ingelogd:
        print(f"\n\n")
        service.main_menu(ingelogde_student)
        print(f"\n\n")
    # print(a)