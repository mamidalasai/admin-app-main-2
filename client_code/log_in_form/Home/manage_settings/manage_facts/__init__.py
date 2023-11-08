from ._anvil_designer import manage_factsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables




class manage_facts(manage_factsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_settings')
    
  def collect_data_from_form(self):
      data = {
          'no_of_visitors': self.text_box_1.text,
          'no_of_borrowers': self.text_box_2.text,
          'no_of_lenders': self.text_box_3.text,
          'lender_commitments': self.text_box_4.text,
          'amount_disbursed': self.text_box_5.text
          # Add more fields as needed
      }
      return data

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    no_of_visitors = self.text_box_1.text
    no_of_borrowers = self.text_box_2.text
    no_of_lenders = self.text_box_3.text
    lender_commitments = self.text_box_4.text
    amount_disbursed = self.text_box_5.text

    if no_of_visitors == "" or no_of_borrowers == "" or no_of_lenders == "" or lender_commitments == "" or amount_disbursed == '':
      Notification("Fill requires Details").show()
    else:
      data = self.collect_data_from_form()
      anvil.server.call('insert_data_to_database', data)
      self.text_box_1.text = self.text_box_1.focus()
      self.text_box_2.text = self.text_box_2.focus()
      self.text_box_3.text = self.text_box_3.focus()
      self.text_box_4.text = self.text_box_4.focus()
      self.text_box_5.text = self.text_box_5.focus()

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.manage_settings.manage_facts.facts_edit_form')
