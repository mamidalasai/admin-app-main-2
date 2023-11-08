from ._anvil_designer import manage_productsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class manage_products(manage_productsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home')

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""

  def text_box_2_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""

  def text_box_3_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""

  def text_box_4_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    
    
    
    
    
