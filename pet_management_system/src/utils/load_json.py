import json

FILE_PATH = "./pet_database.json"


def save_data(library):
    with open(FILE_PATH, 'w') as file:
        json.dump(library.to_dict(), file)


def load_data():
    with open("../../database/data.json", 'r') as file:
        data = json.load(file)
        return data
