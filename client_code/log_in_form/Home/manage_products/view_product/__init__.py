from ._anvil_designer import view_productTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class view_product(view_productTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

        self.data = tables.app_tables.user_profile.search()

    a = -1
    self.list_1 = []
    self.list_2 = []
    self.list_3 = []
    self.list_4 = []
    self.list_5 = []

    for i in self.data:
      a+=1
      self.list_1.append(i['product_id'])
      self.list_2.append(i['product_name'])
      self.list_3.append(i[''])
      self.list_4.append(i['gender'])
      self.list_5.append(i['user_age'])

    print(a)

    self.result = []
    if a == -1:
      alert("No Data Available Here!")
    else:
      for i in range(a+1):
        print(self.list_2[i])
        self.result.append({'coustmer_id' : self.list_1[i], 'full_name' : self.list_2[i], 'profile_status' : self.list_3[i], 'gender' : self.list_4[i], 'user_age' : self.list_5[i],
                          'date_of_birth' : self.list_6[i], 'mobile' : self.list_7[i], 'aadhaar_no' : self.list_8[i]})

      self.repeating_panel_1.items = self.result

      print(self.list_1, self.list_2, self.list_3)
      print(self.result)
      print(a)


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.manage_products.edit_form')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.manage_products.update_form')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products')
