# 🎉 Studentenfeest — Techno 

> **Eindopdracht Databases en Programming — Make It Work | HvA**  
> Auteur: **Gökhan Öztürk** · BDA

---

## 📖 Over het project

Een interactieve Python CLI-applicatie voor het beheren van studentenfeesten.  
Studenten kunnen inloggen, feesten bijhouden, bierconsumptie registreren en rapportages bekijken — allemaal gekoppeld aan een MySQL-database.

---

## ✨ Functionaliteiten

| # | Functie | Beschrijving |
|---|---------|-------------|
| 1 | 🔐 **Inloggen** | Inloggen met student-ID en gebruikersnaam |
| 2 | 🧑 **Student toevoegen** | Nieuw account aanmaken met validatie |
| 3 | 🎪 **Deelname registreren** | Feesten selecteren + bierconsumptie invoeren |
| 4 | 📊 **Rapportage bekijken** | Kosten per feest, totaal bieren, beoordeling |
| 5 | 🗑️ **Toegangskaartje verwijderen** | Kaartje inclusief deelname en consumptie |
| 6 | 🪙 **Vriendenpas verwijderen** | Verlopen of foutief ingevoerde pas verwijderen |
| 7 | 🔄 **Consumptie updaten** | Aantal bieren achteraf aanpassen |

---

## 🗄️ Database structuur

```
Student ──< Toegangkaartje >── Feest
Student ──< Vriendenpas
Toegangkaartje ──|| Deelname ──|| Consumptie
```

| Tabel | Beschrijving |
|-------|-------------|
| `Student` | Studenten met e-mailvalidatie (HvA / VU) |
| `Vriendenpas` | Kortingspas, 12 maanden geldig, 10% korting |
| `Feest` | Altijd op de 3e donderdag van de maand |
| `Toegangkaartje` | Koppeltabel student ↔ feest |
| `Deelname` | Fysieke aanwezigheid bij een feest |
| `Consumptie` | Aantal gedronken bieren per deelname |

---

## 🛠️ Technische stack

![Python](https://img.shields.io/badge/Python-3.14-blue?logo=python)
![MySQL](https://img.shields.io/badge/MySQL-8.0-orange?logo=mysql)
![mysql-connector](https://img.shields.io/badge/mysql--connector--python-latest-green)

```
Python 3.14
MySQL 8.0
mysql-connector-python
```

---

## 📁 Projectstructuur

```
Studentfeest_Project_Python/
│
├── main.py              # Startpunt van de applicatie
├── app.py               # Login-flow en sessie beheer
├── service.py           # Business logic & menu
├── repository.py        # Database CRUD-functies
├── db_connection.py     # MySQL-verbinding
├── config.py            # Configuratie (host, user, db)
│
└── SQL/
    ├── create_script_studentfeest.sql      # DDL — tabellen aanmaken
    ├── studentenfeest_testdata.sql         # Testdata
    └── studentenfeest_views_en_queries.sql # Views, triggers, stored procedures
```

---

## ⚙️ Installatie & gebruik

### 1. Repository clonen

```bash
git clone https://github.com/jouw-gebruikersnaam/Studentfeest_Project_Python.git
cd Studentfeest_Project_Python
```

### 2. Virtuele omgeving aanmaken

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac/Linux
```

### 3. Dependencies installeren

```bash
pip install mysql-connector-python
```

### 4. Database aanmaken

Open MySQL Workbench of een andere MySQL-client en voer uit in deze volgorde:

```sql
-- Stap 1: Schema + tabellen aanmaken
SOURCE create_script_studentfeest.sql;

-- Stap 2: Views, triggers en stored procedures
SOURCE studentenfeest_views_en_queries.sql;

-- Stap 3: Testdata invoegen
SOURCE studentenfeest_testdata.sql;
```

### 5. Configuratie aanpassen

Pas `config.py` aan met jouw MySQL-gegevens:

```python
HOST     = 'localhost'
USER     = 'root'
PORT     = 3306
PASSWORD = 'jouw_wachtwoord'
DATABASE = 'studentenfeest'
```

### 6. Applicatie starten

```bash
python main.py
```

---

## 🖥️ Schermopnamen

```
================================================
  🎉  STUDENTENFEEST — INLOGGEN  🎉
================================================
  Voer uw gegevens in om in te loggen.
------------------------------------------------
  👤  Student ID      : 1
  ✉️   Gebruikersnaam : jan.denvries
================================================

✅ Ingelogd! Welkom Jan!


================================================
  🎉  STUDENTENFEEST — HOOFDMENU  🎉
================================================
  Welkom, Jan Vries
------------------------------------------------
  1.  👤  Student Toevoegen
  2.  🍺  Deelname & Consumptie Registreren
  3.  📋  Bierconsumptie Rapportage Tonen
  4.  🚫  Toegangkaartje Verwijderen
  5.  🪙  Vriendenpas Verwijderen
  6.  🔄  Consumptie Updaten
  7.  🚪  Uitloggen / Afsluiten
================================================
```

---

## 🔐 SQL-features gebruikt

| Feature | Status |
|---------|--------|
| SELECT | ✅ |
| INSERT | ✅ |
| UPDATE | ✅ |
| DELETE | ✅ |
| JOIN | ✅ |
| GROUP BY | ✅ |
| VIEW (3x) | ✅ |
| Subquery | ✅ |
| LIKE | ✅ |
| REGEXP | ✅ |
| Trigger (6x) | ✅ |
| Stored Procedure (5x) | ✅ |
| Generated Column | ✅ |

---

## 🐍 Python-features gebruikt

| Feature | Gebruik |
|---------|---------|
| `while`-loop | Login-validatie, menulus |
| `for`-loop | Feestenlijst doorlopen |
| `if/elif/else` | Menu-keuzes, foutafhandeling |
| `try/except` | Database- en invoerfouten afvangen |
| `list` / `tuple` | Feest-ID's opslaan, DB-rijen verwerken |
| `def` (functies) | Service-laag + repository-laag |
| Type casting | `int(student_id)` |
| `ANSI-stijlen` | Gekleurde terminal-uitvoer |
| `bepaaldureavond()` | Dure avond detectie (kosten > €30) |

---

## 👨‍💻 Auteur

**Gökhan Öztürk**  
MakeItWork · BDA · Hogeschool van Amsterdam

---

## 📄 Licentie

Dit project is gemaakt als schoolopdracht en is niet bestemd voor commercieel gebruik.
