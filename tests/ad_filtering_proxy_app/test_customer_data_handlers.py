from adfilteringproxy.data_handlers.customer_data_handler import HandleCustomerData

class TestHandlingInvalidUserInput:

  def test_handling_invalid_user_input_errors_with_all_valid_values(self):
    """
    Given all values provided to handling_invalid_user_input_errors are valid values
    When we call handling_invalid_user_input_errors()
    Then we expect it to return True and None
    """

    optIn = "True"
    valid_opt_in_value = "True"
    customerId = "000000000002"
    valid_customer_id = "000000000002"
    inactivityTimer = "750"
    valid_inactivity_timer = "750"
    customer_id_in_db = True

    expected_output = True, None

    response = HandleCustomerData.handling_invalid_user_input_errors(
      optIn,
      valid_opt_in_value,
      customerId,
      valid_customer_id,
      inactivityTimer,
      valid_inactivity_timer,
      customer_id_in_db,
    )

    assert response == expected_output

  def test_handling_invalid_user_input_errors_with_invalid_opt_in_value(self):
    """
    Given an invalid optIn value is provided to handling_invalid_user_input_errors
    When we call handling_invalid_user_input_errors()
    Then we expect it to return False and an helpful error message
    """

    optIn = "banana"
    valid_opt_in_value = False
    customerId = "000000000002"
    valid_customer_id = "000000000002"
    inactivityTimer = "750"
    valid_inactivity_timer = "750"
    customer_id_in_db = True

    expected_error_message = f"optIn: <banana> is an invalid value. The value for optIn must be True or False."

    [returned_value, response] = HandleCustomerData.handling_invalid_user_input_errors(
      optIn,
      valid_opt_in_value,
      customerId,
      valid_customer_id,
      inactivityTimer,
      valid_inactivity_timer,
      customer_id_in_db,
    )

    assert returned_value == False
    assert [response.status_code, response.status_text] == [400, "Bad Request"]
    assert response.data == expected_error_message

  def test_handling_invalid_user_input_errors_with_invalid_customer_id_value(self):
    """
    Given an invalid customerId value is provided to handling_invalid_user_input_errors
    When we call handling_invalid_user_input_errors()
    Then we expect it to return False and an helpful error message
    """

    optIn = "true"
    valid_opt_in_value = "true"
    customerId = "250"
    valid_customer_id = False
    inactivityTimer = "750"
    valid_inactivity_timer = "750"
    customer_id_in_db = True

    expected_error_message = f"customerId: <250> is an invalid id, please review the id and try again. Customer ids must be exactly 12 digits and only contain integers."

    [returned_value, response] = HandleCustomerData.handling_invalid_user_input_errors(
      optIn,
      valid_opt_in_value,
      customerId,
      valid_customer_id,
      inactivityTimer,
      valid_inactivity_timer,
      customer_id_in_db,
    )

    assert returned_value == False
    assert [response.status_code, response.status_text] == [400, "Bad Request"]
    assert response.data == expected_error_message

  def test_handling_invalid_user_input_errors_with_invalid_inactivity_timer_value(self):
    """
    Given an invalid inactivityTimer value is provided to handling_invalid_user_input_errors
    When we call handling_invalid_user_input_errors()
    Then we expect it to return False and an helpful error message
    """

    optIn = "true"
    valid_opt_in_value = "true"
    customerId = "000000000003"
    valid_customer_id = "000000000003"
    inactivityTimer = "j750"
    valid_inactivity_timer = False
    customer_id_in_db = True

    expected_error_message = f"inactivityTimer: <j750> is an invalid number of seconds. Number of seconds must be a positive number and only contain integers."

    [returned_value, response] = HandleCustomerData.handling_invalid_user_input_errors(
      optIn,
      valid_opt_in_value,
      customerId,
      valid_customer_id,
      inactivityTimer,
      valid_inactivity_timer,
      customer_id_in_db,
    )

    assert returned_value == False
    assert [response.status_code, response.status_text] == [400, "Bad Request"]
    assert response.data == expected_error_message

  def test_handling_invalid_user_input_errors_when_customer_id_not_in_database(self):
    """
    Given the customer_id_in_db value provided to handling_invalid_user_input_errors is False
    When we call handling_invalid_user_input_errors()
    Then we expect it to return False and an helpful error message
    """

    optIn = "true"
    valid_opt_in_value = "true"
    customerId = "000000000003"
    valid_customer_id = "000000000003"
    inactivityTimer = "750"
    valid_inactivity_timer = "750"
    customer_id_in_db = False

    expected_error_message = f"customerId: <000000000003> is not in the database"

    [returned_value, response] = HandleCustomerData.handling_invalid_user_input_errors(
      optIn,
      valid_opt_in_value,
      customerId,
      valid_customer_id,
      inactivityTimer,
      valid_inactivity_timer,
      customer_id_in_db,
    )

    assert returned_value == False
    assert [response.status_code, response.status_text] == [404, "Not Found"]
    assert response.data == expected_error_message


