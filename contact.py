class Contact:
  """ 
    Class that generates new instances of contacts.

    By the way PEP8 means Python Enhancement Proposal.
  """
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
