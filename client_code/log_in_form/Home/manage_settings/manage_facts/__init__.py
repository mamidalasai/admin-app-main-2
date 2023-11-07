from ._anvil_designer import manage_factsTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


def add_data_to_database(processing_fee, extension_fee, default_fee):
    # Replace 'your_table_name' with the actual name of your database table
    your_table = app_tables.manage_settings
    # Add a new row to the database table
    new_row = your_table.add_row(processing_fee=processing_fee, extension_fee=extension_fee, default_fee=default_fee)


class manage_facts(manage_factsTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('log_in_form.Home.manage_settings')
