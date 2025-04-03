

import json




    
def open_json_file(file_path):
    """Open a JSON file and return its contents."""
    with open(file_path, 'r') as file:
        #data = json.load(file)
        parser = json.load(file)
        #return data
        for item in parser:
            print(item)

if __name__ == '__main__':
    open_json_file('/home/giedrius/venv/lss_app/src/raports/salute.json')
    