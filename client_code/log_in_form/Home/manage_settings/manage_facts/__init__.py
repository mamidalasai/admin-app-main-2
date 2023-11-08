from ._anvil_designer import manage_factsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


def add_data_to_database(no_of_visitors, no_of_borrowers, no_of_lenders, lender_commitments, amount_disbured):
    # Replace 'your_table_name' with the actual name of your database table
    your_table = app_tables.manage_settings
    # Add a new row to the database table
    new_row = your_table.add_row(no_of_visitors=no_of_visitors, no_of_borrowers=no_of_borrowers, no_of_lenders=no_of_lenders, lender_commitments=lender_commitments, amount_disbursed=amount_disbured)


class manage_facts(manage_factsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_settings')

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    no_of_visitors = self.text_box_1.text
    no_of_borrowers = self.text_box_2.text
    no_of_lenders = self.text_box_3.text
    lender_commitments = self.text_box_4.text
    amount_disbursed = self.text_box_5.text

    add_data_to_database(no_of_visitors, no_of_borrowers, no_of_lenders, lender_commitments, amount_disbursed)
    
