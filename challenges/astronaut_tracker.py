import requests

def get_results():
    result = requests.get("http://api.open-notify.org/astros.json").json()
    print_results(result)


def print_results(json_data):
    print(f"people in space: {json_data.get('number')}")
    for person in json_data.get('people'):
        print(f"{person.get('name')} on the {person.get('craft')} ")


get_results()
