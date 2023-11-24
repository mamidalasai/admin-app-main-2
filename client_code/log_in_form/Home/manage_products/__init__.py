from ._anvil_designer import manage_productsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class manage_products(manage_productsTemplate):
  def __init__(self,product_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products.manage_products1')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products.view_product')

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products.add_categories',get_customer_id_value,product_id)

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products.add_groups',get_customer_id_value,product_id)
    
    
    
    
