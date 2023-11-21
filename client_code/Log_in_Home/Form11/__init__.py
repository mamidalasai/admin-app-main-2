from ._anvil_designer import Form11Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form11(Form11Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    

    product_id = int(self.text_box_1.text)
    product_name = self.text_box_2.text
    product_categories = self.drop_down_1.selected_value
    processing_fee = int(self.text_box_3.text)
    extension_fee = int(self.text_box_4.text)
    discount_coupons = self.radio_button_3.selected
    if discount_coupons :
      discount_coupons = self.radio_button_3.text
    else :
      discount_coupons = self.radio_button_4.text
    membership_type = self.drop_down_2.selected_value
    print(membership_type)
    interest_type = self.radio_button_1.selected
    if interest_type :
      interest_type = self.radio_button_1.text
    else :
      interest_type = self.radio_button_2.text
    min_days = int(self.drop_down_3.selected_value)
    print(min_days)
    max_days = int(self.drop_down_4.selected_value)
    print(max_days)
    roi = int(self.text_box_5.text)
    print(roi)
    

    
    anvil.server.call('product_details', product_id, product_name, product_categories, processing_fee, extension_fee, membership_type, interest_type, max_days, min_days, roi, discount_coupons)
    alert("Submitted succesfully")

  def check_box_1_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    profile_visible = self.check_box_1.checked
    if not profile_visible :
      self.text_box_1.hide_text

  

