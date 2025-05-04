from typing import Any

from dictionaries.raports import alphabet, raport

radio_message_dictionary = []


# gauname rtaporto aprašymą pagal įvestą raporto pavadinimą
def get_raport_description_from_raport_dictionary(
    dictionary: dict[str, dict[str, Any]], dictionary_item: str
):
    try:
        description_of_raport = dictionary[dictionary_item]["description"]
        radio_message_dictionary.append(str.upper(dictionary_item))
        print(description_of_raport)
    except KeyError:
        print(f'Toks raportas "{dictionary_item}" nerastas')


def write_value_in_radio_message_dictionary(dictionary: dict, dictionary_item: str):
    # radio_message_dictionary.append(str.upper(dictionary_item))
    get_dictionary_key = dictionary[dictionary_item]
    for key in get_dictionary_key.get("keys").items():
        input_string = input(f"{key[1]} : ")
        new_key_in_message = match_alphabet_letter(key[1][0])
        radio_message_dictionary.append(f'{new_key_in_message} - "{input_string}"')


def format_radio_message(radio_message_dictionary: list):
    input_what_are_we_inviting = input("Ką kviečiame? ")
    input_who_invite = input("Kas kviečia? ")
    radio_message_dictionary.append(input_what_are_we_inviting)
    radio_message_dictionary.append(input_who_invite)


def print_radio_raport(radio_message_dictionary: list):
    print(
        f"{radio_message_dictionary[1]} aš {radio_message_dictionary[2]}, raportas {radio_message_dictionary[0]}, KLAUSAU"
    )
    print(f'"Laukite atsakymo iš {radio_message_dictionary[1]}"')
    for i in radio_message_dictionary[3:]:
        print(f"    eilė {i}")


def match_alphabet_letter(letter: str) -> str:
    for x in alphabet.items():
        if x[0] == letter:
            return x[1]
    return ""


if __name__ == "__main__":
    input_raport_name = input("Raporto pavadinimas: ")
    get_raport_description_from_raport_dictionary(
        dictionary=raport, dictionary_item=input_raport_name
    )
    format_radio_message(radio_message_dictionary)
    write_value_in_radio_message_dictionary(
        dictionary=raport,
        dictionary_item=input_raport_name,
    )

    print_radio_raport(radio_message_dictionary)
    print(radio_message_dictionary)
    print(raport["salta"]["description"])

    print(match_alphabet_letter("B"))
