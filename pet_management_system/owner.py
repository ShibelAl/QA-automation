class Owner:
    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number
        self._pets = []

    @property
    def name(self):
        return self._name

    @property
    def phone_number(self):
        return self._phone_number

    def add_pet_to_owner_pets(self, pet):
        if pet.is_vaccinated:
            self._pets.append(pet)

    def remove_pet_from_owner_pets(self, pet):
        if pet in self._pets:
            self._pets.remove(pet)

    def to_dict(self):
        return {
            'name': self._name,
            'phone_number': self._phone_number,
            'pets': [pet.to_dict() for pet in self._pets]
        }

    def __str__(self):
        pet_names = list(map(lambda pet: pet.name, self._pets))
        return (f"Name: {self._name},"
                f"Phone number: {self._phone_number}"
                f"Pet's names': {pet_names}")
