import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server



# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
@anvil.server.callable
def investment(initial_investment, tenure, membership_type, intrest_rate):
  app_tables.roi_table.add_row(initial_investment=initial_investment, tenure=tenure, membership_type=membership_type, intrest_rate=intrest_rate)



@anvil.server.callable
def teams(name, email, number, joining_date, role, permission):
  app_tables.admin_teams.add_row(name=name, email=email, number=number, joining_date=joining_date, role=role, permission=permission)


@anvil.server.callable
def settings(manage_name, tenure, processing_fee, extension_fee, default_fee, no_of_visitors, no_of_borrowers, no_of_lenders, lender_commitments, amount_disbursed):
  app_tables.manage_settings.add_row(manage_name=manage_name, tenure=tenure, processing_fee=processing_fee,
                                     extension_fee=extension_fee, default_fee=default_fee, no_of_visitors=no_of_visitors,
                                     no_of_borrowers=no_of_borrowers, no_of_lenders=no_of_lenders, lender_commitments=lender_commitments,
                                     amount_disbursed=amount_disbursed
                                    )



@anvil.server.callable
def insert_data_to_database(data):
    # Replace 'your_table_name' with the actual name of your database table
    your_table = app_tables.manage_settings
    new_row = your_table.add_row(**data)
  

@anvil.server.callable
def manage_product(product_id, product_name, membership_type, processing_fee, extension_fee, defaulter_fee, interest_type, max_amount, min_amount, tenure, extensions_allowed, part_payments, fore_closure):
  app_tables.manage_products.add_row(product_id=product_id,
                                     product_name=product_name,
                                     membership_type=membership_type,
                                     processing_fee=processing_fee,
                                     extension_fee=extension_fee,
                                     defaulter_fee=defaulter_fee,
                                     interest_type= interest_type, 
                                     max_amount = max_amount,
                                     min_amount = min_amount, tenure = tenure,
                                     extensions_allowed = extensions_allowed,
                                     part_payments = part_payments,
                                     fore_closure = fore_closure
                                    )

@anvil.server.callable
def lender(customer_id, email_id):
  app_tables.lender.add_row(customer_id=customer_id,
                            email_id=email_id
                           )
@anvil.server.callable
def product_details(product_id, product_name, product_categories, processing_fee, extension_fee, membership_type, interest_type, max_days, min_days, roi, discount_coupons):
  row = app_tables.product_details.add_row(product_id=product_id,
                                           product_name=product_name,
                                           product_categories = product_categories,
                                           processing_fee=processing_fee,
                                           extension_fee=extension_fee,
                                           membership_type=membership_type,
                                           interest_type= interest_type,
                                           max_days = max_days,
                                           min_days = min_days,
                                           roi = roi,
                                           discount_coupons= discount_coupons)