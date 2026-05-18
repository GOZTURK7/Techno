# STUDENT FEEST - TECHNO
# Auteur: Gökhan Öztürk

import db_connection
# CRUD FUNCTIES (CREATE, READ, UPDATE, DELETE)


# ===================================================================================================================================
#                                           A. CREATE FUNCTIES
# ===================================================================================================================================
def create_student(naam, tussenvoegsel, achternaam, geboortedatum, email):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = """INSERT INTO `Student` (`voornaam`, 
    `tussenvoegsel`, `achternaam`, `geboortedatum`, `email`) VALUES
(%s, %s, %s, %s, %s)"""
    params = (naam, tussenvoegsel, achternaam, geboortedatum, email)
    try:
        mycursor.execute(query, params)
        mydb.commit()
        last_id = mycursor.lastrowid
        query = "select * from student where student_id = %s"
        mycursor.execute(query, (last_id,))
        student = mycursor.fetchone()
        return student
    except Exception as e:
        # Je gebruikt rollback() in een except-blok.
        # Als er een fout (foutmelding) optreedt tijdens het uitvoeren van je SQL-query,
        # zorgt de rollback ervoor dat de database terugkeert naar de oude staat.
        mydb.rollback()
        raise Exception(f"Er is een fout opgetreden: {e}")  # return → raise

    finally:
        mycursor.close()
        mydb.close()

def create_vriendenpas(student_id, aankoop_datum):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = """INSERT INTO `Vriendenpas` (`student_id`, `aankoop_datum`) VALUES
(%s, %s)"""
    params = (student_id, aankoop_datum)
    try:
        mycursor.execute(query, params)
        mydb.commit()
        id = mycursor.lastrowid
        return (f"aan student met id: {student_id} op deze datum: {aankoop_datum} "
                f"een nieuwe vriendenpas met id: {id} succesvol toegevoegad!")
    except Exception as e:
        # Je gebruikt rollback() in een except-blok.
        # Als er een fout (foutmelding) optreedt tijdens het uitvoeren van je SQL-query,
        # zorgt de rollback ervoor dat de database terugkeert naar de oude staat.
        mydb.rollback()
        return f"Er is een fout opgetreden: {e}"
    finally:
        mycursor.close()
        mydb.close()

def create_feest(thema, datum):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = """INSERT INTO `Feest` (`thema`, `datum`) VALUES
            (%s, %s)"""
    params = (thema, datum)
    try:
        mycursor.execute(query, params)
        mydb.commit()
        last_id = mycursor.lastrowid

        # Haal de neuwe toegevoegde feest object
        select_query = "SELECT * FROM Feest WHERE feest_id = %s"
        mycursor.execute(select_query, (last_id,))
        feest = mycursor.fetchone()

        return feest, (f"aan Feest met id: {last_id} voor deze datum: {datum} met deze thema: {thema} "
                f"een nieuwe feest succesvol toegevoegad!")
    except Exception as e:
        mydb.rollback()
        return f"Er is een fout opgetreden!:  {e}"
    finally:
        mycursor.close()
        mydb.close()

def create_toegangkaartje(student_id, feest_id):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = """INSERT INTO `Toegangkaartje` (`student_id`,`feest_id`) values (%s, %s)"""
    params = (student_id, feest_id)
    try:
        mycursor.execute(query, params)
        mydb.commit()
        last_id = mycursor.lastrowid

        # Haal de nieuwe toegevoegde feest object
        select_query = "SELECT * FROM Toegangkaartje WHERE kaart_id = %s"
        mycursor.execute(select_query, (last_id,))
        toegangkaartje = mycursor.fetchone()
        return toegangkaartje, (f"aan Toegangkaartje met id: {last_id}  "
                   f"een nieuwe toegangkaartje succesvol toegevoegad!")
    except Exception as e:
        mydb.rollback()
        return f"Er is een fout opgetreden!:  {e}"
    finally:
        mycursor.close()
        mydb.close()

