from dictionaries.raports import raport
from dictionaries.raports import alphabet

raport_dictionary = []
raport_dictionary_test = ['S1 aš G2', 'SITPRA','A - 1204C25', 'B - 12345678', 'C - pastebetas priešas', 'D - priešas juda link šiaurės', 'E - stebėsime toliau']

def get_value_from_dictionary(dictionary: dict, dictionary_key: str, value_name: str):
    raport_dictionary.append(str.upper(value_name))
    get_dictionary_key = dictionary[dictionary_key][value_name]
    if get_dictionary_key["description"] is None:
        print("")
    else:
        print(get_dictionary_key["description"])
    for description in get_dictionary_key.get("keys"):
       input_string = input(f"- {get_dictionary_key['keys'][description]} : ")
       raport_dictionary.append(f'{get_dictionary_key["keys"][description][0]} - {input_string}')

def get_raport_description(dictionary: dict, dictionary_key: str, value_name: str):
    get_dictionary_key = dictionary[dictionary_key][value_name]
    if get_dictionary_key["description"] is None:
        print("")
    else:
        print(get_dictionary_key["description"])  
    
def format_raport(raport_dictionary: list):
    print (f'{raport_dictionary[0]}, {raport_dictionary[1]}, KLAUSAU')
    for i in raport_dictionary[2:]:
        print(f'    eilė {i}')
        
def format_radio_message(raport_dictionary: list):
    input_what_are_we_inviting = input("Ką kviečiame? ")
    input_who_invite = input("Kas kviečia? ")
    raport_dictionary.append(f"{input_what_are_we_inviting} aš {input_who_invite}")
    


if __name__ == "__main__":
    input_raport_name = input("Koks raportas? ")
    get_raport_description(dictionary=raport, dictionary_key="radio_raports", value_name=input_raport_name)
    format_radio_message(raport_dictionary)
    get_value_from_dictionary(
        dictionary=raport, dictionary_key="radio_raports", value_name=input_raport_name
    )

    format_raport(raport_dictionary)
    
