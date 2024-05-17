## Address Book System

This is a task for practicing class-based programming. The task is to create an address book system that can store and manage contact information.

### Implementation

The system should consist of the following classes:

- **Field:** A base class for record fields.
- **Name:** A class for storing a contact's name. This field is mandatory.
- **Phone:** A class for storing a phone number. It should have validation logic to ensure the number is in the correct format (10 digits).
- **Record:** A class for storing information about a contact, including their name and a list of phone numbers.
- **AddressBook:** A class for storing and managing records.

### Functionality

- **AddressBook:**

  - Add records
  - Search records by name
  - Delete records by name

- **Record:**
  - Add phone numbers
  - Remove phone numbers
  - Edit phone numbers
  - Search for phone numbers

### Recommendations

You can start with the following basic code:

```python
from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # Implement class logic
    pass

class Phone(Field):
    # Implement class logic
    pass

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # Implement class logic

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # Implement class logic
    pass

```

Once implemented, your code should run as follows:

```python
# Create a new address book
book = AddressBook()

# Create a record for John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Add John's record to the address book
book.add_record(john_record)

# Create and add a new record for Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Print all records in the book
for name, record in book.data.items():
    print(record)

# Find and edit John's phone number
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Output: Contact name: John, phones: 1112223333; 5555555555

# Search for a specific phone number in John's record
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Output: 5555555555

# Delete Jane's record
book.delete("Jane")
```
