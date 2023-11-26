from ._anvil_designer import loan_managementTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class loan_management(loan_managementTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home')

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.loan_management.loan_disbursed')

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.loan_management.manual_disbursement')

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.loan_management.lost_opportunities')

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.loan_management.rejected_loans')

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.loan_management.under_process')

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.loan_management.closed_loans')

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.loan_management.lapsed')

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.loan_management.defaulters')

  def link_10_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.loan_management.npa_form')

  def link_11_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.loan_management.ots_form')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.loan_management.approved_loans')

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.loan_management.rejected_loans')

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.loan_management.under_process')

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.loan_management.open_loans')

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('log_in_form.Home.loan_management.closed_loans')
