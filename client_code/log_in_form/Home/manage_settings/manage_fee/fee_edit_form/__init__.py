from ._anvil_designer import fee_edit_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class fee_edit_form(fee_edit_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = app_tables.manage_settings.search()
  
    self.p_list = []
    self.e_list = []
    self.d_list = []
    for i in self.data:
      self.p_list.append(i['processing_fee'])
      self.e_list.append(i['extension_fee'])
      self.d_list.append(i['default_fee'])
  
    for i in self.p_list:
      if i == None:
        self.p_list.remove(i)
    for i in self.e_list:
      if i == None:
        self.e_list.remove(i)
    for i in self.d_list:
      if i == None:
        self.d_list.remove(i)
        
    self.text_box_1.text = self.p_list[-1]
    self.text_box_2.text = self.e_list[-1]
    self.text_box_3.text = self.d_list[-1]

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_settings.manage_fee')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    data = app_tables.manage_settings.search()

    p_list = []
    e_list = []
    d_list = []
    a = -1
    b = -1
    c = -1
    for i in data:
      p_list.append(i['processing_fee'])
      e_list.append(i['extension_fee'])
      d_list.append(i['default_fee'])
      a+=1
      b+=1
      c+=1

    for i in p_list:
      if i == None:
        p_list.remove(i)
        
    
    for i in e_list:
      if i == None:
        e_list.remove(i)
        
    for i in d_list:
      if i == None:
        d_list.remove(i)

    data[a]['processing_fee'] = self.text_box_1.text
    data[b]['extension_fee'] = self.text_box_2.text
    data[c]['default_fee'] = self.text_box_3.text
    print(a) 
    print(b)
    print(c)