def create_deelname(kaart_id):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = "insert into deelname (kaart_id) values (%s)"
    params = (kaart_id,)
    try:
        mycursor.execute(query, params)
        mydb.commit()
        last_id = mycursor.lastrowid

        # Haal de nieuwe toegevoegde deelname object
        select_query = "SELECT * FROM deelname WHERE deelname_id = %s"
        mycursor.execute(select_query, (last_id,))
        deelname = mycursor.fetchone()
        return deelname, (f"aan Deelname met id: {last_id}  "
                                f"een nieuwe deelname succesvol toegevoegad!")
    except Exception as e:
        mydb.rollback()
        return f"Er is een fout opgetreden!:  {e}"
    finally:
        mycursor.close()
        mydb.close()
# print(create_deelname(105))
# returned : ((77, 105, datetime.datetime(2026, 5, 13, 22, 53, 3)), 'aan Deelname met id: 77 een nieuwe deelname succesvol toegevoegd!')

def create_consumptie(deelname_id, aantal_bieren):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = "insert into consumptie (deelname_id, aantal_bieren) values (%s, %s)"
    params = (deelname_id, aantal_bieren)

    try:
        mycursor.execute(query, params)
        mydb.commit()
        last_id = mycursor.lastrowid

        # Haal de nieuwe toegevoegde consumptie object
        select_query = "select * from consumptie where consumptie_id = %s"
        mycursor.execute(select_query, (last_id,))
        consumptie = mycursor.fetchone()
        return consumptie, (f"aan Consumptie met id: {last_id}  "
                            f"een nieuwe consumptie succesvol toegevoegad!")
    except Exception as e:
        mydb.rollback()
        return f"Er is een fout opgetreden!:  {e}"
    finally:
        mycursor.close()
        mydb.close()
# print(create_consumptie(77, 12))
# returned: ((77, 77, 12), 'aan Consumptie met id: 77 een nieuwe consumptie succesvol toegevoegd!')


# ===================================================================================================================================
#                                           B. READ FUNCTIES
# ===================================================================================================================================
# 1 Geeft het overzicht van alle tabellen
def get_overzicht_alles():
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = (" select \n"
             "student_id,\n"
             "voornaam,\n"
             "achternaam,\n"
             "thema,\n"
             "datum \n"
             "from\n"
             "(SELECT s.student_id, voornaam, achternaam, thema, datum\n"
             "FROM student s\n"
             "join toegangkaartje t on s.student_id = t.student_id\n"
             "join deelname d on t.kaart_id = d.kaart_id\n"
             "join feest f on f.feest_id = t.feest_id\n"
             "join consumptie c on c.deelname_id = d.deelname_id) overzicht\n"
             "order by student_id asc \n")
    mycursor.execute(query)
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows

# 2 Kosten per student per feest
def get_kosten_per_student_per_feest():
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = ("""select student_id, naam, datum, 
    thema, totale_kosten from v_kosten_per_feest_per_student order by student_id asc""")
    mycursor.execute(query)
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows

def get_kosten_voor_student(student_id):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = """
        SELECT naam, datum, thema, aantal_bieren, totale_kosten
        FROM v_kosten_per_feest_per_student
        WHERE student_id = %s
        ORDER BY datum desc limit 4
    """
    mycursor.execute(query, (student_id,))
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows

# 3 Totaal gedronken bieren (alle studenten samen)
def get_total_gedronken_bieren():
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = ("""select sum(totale_bieren) as totale_gedronken_bieren 
from v_statistieken_per_student""")
    mycursor.execute(query)
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows

# 4 Totale bieren per student (met ook null waarde)
def get_total_bieren_per_student():
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = ("""select student_naam, totale_bieren
from v_statistieken_per_student""")
    mycursor.execute(query)
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows

# 5 Gemiddelde bieren per feest per student
def get_gem_bier_per_feest_per_student():
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = ("""select student_naam, gemiddelde_bieren_per_feest
    from v_statistieken_per_student""")
    mycursor.execute(query)
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows

