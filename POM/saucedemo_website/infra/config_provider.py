import json


# class ConfigProvider:
#
#     @staticmethod
#     def load_from_file(filename):
#         try:
#             with open('config.json', 'r') as f:
#                 return json.load(f)
#         except FileNotFoundError:
#             print(f"File {filename} not found. Starting with an empty library.")

import json
import os


class ConfigProvider:

    @staticmethod
    def load_from_file(filename):
        if not os.path.isabs(filename):
            # Convert relative path to absolute path
            current_dir = os.path.dirname(os.path.abspath(__file__))
            filename = os.path.join(current_dir, filename)
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File {filename} not found. Starting with an empty configuration.")
            return {}
        except json.JSONDecodeError:
            print(f"File {filename} is not a valid JSON file. Starting with an empty configuration.")
            return {}
