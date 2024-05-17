from collections import UserDict

class RecordNotFoundError(KeyError):
    """Exception raised when a record is not found."""
    pass

class RecordAlreadyExistsError(KeyError):
    """Exception raised when a record already exists."""
    pass

class AddressBook(UserDict):
    """A simple address address book implementation."""

    def add_record(self, record):
        """Add a record to the address book."""
        if record.name.value in self.data:
            raise RecordAlreadyExistsError(f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record

    def find(self, name):
        """Find a record by name."""
        try:
            return self.data[name]
        except KeyError:
            raise RecordNotFoundError(f"Record with name '{name}' not found.")

    def delete(self, name):
        """Delete a record by name."""
        if name not in self.data:
            raise RecordNotFoundError(f"Record with name '{name}' not found.")
        del self.data[name]