# 6 Feestoverzicht met kaartjes en aanwezigheid
def get_feestoverzicht_met_kaart_aanwezigheid():
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = ("""SELECT
    f.datum,
    f.thema,
    COUNT(DISTINCT tk.kaart_id)			AS verkochte_kaartjes,
    SUM(tk.status = 'geannuleerd')		AS geannuleerd,
    COUNT(DISTINCT d.deelname_id)		AS daadwerkelijk_aanwezig,
	COUNT(DISTINCT		-- De CASE-expressie doorzoekt de hele lijst, rij voor rij, 
			CASE		-- om te bepalen welke waarden aan de voorwaarden voldoen.(when = if en then = return)
				WHEN d.kaart_id IS NULL AND tk.status = 'verkocht' 
				THEN tk.kaart_id 
			END) 						AS betaald_maar_niet_meegedaan
FROM Feest f
LEFT JOIN Toegangkaartje tk ON f.feest_id    = tk.feest_id
LEFT JOIN Deelname d        ON tk.kaart_id   = d.kaart_id
LEFT JOIN Consumptie c      ON d.deelname_id = c.deelname_id
GROUP BY f.feest_id, f.datum, f.thema
ORDER BY f.datum""")
    mycursor.execute(query)
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows

# 7 Actieve en passieve vriendenpassen
def get_actieve_passieve_vriendenpassen():
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = ("""select *, (case when verval_datum >= now() then 'actief' else 'passief' end) as kaart_status
from vriendenpas order by student_id""")
    mycursor.execute(query)
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows

# 8 Aantal passieve en actieve karten per student
def get_actieve_passieve_vriendenpassen_per_student():
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = ("""select 
student_id, 
count(pas_id) total_pas,
count(case when verval_datum >= now() then 'actieve' end) as total_actieve_kart,
count(case when verval_datum < now() then 'passieve' end) as total_passieve_kart
from vriendenpas
group by student_id order by student_id""")
    mycursor.execute(query)
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows

# 9 Zoek studenten met e-mailadres
def get_student_met_email(student_id, gebruiker_naam):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = """SELECT * FROM student
                WHERE email LIKE %s OR email LIKE %s"""
    params = (f"{gebruiker_naam}@vu.nl", f"{gebruiker_naam}@ad.hva.nl")
    mycursor.execute(query, params)
    rows = mycursor.fetchall() # als er twee email zoals yusi@vu.nl en yusi@ad.hva.nl is
    # dan return het 2 student dus als er fethone() zou zijn dan return het eerste value en veroorzakt crash
    mycursor.close()
    mydb.close()
    for row in rows: # als er twee student met hetzelfde gebruiker_naam dan kiezen wij student die zijn id gelijk is aan student_id
        if row[0] == student_id:
            return row
    return None

# 10 studenten die MEER dan gemiddeld dronken
def get_studenten_meer_dan_gem_dronken():
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = """select	student_id, 
		student_naam, 
        totale_bieren,
		round((select avg(totale_bieren) from v_statistieken_per_student),2) as gemiddelde
        from v_statistieken_per_student
        where totale_bieren > (round((select avg(totale_bieren) from v_statistieken_per_student),2))"""
    mycursor.execute(query)
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows

# 11 Get alle feesten:
def get_alle_feesten():
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = """
        SELECT * FROM feest
        WHERE datum >= DATE_SUB(NOW(), INTERVAL 6 MONTH)
        AND datum <= NOW()
        ORDER BY datum ASC
        limit 4
    """ # Geeft terug de feesten van laatste 4 maanden
    mycursor.execute(query)
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows
# print(get_alle_feesten())
# Returned: [(1, 'Techno Night', datetime.datetime(2025, 1, 16, 22, 0), Decimal('19.50'), 4, Decimal('2.80')),
# (2, 'Neon Party', datetime.datetime(2025, .....

def get_kaartje(student_id, feest_id):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = """select * from toegangkaartje where student_id = %s and feest_id = %s"""
    params = (student_id, feest_id)
    mycursor.execute(query, params)
    rows = mycursor.fetchall()
    mycursor.close()
    mydb.close()
    return rows

def get_kaartje_met_kaart_id(kaart_id):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = "select * from toegangkaartje where kaart_id = %s"
    params = (kaart_id,)
    mycursor.execute(query, params)
    row = mycursor.fetchone()
    mycursor.close()
    mydb.close()
    return row

