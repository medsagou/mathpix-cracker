import string
import os
import base64
from io import BytesIO
import random
import itertools




def check_exist_file(file_path):
    if os.path.exists(file_path):
        return True
    else:
        return False

def generate_random_string():
    letters = string.ascii_letters  # Get all uppercase and lowercase letters
    first_char = random.choice(letters)  # Choose a random letter for the first character
    rest_of_string = ''.join(random.choices(string.ascii_letters + string.digits, k=5))  # Generate 5 random characters (letters or digits)
    return first_char + rest_of_string


def generate_email_string(email):
    parts = email.split('@')
    username = parts[0]
    domain = parts[1]
    variations = []

    for i in range(1, len(username)):
        for combo in itertools.combinations(range(1, len(username)), i):
            modified_username = list(username)
            for index in combo:
                modified_username[index] = f".{modified_username[index]}"
            variations.append("".join(modified_username) + f"@{domain}")

    return variations


def remove_duplicate(source_file, file_to_remove_lines):
    with open(file_to_remove_lines, 'r') as file1:
        lines_to_remove = file1.readlines()

    with open(source_file, 'r') as file2:
        lines = file2.readlines()

    with open(source_file, 'w') as file2:
        for line in lines:
            if line not in lines_to_remove:
                file2.write(line)

def get_lines(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line

if __name__ == "__main__":
    email = "sakou81833@gmail.com"
    variations = generate_email_string(email)
    with open("../data/emails",'w') as F:
        for var in variations:
            F.write(var)
            F.write('\n')
    print(len(variations))