class TestRequestTargetedAd:

  def test_request_targeted_ad_with_all_values_set_to_true(self):
    """
    Given all values provided to request_targeted_ad are set to True
    When we run request_targeted_ad()
    Then we expect it to return True
    """

    customer_choice = "True"
    original_ad_already_targeted = True
    customer_is_active = True
    ad_decision_system_offline = True

    response = HandleCustomerData.request_targeted_ad(
      customer_choice,
      original_ad_already_targeted,
      customer_is_active,
      ad_decision_system_offline
    )

    assert response == True

  def test_request_targeted_ad_when_customer_choice_is_false(self):
    """
    Given the customer_choice value provided to request_targeted_ad is set to False
    And all the other values are set to True
    When we run request_targeted_ad()
    Then we expect it to return False
    """

    customer_choice = "False"
    original_ad_already_targeted = True
    customer_is_active = True
    ad_decision_system_offline = True

    response = HandleCustomerData.request_targeted_ad(
      customer_choice,
      original_ad_already_targeted,
      customer_is_active,
      ad_decision_system_offline
    )

    assert response == False

  def test_request_targeted_ad_when_original_ad_already_targeted_is_false(self):
    """
    Given the original_ad_already_targeted value provided to request_targeted_ad is set to False
    And all the other values are set to True
    When we run request_targeted_ad()
    Then we expect it to return False
    """

    customer_choice = "True"
    original_ad_already_targeted = False
    customer_is_active = True
    ad_decision_system_offline = True

    response = HandleCustomerData.request_targeted_ad(
      customer_choice,
      original_ad_already_targeted,
      customer_is_active,
      ad_decision_system_offline
    )

    assert response == False

  def test_request_targeted_ad_when_customer_is_active_is_false(self):
    """
    Given the customer_is_active value provided to request_targeted_ad is set to False
    And all the other values are set to True
    When we run request_targeted_ad()
    Then we expect it to return False
    """

    customer_choice = "True"
    original_ad_already_targeted = True
    customer_is_active = False
    ad_decision_system_offline = True

    response = HandleCustomerData.request_targeted_ad(
      customer_choice,
      original_ad_already_targeted,
      customer_is_active,
      ad_decision_system_offline
    )

    assert response == False

  def test_request_targeted_ad_when_ad_decision_system_offline_is_false(self):
    """
    Given the ad_decision_system_offline value provided to request_targeted_ad is set to False
    And all the other values are set to True
    When we run request_targeted_ad()
    Then we expect it to return False
    """

    customer_choice = "True"
    original_ad_already_targeted = True
    customer_is_active = True
    ad_decision_system_offline = False

    response = HandleCustomerData.request_targeted_ad(
      customer_choice,
      original_ad_already_targeted,
      customer_is_active,
      ad_decision_system_offline
    )

    assert response == False
