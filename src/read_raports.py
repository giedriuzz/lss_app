from dictionaries.raports import raport
from dictionaries.raports import alphabet

radio_message_dictionary = []
radio_message_dictionary_test = ['S1 aš G2', 'SITPRA','A - 1204C25', 'B - 12345678', 'C - pastebetas priešas', 'D - priešas juda link šiaurės', 'E - stebėsime toliau']

def write_value_in_radio_message_dictionary(dictionary: dict, dictionary_key: str, value_name: str):
    radio_message_dictionary.append(str.upper(value_name))
    get_dictionary_key = dictionary[0][dictionary_key][value_name]
    if get_dictionary_key["description"] is None:
        print("")
    else:
        print(get_dictionary_key["description"])
    for description in get_dictionary_key.get("keys"):
       input_string = input(f"- {get_dictionary_key['keys'][description]} : ")
       radio_message_dictionary.append(f'{get_dictionary_key["keys"][description][0]} - {input_string}')

def get_raport_description_from_radio_message_dictionary(dictionary: dict, dictionary_key: str, value_name: str):
    get_dictionary_key = dictionary[0][dictionary_key][value_name]
    if get_dictionary_key["description"] is None:
        print("")
    else:
        print(get_dictionary_key["description"])  
    
def format_raport(radio_message_dictionary: list):
    print (f'{radio_message_dictionary[0]}, {radio_message_dictionary[1]}, KLAUSAU')
    for i in radio_message_dictionary[2:]:
        print(f'    eilė {i}')
        
def format_radio_message(radio_message_dictionary: list):
    input_what_are_we_inviting = input("Ką kviečiame? ")
    input_who_invite = input("Kas kviečia? ")
    radio_message_dictionary.append(f"{input_what_are_we_inviting} aš {input_who_invite}")
    


if __name__ == "__main__":
    """ input_raport_name = input("Koks raportas? ")
    get_raport_description_from_radio_message_dictionary(dictionary=raport, dictionary_key="radio_raports", value_name=input_raport_name)
    format_radio_message(radio_message_dictionary)
    write_value_in_radio_message_dictionary(
        dictionary=raport, dictionary_key="radio_raports", value_name=input_raport_name
    )

    format_raport(radio_message_dictionary) """
    for i in alphabet:
        print(f'{i} - {alphabet[i]}')
    
   
    
