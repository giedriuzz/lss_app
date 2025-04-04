from src.dictionaries.raports import raport


def get_value_from_dictionary(
    dictionary: dict, dictionary_key: str, dictionary_name: str
):
    select_dictionary = dictionary[dictionary_key]
    for keys, values in select_dictionary[dictionary_name].items():
        print(keys, ":", values)


if __name__ == "__main__":
    get_value_from_dictionary(raport, "radio_raports", "salta")
