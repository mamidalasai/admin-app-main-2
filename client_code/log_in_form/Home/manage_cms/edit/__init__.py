from ._anvil_designer import edit_formTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class edit_form(edit_formTemplate):
  def __init__(self, get_customer_id_value, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.data = tables.app_tables.user_profile.search()
  

    self.id_list = []
    self.name_list = []
    self.status_list = []
    self.gender_list = []
    self.age_list = []
    self.dob_list = []
    self.aadhar_list = []
    self.pan_list = []
    self.city_list = []
    self.email_user_list = []
    self.last_confirm_list = []
    self.mobile_check_list = []
    self.mother_tongue_list = []
    self.mother_status_list = []
    self.date_marrige_list = []
    self.space_name_list = []
    self.about_list = []
    self.alets_list = []
    self.terms_list = []
    self.mail_id_list = []
    self.qualification_list = []
    self.address_type_list = []
    self.street_list = []
    self.build_name_list = []
    self.house_no_list = []
    self.landmark_list = []
    self.pincode_list = []
    self.state_list = []
    self.spouse_number_list = []
    self.company_name_list = []
    self.company_adress_list = []
    self.proffic_list = []
    self.user_type_list = []
    self.approve_list = []
    self.mobile_list = []
    a = -1
    for i in self.data:
      a+=1
      self.id_list.append(i['coustmer_id'])
      self.name_list.append(i['full_name'])
      self.status_list.append(i['profile_status'])
      self.gender_list.append(i['gender'])
      self.age_list.append(i['user_age'])
      self.dob_list.append(i['date_of_birth'])
      self.aadhar_list.append(i['aadhaar_no'])
      self.pan_list.append(i['pan_number'])
      self.city_list.append(i['city'])
      self.email_user_list.append(i['email_user'])
      self.last_confirm_list.append(i['last_confirm'])
      self.mobile_check_list.append(i['mobile_check'])
      self.mother_status_list.append(i['marital_status'])
      self.mother_tongue_list.append(i['mouther_tounge'])
      self.date_marrige_list.append(i['Date_mariage'])
      self.space_name_list.append(i['spouse_name'])
      self.about_list.append(i['about'])
      self.alets_list.append(i['alerts'])
      self.terms_list.append(i['terms'])
      self.mail_id_list.append(i['mail_id'])
      self.qualification_list.append(i['qualification'])
      self.address_type_list.append(i['address_type'])
      self.street_list.append(i['street'])
      self.build_name_list.append(i['building_name'])
      self.house_no_list.append(i['house_no'])
      self.landmark_list.append(i['house_landmark'])
      self.pincode_list.append(i['pincode'])
      self.state_list.append(i['state'])
      self.spouse_number_list.append(i['spouse_mobile'])
      self.company_name_list.append(i['spouse_company_name'])
      self.company_adress_list.append(i['spouse_company_address'])
      self.proffic_list.append(i['spouse_profficen'])
      self.user_type_list.append(i['usertype'])
      self.approve_list.append(i['registration_approve'])
      self.mobile_list.append(i['mobile'])

    print(self.company_adress_list)
    if get_customer_id_value in self.id_list:
      c = self.id_list.index(get_customer_id_value)
      self.text_box_2.text = self.name_list[c]
      self.text_box_3.text = bool(self.status_list[c])
      self.text_box_4.text= self.gender_list[c]
      self.text_box_5.text = self.age_list[c]
      self.date_picker_1.text = self.dob_list[c]
      self.text_box_7.text = self.mobile_list[c]
      self.text_box_8.text = self.aadhar_list[c]
      self.text_box_9.text = self.pan_list[c]
      self.text_box_10.text = self.city_list[c]
      self.text_box_12.text = bool(self.last_confirm_list[c])
      self.text_box_13.text = bool(self.mobile_check_list[c])
      self.text_box_14.text = self.mother_tongue_list[c]
      self.text_box_15.text = self.mother_status_list[c]
      self.date_picker_2.text = self.date_marrige_list[c]
      self.text_box_17.text = self.space_name_list[c]
      self.text_box_24.text = self.about_list[c]
      self.text_box_26.text = bool(self.alets_list[c])
      self.text_box_35.text = bool(self.terms_list[c])
      self.text_box_32.text = self.qualification_list[c]
      self.text_box_25.text = self.address_type_list[c]
      self.text_box_34.text = self.street_list[c]
      self.text_box_27.text = self.build_name_list[c]
      self.text_box_29.text = self.house_no_list[c]
      self.text_box_28.text = self.landmark_list[c]
      self.text_box_30.text = self.pincode_list[c]
      self.text_box_33.text = self.state_list[c]
      self.text_box_18.text = self.spouse_number_list[c]
      self.text_box_19.text = self.company_name_list[c]
      self.text_box_20.text = self.company_adress_list[c]
      self.text_box_21.text =  self.proffic_list[c]
      self.text_box_22.text = self.user_type_list[c]
      self.text_box_23.text = bool(self.approve_list[c])
    

    self.get = get_customer_id_value
  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    data = tables.app_tables.user_profile.search()

    id_list = []
    for i in self.data:
      id_list.append(i['coustmer_id'])

    if self.get in id_list:
      a = id_list.index(self.get)
      data[a]['full_name'] = self.text_box_2.text
      data[a]['profile_status'] = bool(self.text_box_3.text)
      data[a]['gender'] = self.text_box_4.text
      data[a]['user_age'] = int(self.text_box_5.text)
      data[a]['date_of_birth'] = self.date_picker_1.date
      data[a]['mobile'] = self.text_box_7.text
      data[a]['aadhaar_no'] = self.text_box_8.text
      data[a]['pan_number'] = self.text_box_9.text
      data[a]['city'] = self.text_box_10.text
      data[a]['last_confirm'] = bool(self.text_box_12.text)
      data[a]['mobile_check'] = bool(self.text_box_13.text)
      data[a]['mouther_tounge'] = self.text_box_14.text
      data[a]['marital_status'] = self.text_box_15.text
      data[a]['Date_mariage'] = self.date_picker_2.date
      data[a]['spouse_name'] = self.text_box_17.text
      data[a]['spouse_mobile'] = self.text_box_18.text
      data[a]['spouse_company_name'] = self.text_box_19.text
      data[a]['spouse_company_address'] = self.text_box_20.text
      data[a]['spouse_profficen'] = self.text_box_21.text
      data[a]['usertype'] = self.text_box_22.text
      data[a]['registration_approve'] = bool(self.text_box_23.text)
      data[a]['about'] = self.text_box_24.text
      data[a]['address_type'] = self.text_box_25.text
      data[a]['alerts'] = bool(self.text_box_26.text)
      data[a]['building_name'] = self.text_box_27.text
      data[a]['house_landmark'] = self.text_box_28.text
      data[a]['house_no'] = self.text_box_29.text
      data[a]['pincode'] = self.text_box_30.text
      data[a]['qualification'] = self.text_box_32.text
      data[a]['state'] = self.text_box_33.text
      data[a]['street'] = self.text_box_34.text
      data[a]['terms'] = bool(self.text_box_35.text)
      print(a)
    

  

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    value_to_pass = self.get
    open_form('admin.dashboard.view_profile', self.get)

  
