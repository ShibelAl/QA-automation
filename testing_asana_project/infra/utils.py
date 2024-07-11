import random
import string


class Utils:

    @staticmethod
    def generate_random_string(length=10):
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

