from rest_framework.response import Response
from rest_framework import status

class HandleCustomerData:

  def handling_invalid_user_input_errors(
    optIn,
    valid_opt_in_value,
    customerId,
    valid_customer_id,
    inactivityTimer,
    valid_inactivity_timer,
    customer_id_in_db,
  ):

    match valid_opt_in_value:
      case False:
        response = Response(
          f"optIn: <{optIn}> is an invalid value."
          " The value for optIn must be True or False.",
          status=status.HTTP_400_BAD_REQUEST
        )
        return False, response

    match valid_customer_id:
      case False:
        response = Response(
          f"customerId: <{customerId}> is an invalid id, please review the id and try again."
          " Customer ids must be exactly 12 digits and only contain integers.",
          status=status.HTTP_400_BAD_REQUEST
        )
        return False, response

    match valid_inactivity_timer:
      case False:
        response = Response(
          f"inactivityTimer: <{inactivityTimer}> is an invalid number of seconds."
          " Number of seconds must be a positive number and only contain integers.",
          status=status.HTTP_400_BAD_REQUEST
        )
        return False, response
    
    match customer_id_in_db:
      case False:
        response = Response(
          f"customerId: <{valid_customer_id}> is not in the database",
          status=status.HTTP_404_NOT_FOUND
        )
        return False, response

    return True, None

  def request_targeted_ad(
    customer_choice,
    original_ad_already_targeted,
    customer_is_active,
    ad_decision_system_offline,
  ):
    
    capitalized_customer_choice = customer_choice.capitalize()

    match capitalized_customer_choice:
      case "False":
        return False
    
    given_values = [
      original_ad_already_targeted,
      customer_is_active,
      ad_decision_system_offline,
    ]

    for value in given_values:
      match value:
        case False:
          return False
    
    return True
