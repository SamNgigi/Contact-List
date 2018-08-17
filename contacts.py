# We import the pyperclip module
import pyperclip

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

  @classmethod
  def contact_exists(cls, number):
    """ 
      This function return a boolean if a number passed in matches on we have in the contact_list.
    """

    for contact in cls.contact_list:
      if contact.phone_number == number:
        return True
    return False


  @classmethod
  def display_contacts(cls):
    """  
      This function returns all the contacts we have stored in
      contact_list.
    """

    return cls.contact_list

  @classmethod
  def copy_email(cls, number):
    """ 
      This function return the contact email matching the number passed in.

      Since its functionality is pretty similar to find_by_number we
      will use the find_by_number method to return the contact then
      extract the email.
    """

    found_contact = Contact.find_by_number(number)
    pyperclip.copy(found_contact.email)
