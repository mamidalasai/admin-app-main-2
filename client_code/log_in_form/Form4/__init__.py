from ._anvil_designer import Form4Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form4(Form4Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.customer_id= []
    self.email_id = []
    self.full_name = []
    self.interest_rate = []
    self.loan_id = []
    self.loan_status = []
    self.max_amount = []
    self.min_amount = []
    self.tenure = []
    self.total_repayment = [properties]
    
    data = tables.app_tables.loan_details.search()
    for row in data:
      self.customer_id.append(row['customer_id'])
      self.email_id.append(row['email_id'])
      self.full_name.append(row['full_name'])
      self.interest_rate.append(row['interest_rate'])
      self.loan_id.append(row['loan_id'])
      self.loan_status.append(row['loan_status'])
      self.max_amount.append(row['max_amount'])
      self.min_amount.append(row['min_amount'])
      self.tenure.append(row['tenure'])
      self.total_repayment.append(row['total_repayment'])
      
    
    self.label_3.text = self.user_id[-1]
    self.label_5.text = self.name[-1]
    self.label_7.text = self.password[-1]
    self.label_9.text = self.mobile_no[-1]
    self.label_11.text = self.mail_id[-1]
    self.label_13.text = self.pincode[-1]
    self.label_3.text = self.user_id[-1]
    self.label_3.text = self.user_id[-1]
    self.label_3.text = self.user_id[-1]
    self.label_3.text = self.user_id[-1]
    print(self.pincode)
