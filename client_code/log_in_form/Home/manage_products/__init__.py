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

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    product_id = self.text_box_1.text
    product_name = self.text_box_2.text
    membership_type = self.drop_down_4.selected_value
    processing_fee = self.text_box_4.text
    extension_fee = self.text_box_5.text
    defaulter_fee = self.text_box_6.text
    interest_type = self.drop_down_1.selected_value
    max_amount = self.text_box_7.text
    min_amount = self.text_box_8.text
    tenure = self.text_box_9.text
    extensions_allowed = self.drop_down_2.selected_value
    part_payments = self.drop_down_3.selected_value
    fore_closure = self.text_box_10.text

    
    
    
    
