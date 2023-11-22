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

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.manage_products.edit_form')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.manage_products.update_form')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products')
