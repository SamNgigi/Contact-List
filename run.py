#!/usr/bin/env python
# Importing our Contact class
from contacts import Contact
import pyperclip

def create(first_name, last_name, phone_number, email_address):
  """  
    Function to create new contact
  """

  new_contact = Contact(first_name, last_name, phone_number, email_address)
  return new_contact

def save(contact):
  """  
    Function to save new contact.
  """

  contact.save_contact()

def delete(contact):
  """  
    Function to delete a contact
  """

  contact.delete_contact()

def find(number):
  """  
    Function that find a contact by number and returns the contact
  """
  return Contact.find_by_number(number)

def exists(number):
  """  
    Returns a boolean depending on if number has matching contact.
  """
  return Contact.contact_exists(number)

def display():
  """  
    Returns a list of all the save contacts
  """
  return Contact.display_contacts()

def copy(number):
  """  
    Returns copied contact email address based on matching number.
  """
  return Contact.copy_email(number)

# Defining our main application
def main():
  print("Hello! Welcome to your contact list. What is your name?")
  username = input()

  print(f"Hello {username}! What would you like to do?")

  while True:
    print("""  
      Use these short codes:

      nc - create a new contact
      dc - display contacts
      fc - find contact
      rc - remove contact
      cc - copy contact
      ex - exit the contact list
    """)
    short_code = input().lower()

    if short_code == 'nc':
      print("New Contact")
      print("*"*10)

      print("First Name - ")
      first_name = input()

      print("Last Name - ")
      last_name = input()

      print("Phone number - ")
      phone_number = input()

      print("Email address - ")
      email_address = input()

      # Saving our created contact
      save(create(first_name, last_name, phone_number, email_address))

      print('\n')
      print(f"New Contact {first_name} {last_name} created")
      print('\n')

    elif short_code == 'dc':
      if display():
        print("Here is a list of all your contacts.")
        print("\n")

        for contact in display():
          """  
            Note that we have to say contact.email and note
            email_address here because the display method is
            fetching straight using the class definition of email.
          """
          print(f"""
          {contact.first_name} 
          {contact.last_name}
          {contact.phone_number}
          {contact.email}
          """)
      else:
        print("You don't seem to have any contacts saved yet.")

    elif short_code == 'fc':
      print("Enter number you want to search for")
      search_number = input()

      if exists(search_number):
        search_contact = find(search_number)

        print(f"{search_contact.first_name} {search_contact.last_name}")

        print("*"*20)


        print(f"Phone number - {search_contact.phone_number}")
        print(f"Email address - {search_contact.email}")
      else:
        print("This contact does not exists")

    elif short_code == 'rc':
      if display():
        print(f'Are you sure you want to delete {display()[0].first_name}? y/N')
        y_n = input().lower()
        if y_n == 'y':
          delete(display()[0])
      else:
        print("Nothing to delete")
    
    elif short_code == 'cc':
      print("What is the contact number for the email you want to copy")
      number = input()
      if exists(number):
        copy(number)
        print(f"{pyperclip.paste()} found")
      else:
        print("Number does not exist")

    elif short_code == "ex":
      print("Asta Lavista")
      break
    else:
      print("I really didn't get that. Please use the short codes.")

if __name__ == '__main__':

  main()