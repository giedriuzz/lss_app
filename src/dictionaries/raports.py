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
            "description": "SALTA Išsamus kontakto raportas",
            "keys": {
                "key_1": "S - PAJĖGOS (Priešo pajėgos)",
                "key_2": "A - PRIEŠO VEIKSMAI (Kas atsitiko)",
                "key_3": "L - VIETA (Priešo ir draugiškų pajėgų dislokacijos vieta, jei yra žinoma)",
                "key_4": "T - DATOS LAIKO GRUPĖ (DLG) (Tiesioginio ar vizualaus kontakto laikas)",
                "key_5": "A - DRAUGIŠKŲ PAJĖGŲ VEIKSMAI (Kas padaryta, kas ketinama daryti)",
                "additional_1": "BŪTINA PAGALBA (Kokia reikalinga pagalba)",
                "additional_2": "Incidento kontrolės punkto (angl. ICP) vieta",
                "additional_3": "Saugus maršrutas iki incidento kontrolės punkto (angl. ICP)",
            },
        },
        "walta": {
            "description": "WALTA Išsamus kontakto raportas",
            "keys": {
                "key_1": "W - PAJĖGOS (Priešo pajėgos)",
                "key_2": "A - PRIEŠO VEIKSMAI (Kas atsitiko)",
                "key_3": "L - VIETA (Priešo ir draugiškų pajėgų dislokacijos vieta, jei yra žinoma)",
                "key_4": "T - DATOS LAIKO GRUPĖ (DLG) (Tiesioginio ar vizualaus kontakto laikas)",
                "key_5": "A - DRAUGIŠKŲ PAJĖGŲ VEIKSMAI (Kas padaryta, kas ketinama daryti)",
                "additional_1": "BŪTINA PAGALBA (Kokia reikalinga pagalba)",
                "additional_2": "Incidento kontrolės punkto (angl. ICP) vieta",
                "additional_3": "Saugus maršrutas iki incidento kontrolės punkto (angl. ICP)",
            },
        },
        "medevac": {"Pavadinimas": "MEDEVAC", "Aprašymas": "MEDEVAC raportas"},
        "locstat": {"Pavadinimas": "LOCSTAT", "Aprašymas": "Pranešimas apie padėtį"},
        "casevac": {
            "Pavadinimas": "CASEVAC",
            "Aprašymas": "Pranešimas apie sužeistąjį, -uosius",
        },
        "sitpra": {
            "Pavadinimas": "SITPRA",
            "Aprašymas": "SITPRA (angl. SITREP) Situacijos raportas",
        },
    }
}

""" KA ŠAUKIAME čia KAS ŠAUKIA, raportas SALTA "Klausau"
    eilė Siera 
"""
