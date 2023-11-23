from ._anvil_designer import edit_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class edit_form(edit_formTemplate):
  def __init__(self, get_customer_id_value, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.product_details.search()
  

    self.id_list = []
    self.name_list = []
    self.categories_list = []
    self.proce_list = []
    self.extension_list = []
    self.mtype_list = []
    self.intype_list = []
    self.max_list = []
    self.min_list = []
    self.roi_list = []
    self.disco_list = []
   
    a = -1
    for i in self.data:
      a+=1
      self.id_list.append(i['product_id'])
      self.name_list.append(i['product_name'])
      self.categories_list.append(i['product_categories'])
      self.proce_list.append(i['processing_fee'])
      self.extension_list.append(i['extension_fee'])
      self.mtype_list.append(i['membership_type'])
      self.intype_list.append(i['interest_type'])
      self.max_list.append(i['max_days'])
      self.min_list.append(i['min_days'])
      self.roi_list.append(i['roi'])
      self.disco_list.append(i['discount_coupons'])

    if get_customer_id_value in self.id_list:
      c = self.id_list.index(get_customer_id_value)
      self.label_1.text = self.id_list[c]
      self.text_box_2.text = self.name_list[c]
      self.drop_down_1.selected_value = self.categories_list[c]
      self.text_box_3.text = self.proce_list[c]
      self.text_box_4.text = self.extension_list[c]
      self.drop_down_2.selected_value = self.mtype_list[c]
      self.radio_button_1.text = self.intype_list[c]
      self.drop_down_3.text = self.max_list[c]
      self.drop_down_4.text = self.min_list[c]
      self.text_box_5.text = self.roi_list[c]
      self.radio_button_3.text = self.disco_list[c]


    self.get = get_customer_id_value


  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    data = tables.app_tables.product_details.search()

    id_list = []
    for i in self.data:
      id_list.append(i['product_id'])

    if self.get in id_list:
      a = id_list.index(self.get)
      data[a]['product_name'] = self.text_box_2.text
      data[a]['product_categories'] = self.drop_down_1.selected_value 
      data[a]['processing_fee'] =  int(self.text_box_3.text)
      data[a]['extension_fee'] = int(self.text_box_4.text)
      data[a]['membership_type'] = self.drop_down_2.selected_value
      data[a]['interest_type'] = self.radio_button_1.text 
      data[a]['max_days'] = int(self.drop_down_3.text)
      data[a]['min_days'] = int(self.drop_down_4.text) 
      data[a]['roi'] = int(self.text_box_5.text)
      data[a]['discount_coupons'] = self.radio_button_3.text
    
      print(a)
      open_form('log_in_form.Home.manage_products.view_product.view_profile')

  def link_1_copy_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_products.view_product.view_profile')
