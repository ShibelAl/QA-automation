class APIHouses:
    def __init__(self, request: APIE):
        self._request = request

    def get_houses_by_id(self, id):
        self._request.get(f"https://wizard-world-api.herokuapp.com/Houses/{id}")