def get_consumptie_met_kaart_id(kaart_id):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = """
        SELECT d.deelname_id, c.consumptie_id, c.aantal_bieren
        FROM deelname d
        LEFT JOIN consumptie c ON c.deelname_id = d.deelname_id
        WHERE d.kaart_id = %s
    """
    mycursor.execute(query, (kaart_id,))
    row = mycursor.fetchone()
    mycursor.close()
    mydb.close()
    return row

def get_beoordeling_met_id(student_id):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = "SELECT beoordeling FROM studentenfeest.v_drankbeoordeling where student_id = %s;"
    param = (student_id,)
    mycursor.execute(query, param)
    beoordeling = mycursor.fetchone()
    mycursor.close()
    mydb.close()
    return beoordeling


# ===================================================================================================================================
#                                           C. UPDATE FUNCTIES
# ===================================================================================================================================
def update_student(student_id, voornaam=None, tussenvoegsel=None, achternaam=None, geboortedatum=None, email=None):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()

    fields = []
    params = []

    if voornaam is not None:
        fields.append("voornaam = %s")
        params.append(voornaam)

    if tussenvoegsel is not None:
        fields.append("tussenvoegsel = %s")
        params.append(tussenvoegsel)

    if achternaam is not None:
        fields.append("achternaam = %s")
        params.append(achternaam)

    if geboortedatum is not None:
        fields.append("geboortedatum = %s")
        params.append(geboortedatum)

    if email is not None:
        fields.append("email = %s")
        params.append(email)

    # Als er geen parameters werd ingevoerd
    if not fields:
        return "Geen velden om te updaten"

    # Voegt de velden samen met een komma als scheidingsteken
    # Maakt een dynamische SQL-string door de lijst 'fields' te combineren
    # Voorbeeld uitvoer: "update student set voornaam = %s, email = %s WHERE student_id = %s"
    query = f"""
        UPDATE student
        SET {", ".join(fields)}
        WHERE student_id = %s
        """
    params.append(student_id)
    try:
        mycursor.execute(query, params)
        mydb.commit()
        return "Student succesvol bijgewerkt (updated)"
    except Exception as e:
        mydb.rollback()
        return f"Fout: {e}"
    finally:
        mycursor.close()
        mydb.close()
# returned: Student succesvol geüpdatet
# print(update_student(student_id = 1, email="jan.denvries@ad.hva.nl"))

def update_toegangkaartje_status(kaart_id, status):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = """update toegangkaartje set status = %s where kaart_id = %s"""
    try:
        mycursor.execute(query, (status,kaart_id))
        mydb.commit()
        return f"Toegangkaartje-status met id {kaart_id} succesvol geannuleerd (updated)"
    except Exception as e:
        mydb.rollback()
        return f"Fout: {e}"
    finally:
        mycursor.close()
        mydb.close()
# Returned: Toegangkaartje-status met id 102 succesvol geannuleerd (updated)
# print(update_toegangkaartje_status(102, "geannuleerd"))

def update_feest_thema(feest_id, thema):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = "update feest set thema = %s where feest_id = %s"

    try:
        mycursor.execute(query, (thema, feest_id))
        mydb.commit()
        return f"Thema van feest {feest_id} gewijzigd naar '{thema}'."
    except Exception as e:
        mydb.rollback()
        return f"Fout: {e}"
    finally:
        mycursor.close()
        mydb.close()
# Thema van feest 18 gewijzigd naar 'Don't give up'.
# print(update_feest_thema(18, "Don't give up"))

def update_deelname_checkin_tijd(deelname_id, check_in_tijd):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = "update deelname set check_in_tijd = %s where deelname_id = %s"

    try:
        mycursor.execute(query, (check_in_tijd, deelname_id))
        mydb.commit()
        return f"Check_in_tijd van deelname met id: {deelname_id} gewijzigd naar '{check_in_tijd}'."
    except Exception as e:
        mydb.rollback()
        return (f"Fout: {e} Check de Feest datum en toegang kaartje datum; "
                f"check in moet tussen deze zijn en precies op feest datum zijn")
    finally:
        mycursor.close()
        mydb.close()
