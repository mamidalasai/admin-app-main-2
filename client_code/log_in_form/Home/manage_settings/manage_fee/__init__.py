from ._anvil_designer import manage_feeTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables





class manage_fee(manage_feeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_settings')
  def collect_data_from_form(self):
      data = {
          'processing_fee': self.text_box_1.text,
          'extension_fee': self.text_box_2.text,
          'default_fee': self.text_box_3.text
          # Add more fields as needed
      }
      return data

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    processing_fee = self.text_box_1.text
    extension_fee = self.text_box_2.text
    default_fee = self.text_box_3.text

    if processing_fee == "" or extension_fee == "" or default_fee == "":
      Notification("Fill requires Details").show()
    else:
      data = self.collect_data_from_form()
      anvil.server.call('insert_data_to_database', data)
      self.text_box_1.text = self.text_box_1.focus()
      self.text_box_2.text = self.text_box_2.focus()
      self.text_box_3.text = self.text_box_3.focus()

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    open_form('log_in_form.Home.manage_settings.manage_fee.fee_edit_form')