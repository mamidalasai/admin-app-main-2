from ._anvil_designer import add_groupsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class add_groups(add_groupsTemplate):
  def __init__(self,**properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.



  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products.view_product')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.manage_products.manage_products1')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""     
    get_customer_id_value = self.drop_down_1.selected_value
    open_form('log_in_form.Home.manage_products.add_categories',get_customer_id_value)



