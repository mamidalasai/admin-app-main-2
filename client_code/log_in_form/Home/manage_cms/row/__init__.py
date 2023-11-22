from ._anvil_designer import rowTemplate
from anvil import *
import anvil.server

class row(rowTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  
  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    value_to_pass = self.link_1.text
    open_form('admin.dashboard.borrowers.view_profile', value_to_pass)
