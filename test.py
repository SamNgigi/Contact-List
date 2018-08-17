# Below doesn't work in python
# import Contact from contacts
# Should be
from contacts import Contact

test = Contact("Test", "Testing", "11111", "test@mail.com");

print(test) # returns <contacts.Contact object at 0x7f0cd8845860>
print(test.phone_number) # returns 11111
# returns  My name is Test
print(f'My name is {test.first_name}') 
