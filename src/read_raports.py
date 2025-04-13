from dictionaries.raports import raport


def get_value_from_dictionary(dictionary: dict, dictionary_key: str, value_name: str):
    get_dictionary_key = dictionary[dictionary_key][value_name]
    if get_dictionary_key["description"] is None:
        print("")
    else:
        print(get_dictionary_key["description"])
    for description in get_dictionary_key.get("keys"):
        print(f"{get_dictionary_key['keys'][description]}")


if __name__ == "__main__":
    get_value_from_dictionary(
        dictionary=raport, dictionary_key="radio_raports", value_name="walta"
    )
