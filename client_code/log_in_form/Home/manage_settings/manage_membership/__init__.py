from ._anvil_designer import manage_membershipTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables





    
class manage_membership(manage_membershipTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_settings')

  # In your Anvil client-side code for each form
  def collect_data_from_form(self):
      data = {
          'manage_name': self.drop_down_1.selected_value,
          'tenure': self.drop_down_2.selected_value
          # Add more fields as needed
      }
      return data

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    manage_name = self.drop_down_1.selected_value
    tenure = self.drop_down_2.selected_value

    data = self.collect_data_from_form()
    anvil.server.call('insert_data_to_database', data)

