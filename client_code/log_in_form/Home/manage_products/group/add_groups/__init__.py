from ._anvil_designer import add_groupsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from anvil import app, open_form



class add_groups(add_groupsTemplate):
  def __init__(self,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    text_data = self.text_box_1.text
    self.V= text_data


