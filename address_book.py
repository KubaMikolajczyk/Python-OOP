from address import Address
from work_address import WorkAddress


class AddressBook:
    
    def __init__(self, name):
        self.name = name
        self.addresses = []

    def add_address(self, address):
        if isinstance(address, Address):
            self.addresses.append(address)
        else:
            raise TypeError

    def find(self, search_phrase):
        pass

    def sort(self):
        pass
        
    def create_from_csv(list_name, csv_path):
        pass
      
    def save_to_csv(self):
        pass