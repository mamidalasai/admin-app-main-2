from ._anvil_designer import facts_edit_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class facts_edit_form(facts_edit_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = app_tables.manage_settings.search()
  
    self.v_list = []
    self.b_list = []
    self.l_list = []
    self.c_list = []
    self.a_list = []
    for i in self.data:
      self.v_list.append(i['no_of_visitors'])
      self.b_list.append(i['no_of_borrowers'])
      self.l_list.append(i['no_of_lenders'])
      self.c_list.append(i['lender_commitments'])
      self.a_list.append(i['amount_disbursed'])
  
    for i in self.v_list:
      if i == None:
        self.v_list.remove(i)
    for i in self.b_list:
      if i == None:
        self.b_list.remove(i)
    for i in self.l_list:
      if i == None:
        self.l_list.remove(i)
    for i in self.c_list:
      if i == None:
        self.c_list.remove(i)
    for i in self.a_list:
      if i == None:
        self.a_list.remove(i)
        
    self.text_box_1.text = self.v_list[-1]
    self.text_box_2.text = self.b_list[-1]
    self.text_box_3.text = self.l_list[-1]
    self.text_box_4.text = self.c_list[-1]
    self.text_box_5.text = self.a_list[-1]
    

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_settings.manage_facts')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    data = app_tables.manage_settings.search()
    a = -1
    b = -1
    c = -1
    d = -1
    e = -1
    for i in data:
      a+=1
      b+=1
      c+=1
      d+=1
      e+=1

    data[a]['no_of_visitors'] = self.text_box_1.text
    data[b]['no_of_borrowers'] = self.text_box_2.text
    data[c]['no_of_lenders'] = self.text_box_3.text
    data[d]['lender_commitments'] = self.text_box_4.text
    data[e]['amount_disbursed'] = self.text_box_5.text

