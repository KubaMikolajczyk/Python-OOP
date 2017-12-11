class Address:

    def __init__(self, person, city, street, house_no):
        self.person = person
        self.city = city
        self.street = street
        self.house_no = house_no

    def get_full_address(self):
        return "{}, {}, {} {}".format(self.person, self.city, self.street, self.house_no)

    def __repr__(self):
        return self.get_full_address()
    
    def __eq__(self, other):
        return self.person == other.person \
               and self.city == other.city \
               and self.street == other.street \
               and self.house_no == other.house_no
