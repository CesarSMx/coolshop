import uuid #this module is used to create uniques ID

class Client:

    def __init__(self, first_name, last_name, email, phone_number, uid=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number 
        self.uid = uid or uuid.uuid4()

    def to_dict(self):
        #Return a dict representation of our object. See __dict__.
        return vars(self)  

    @staticmethod 
    def schema():
        #The decorator @staticmethod is used to declare a method that
        #can be executed without a declared instance the class.
        #In this case, schema() will return a list with the schema of how
        #our program write and read the csv file (or database)
        return ['uid', 'first_name', 'last_name', 'email', 'phone_number']
