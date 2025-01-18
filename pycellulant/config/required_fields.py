class RequiredApiFields:
  """A class holding dictionaries of required fields
    for variety of transaction supported by pypesa.
    """
  checkout_request = {
    "msisdn",
    "account_number",
    "callback_url",
    "country_code",
    "currency_code",
    "customer_email",
    "customer_first_name",
    "customer_last_name",
    "due_date",
    "fail_redirect_url",
    "merchant_transaction_id",
    "raise_invoice",
    "request_amount",
    "request_description",
    "service_code",
    "success_redirect_url"
  }

