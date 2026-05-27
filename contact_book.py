# Contact book program

contacts = [
    {"name": "Aditi", "phone": "11111", "email": "a@gmail.com"},
    {"name": "Rahul", "phone": "22222", "email": "r@gmail.com"},
    {"name": "Neha", "phone": "33333", "email": "n@gmail.com"}
]

def find_contact(name):

    for contact in contacts:

        if contact["name"].lower() == name.lower():
            return contact

    return "Contact not found"

search = input("Enter name: ")

print(find_contact(search))