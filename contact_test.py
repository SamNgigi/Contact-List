#!/usr/bin/env python
# Importing the unittest module
import unittest
# Importing Contact class
from contacts import Contact

class TestContact(unittest.TestCase):
  """
    We define the TestContact sub-class that defines our test for the
    Contact class.

    Args:
      unittest.TestCase

      We inherit the TestCase class that has its own predefined properties and method that will help in creating test cases.  
  """
  
  # Setup - Object creation/instantiation
  def setUp(self):
    """  
      Set up method to run before each test case.

      We create our contact object instance that we will use to conduct to test different aspects of our Contact class.
    """
    
    # Create an object instance new_contact of class Contact
    self.new_contact = Contact("James", "Bond", "007007007", "bond@mi6.com")

  # Testing proper instantiation of object.
  def test_proper_object_creation(self):
    """  
      test_init test case is to test if our object instance has been created properly.
    """

    self.assertEqual(self.new_contact.first_name, "James")
    self.assertEqual(self.new_contact.last_name, "Bond")
    self.assertEqual(self.new_contact.phone_number, "007007007")
    self.assertEqual(self.new_contact.email, "bond@mi6.com")

  
  # Testing saving of our object
  def test_save_contact(self):
    """  
      test_save_contact case is to test if the contact object is
      being save into the contact list that we will create.
    """

    # save_contact method which we will define in our Contact class.
    # It should basically add a Contact instance to the Contact list
    self.new_contact.save_contact()
    # We check if your contact_list length is now 1
    self.assertEqual(len(Contact.contact_list), 1);

  
  # Function that clears our array following each test.
  def tearDown(self):
    Contact.contact_list = []

  # Test saving multiple contact.
  def test_save_multiple_contacts(self):
    # Saving our setUp contact
    self.new_contact.save_contact()
    # Adding another contact
    self.added_contact = Contact("Ethan", "Hunt", "0786474", "ethan@imf.com")
    # Saving our new contact
    self.added_contact.save_contact()
    # Checking to see if the length of our array has increased.
    self.assertEqual(len(Contact.contact_list), 2)

  # Test deleting of a saved contact.
  def test_delete_contact(self):
    #Saving our setUp contact
    self.new_contact.save_contact()
    # Adding another contact
    self.added_contact = Contact("Ethan", "Hunt", "0786474", "ethan@imf.com")
    # Saving our new contact
    self.added_contact.save_contact()
    # Calling our delete_contact function
    self.new_contact.delete_contact()
    # Checking to see if the length of our array has reduced
    self.assertEqual(len(Contact.contact_list), 1)


  def test_find_contact_by_number(self):
    """ 
      Test find_contact by number method that is meant to return a
      contact when given a number.
    """
    
    self.new_contact.save_contact()
   
    self.added_contact = Contact("Ethan", "Hunt", "0786474", "ethan@imf.com")
    
    self.added_contact.save_contact()

    found_contact = Contact.find_by_number("0786474")
    """  
      Since we know that add_contact number is 0786474 with email
      ethan@imf.com, found contact method should return the same email.
    """
    self.assertEqual(found_contact.email, self.added_contact.email)





if __name__ == '__main__':
  """ 
    We are confirming that unittest.main should be run only if this
    (contact_test.py) is being run.
  """

  unittest.main()
  """ 
    Above is the method that executes all the tests.
  """