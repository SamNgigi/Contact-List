class Contact:
  """ 
    Class that generates new instances of contacts.

    By the way PEP8 means Python Enhancement Proposal.
  """

  # Our empty list to store new contacts
  contact_list = []

  # Our initializing class method.
  def __init__(self, first_name, last_name, phone_number, email):
    """ 
      The __init__ method allows us to define properties for our
      object. Kinda like a constructor.

      The "self" here is a special key word here is very similar to
      the this keyword in JavaScript. It represents the actual
      object itself. 
    """
    self.first_name = first_name
    self.last_name = last_name
    self.phone_number = phone_number
    self.email = email

  def save_contact(self):
    """  
      This method saves objects into contact list by appending
      them.
    """
    Contact.contact_list.append(self)

  def delete_contact(self):
    """  
      This method deletes a saved contact from the contact list
    """
    Contact.contact_list.remove(self)

  @classmethod
  def find_by_number(cls, number):
    """  
      This method takes in a number and returns the contact with
      that number.

      Args:
        cls: 
          This allows us to access the contact_list array
        number: 
          Allows us to pass in the phone_number in order to return the contact matching the number.
    """
    for contact in cls.contact_list:
      if contact.phone_number == number:
        return contact