# Returned: Check_in_tijd van deelname met id: 1 gewijzigd naar '2025-01-16 22:00:11'.
# print(update_deelname_checkin_tijd(1, "2025-01-16 22:00:11"))

def update_consumptie_aantal_bieren(consumptie_id, aantal_bieren):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    query = "update consumptie set aantal_bieren = %s where consumptie_id = %s"

    try:
        mycursor.execute(query, (aantal_bieren, consumptie_id))
        mydb.commit()
        return f"aantal_bieren van consumptie met id: {consumptie_id} gewijzigd naar '{aantal_bieren}'."
    except Exception as e:
        mydb.rollback()
        if 'chk_positief_aantal_bier' in str(e):
            return 'Je mag geen negatieve getallen invullen!'
        return f"Fout: {e}"
    finally:
        mycursor.close()
        mydb.close()
# print(update_consumptie_aantal_bieren(1, 10))
# returned: aantal_bieren van deelname met id: 1 gewijzigd naar '10'.
# print(update_consumptie_aantal_bieren(1, -10))
# Returned: Je mag geen negatieve getallen invullen!

# ===================================================================================================================================
# DELETE FUNCTIES
# ===================================================================================================================================


# ===================================================================================================================================
#                                           D. DELETE FUNCTIES
# ===================================================================================================================================
def delete_toegangkaartje(kaart_id):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()

# Roep ik hier STORED PROCEDURE 4:DELETE TOEGANGKAARTJE
# kaartje + deelname + consumptie cascade
# 1. delete_toegangkaartje(p_kaart_id)
# Verwijdert Consumptie → Deelname → Toegangkaartje in volgorde.
    query = f"CALL delete_toegangkaartje(%s)"
    try:
        mycursor.execute(query, (kaart_id,))
        mydb.commit()
        return f"✅Kaartje met id: {kaart_id} \033[1m\033[32msuccesvol\033[0m verwijderd."
    except Exception as e:
        mydb.rollback()
        if 'Kaartje niet gevonden' in str(e): ## str(e) zet de foutmelding
            # om naar tekst zodat je op specifieke fouten kunt controleren.
            # De MESSAGE_TEXT uit de stored procedure is terug te vinden in str(e).
            return f"Kaartje met id {kaart_id} bestaat niet."
        return f"Fout: {e}"
    finally:
        mycursor.close()
        mydb.close()
# print(delete_toegangkaartje(999))
# Returned: Kaartje met id 999 bestaat niet.
# print(delete_toegangkaartje(105))
# Returned: Kaartje met id 105 succesvol verwijderd.

def delete_vriendenpas(pas_id):
    mydb = db_connection.get_connection()
    mycursor = mydb.cursor()
    # Roep ik hier STORED PROCEDURE 5:DELETE VRIENDENPAS
    # 2. delete_vriendenpas(p_pas_id)
    # Verwijdert alleen de pasregel zelf — geen afhankelijke tabellen, direct te verwijderen.
    # Gebruik: foutief ingevoerde pas corrigeren zonder de student te wijzigen.
    query = "CALL delete_vriendenpas(%s)"
    try:
        mycursor.execute(query, (pas_id,))
        mydb.commit()
        return f"Vriendenpas met id {pas_id} succesvol verwijderd."
    except Exception as e:
        mydb.rollback()
        if 'Vriendenpas niet gevonden' in str(e): ## str(e) zet de foutmelding
            # om naar tekst zodat je op specifieke fouten kunt controleren.
            # De MESSAGE_TEXT uit de stored procedure is terug te vinden in str(e).
            return f"Vriendenpas met id {pas_id} bestaat niet."
        return f"Fout: {e}"
    finally:
        mycursor.close()
        mydb.close()
# print(delete_vriendenpas(27))
# Returned: Vriendenpas met id 27 succesvol verwijderd.
# print(delete_vriendenpas(999))
# Returned: Vriendenpas met id 999 bestaat niet.

