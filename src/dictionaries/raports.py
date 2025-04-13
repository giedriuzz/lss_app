"""
Raportai

Visada turi būti:
- description
- keys
"""

raport = {
    "radio_raports": {
        "salute": {
            "Pavadinimas": "SALUTE",
            "Aprašymas": "Pranešimai apie pastebėtą priešą",
        },
        "salta": {
            "description": "SALTA - išsamus kontakto raportas",
            "keys": {
                "key_1": "S - PAJĖGOS (priešo pajėgos)",
                "key_2": "A - PRIEŠO VEIKSMAI (kas atsitiko)",
                "key_3": "L - VIETA (priešo ir draugiškų pajėgų dislokacijos vieta, jei yra žinoma)",
                "key_4": "T - DATOS LAIKO GRUPĖ (DLG) (tiesioginio ar vizualaus kontakto laikas)",
                "key_5": "A - DRAUGIŠKŲ PAJĖGŲ VEIKSMAI (kas padaryta, kas ketinama daryti)",
                "additional_1": " BŪTINA PAGALBA (kokia reikalinga pagalba)",
                "additional_2": " Incidento kontrolės punkto (angl. ICP) vieta",
                "additional_3": " Saugus maršrutas iki incidento kontrolės punkto (angl. ICP)",
            },
        },
        "walta": {
            "description": "WALTA - išsamus kontakto raportas",
            "keys": {
                "key_1": "W - PAJĖGOS (kas dalyvauja)",
                "key_2": "A - PRIEŠO VEIKSMAI (Kas atsitiko)",
                "key_3": "L - VIETA (Priešo (koordinatės). Draugiškų pajėgų (nuorodos/koordinatės)",
                "key_4": "T - DATOS LAIKO GRUPĖ (DLG) (tiesioginio ar vizualaus kontakto laikas)",
                "key_5": "A - DRAUGIŠKŲ PAJĖGŲ VEIKSMAI (kas padaryta, kas ketinama daryti)",
                "additional_1": " BŪTINA PAGALBA (kokia reikalinga pagalba)",
                "additional_2": " Incidento kontrolės punkto (angl. ICP) vieta",
                "additional_3": " Saugus maršrutas iki incidento kontrolės punkto (angl. ICP)",
            },
        },
        "medevac": {"Pavadinimas": "MEDEVAC", "Aprašymas": "MEDEVAC raportas"},
        "locstat": {"Pavadinimas": "LOCSTAT", "Aprašymas": "Pranešimas apie padėtį"},
        "casevac": {
            "Pavadinimas": "CASEVAC",
            "Aprašymas": "Pranešimas apie sužeistąjį, -uosius",
        },
        "sitpra": {
            "description": "SITPRA - situacijos raportas",
            "keys": {
            "key_1": "A - DATOS LAIKO GRUPĖ (DLG)",
            "key_2": "B - Vieta (savo pajėgų)",
            "key_3": "C - Kas atsitiko",
            "key_4": "D - Kas vyksta",
            "key_5": "E - Ketinimai",
            
        },
    }
}
},
alphabet = {
    'A': "ALFA",
    'B': "BRAVO",
    'C': "CHARLIE",
    'D': "DELTA",
    'E': "ECHO",
    'F': "FOXTROT",
    'G': "GOLF",
    'H': "HOTEL",
    'I': "INDIA",
    'J': "JULIET",
    'K': "KILO",
    'L': "LIMA",
    'M': "MIKE",
    'N': "NOVEMBER",
    'O': "OSCAR",
    'P': "PAPA",
    'Q': "QUEBEC",
    'R': "ROMEO",
    'S': "SIERRA",
    'T': "TANGO",
    'U': "UNIFORM",
    'V': "VICTOR",
    'W': "WHISKEY",
    'X': "XRAY",
    'Y': "YANKEE",
    'Z': "ZULU",
}

