class ValidateData:
  
  def is_valid_customer_id(customerId):
    return customerId if len(customerId) == 12 and customerId.isdigit() else False

  def is_seconds_input_valid(inactivityTimer):
    return inactivityTimer if inactivityTimer.isdigit() and int(inactivityTimer) >= 0 else False

  def is_valid_opt_in(optIn):
    accepted_values = ["False", "false", "True", "true"]

    return optIn if optIn in accepted_values else False

  def is_customer_id_in_db(customer_id, customer_ids_serializer):

    for id in customer_ids_serializer.data:
      if id["customer_id"] == customer_id:
        return True
    
    return False

  def is_divisible_by_seven(customerId):
    return False if int(customerId) % 7 == 0 else True

  def is_active(inactivityTimer):
    return True if int(inactivityTimer) <= 7200 else False

  def is_divisible_by_nine(inactivityTimer):
    return False if int(inactivityTimer) % 9 == 0 else True
