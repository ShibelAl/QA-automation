import random
from enum import Enum


class LogicUtils(Enum):
    FIRST_NAME = ["John", "Jane", "Alice", "Bob", "Michael", "Sarah", "David", "Emily"]
    LAST_NAME = ["Smith", "Doe", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", "Jackson"]
    CITY = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]
    STATE = ["NY", "CA", "IL", "TX", "AZ", "PA", "FL", "OH"]
    ADDRESS = ["123 Main St", "456 Elm St", "789 Maple St", "101 Oak St", "202 Pine St", "303 Cedar St"]
    ZIP_CODE = ["10001", "90001", "60601", "77001", "85001", "19101", "33101", "44101"]
    SSN = ["123-45-6789", "987-65-4321", "555-55-5555", "666-66-6666", "111-22-3333", "222-33-4444"]
    PHONE = ["555-123-4567", "555-987-6543", "555-111-2222", "555-333-4444", "555-555-6666"]
    USERNAME = ["user1", "user2", "user3", "user4", "user5", "user6", "user7", "user8"]
    PASSWORD = ["password1", "password2", "password3", "password4", "password5", "password6"]
    CONFIRM = ["password1", "password2", "password3", "password4", "password5", "password6"]


def generate_random_value(field):
    return random.choice(field.value)