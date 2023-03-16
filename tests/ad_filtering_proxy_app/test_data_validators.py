import pytest

from adfilteringproxy.data_handlers.data_validator import ValidateData
from adfilteringproxy.serializers import CustomerIdSerializer
from tests.factories.models_factory import CustomerIdFactory


class TestCustomerIdValidation:

  @pytest.mark.django_db
  def serialize_customer_ids_data(self):
    """
    Creating and serializing a set of mocked_customer_ids
    """

    # Resetting CustomerIdFactory sequence before test
    CustomerIdFactory.reset_sequence()
    
    mocked_customer_ids = CustomerIdFactory.create_batch(5)
    mocked_customer_ids_data = []
    for customer in  mocked_customer_ids:
      mocked_customer_ids_data.append({"customer_id": customer.customer_id})

    customer_ids_serializer = CustomerIdSerializer(data=mocked_customer_ids_data, many=True)

    assert customer_ids_serializer.is_valid()

    return customer_ids_serializer

  def test_is_valid_customer_id_with_valid_customer_id(self):
    """
    Given a valid customerId
    When we run it through is_valid_customer_id()
    Then we expect to return the customerId value
    """

    customer_id = "000000000002"
    expected_output = "000000000002"

    validation_result = ValidateData.is_valid_customer_id(customer_id)

    assert validation_result == expected_output
  
  @pytest.mark.parametrize(
    "customer_id, expected_output",
    [("500", False), ("a00000000002", False), ("a500", False)]
  )
  def test_is_valid_customer_id_with_invalid_customer_id(self, customer_id, expected_output):
    """
    Given an invalid customerId
      (too short, includes other chars than integers or both)
    When we run it through is_valid_customer_id()
    Then we expect to return False
    """

    validation_result = ValidateData.is_valid_customer_id(customer_id)

    assert validation_result == expected_output

  @pytest.mark.django_db
  def test_is_customer_id_in_db_when_true(self):
    """
    Given a valid customerId and a serialized set of customer ids
    When the customerId is present in the data set provided
    Then we expect to return True
    """

    customer_ids_serializer = self.serialize_customer_ids_data()

    customer_id = "000000000002"
    expected_output = True

    validation_result = ValidateData.is_customer_id_in_db(customer_id, customer_ids_serializer)

    assert validation_result == expected_output

  @pytest.mark.django_db
  def test_is_customer_id_in_db_when_false(self):
    """
    Given a valid customerId and a serialized set of customer ids
    When the customerId is not present in the data set provided
    Then we expect to return False
    """

    customer_ids_serializer = self.serialize_customer_ids_data()

    customer_id = "000000000009"
    expected_output = False

    validation_result = ValidateData.is_customer_id_in_db(customer_id, customer_ids_serializer)

    assert validation_result == expected_output

  def test_is_divisible_by_seven_when_customer_id_is_divisible_by_seven(self):
    """
    Given a valid customerId
    When the customerId is exactly divisible by seven
    Then we expect to return False
    """

    customer_id = "000000000014"
    expected_output = False

    validation_result = ValidateData.is_divisible_by_seven(customer_id)

    assert validation_result == expected_output

  def test_is_divisible_by_seven_when_customer_id_is_not_divisible_by_seven(self):
    """
    Given a valid customerId
    When the customerId is not exactly divisible by seven
    Then we expect to return True
    """

    customer_id = "000000000005"
    expected_output = True

    validation_result = ValidateData.is_divisible_by_seven(customer_id)

    assert validation_result == expected_output


class TestInactivityTimerValidation:

  def test_is_seconds_input_valid_with_valid_inactivity_timer(self):
    """
    Given a valid inactivityTimer input
    When we run it through is_seconds_input_valid()
    Then we expect to return the inactivityTimer value
    """

    inactivity_timer = "750"
    expected_output = "750"

    validation_result = ValidateData.is_seconds_input_valid(inactivity_timer)

    assert validation_result == expected_output

  @pytest.mark.parametrize(
    "inactivity_timer, expected_output",
    [("y750", False), ("-25", False), ("-25f", False)]
  )
  def test_is_seconds_input_valid_with_invalid_inactivity_timer(self, inactivity_timer, expected_output):
    """
    Given an invalid inactivityTimer input 
      (includes other chars than integers, given a negative value or both)
    When we run it through is_seconds_input_valid()
    Then we expect to return False
    """

    validation_result = ValidateData.is_seconds_input_valid(inactivity_timer)

    assert validation_result == expected_output
  
  @pytest.mark.parametrize(
    "inactivity_timer, expected_output",
    [("750", True), ("7200", True)]
  )
  def test_is_active_when_inactivity_timer_is_lesser_or_equals_to_two_hours(self, inactivity_timer, expected_output):
    """
    Given a valid inactivityTimer input
    When the inactivityTimer value is lesser or equals to 7200 seconds (2 hours)
    Then we expect to return True
    """

    validation_result = ValidateData.is_active(inactivity_timer)

    assert validation_result == expected_output

  def test_is_active_when_inactivity_timer_is_greater_than_two_hours(self):
    """
    Given a valid inactivityTimer input
    When the inactivityTimer value is greater than 7200 seconds (2 hours)
    Then we expect to return False
    """

    inactivity_timer = "7500"
    expected_output = False

    validation_result = ValidateData.is_active(inactivity_timer)

    assert validation_result == expected_output

  def test_is_divisible_by_nine_when_inactivity_timer_is_divisible_by_nine(self):
    """
    Given a valid inactivityTimer input
    When the inactivityTimer is exactly divisible by nine
    Then we expect to return False
    """

    inactivity_timer = "18"
    expected_output = False

    validation_result = ValidateData.is_divisible_by_nine(inactivity_timer)

    assert validation_result == expected_output

  def test_is_divisible_by_nine_when_inactivity_timer_is_not_divisible_by_nine(self):
    """
    Given a valid inactivityTimer input
    When the inactivityTimer is not exactly divisible by nine
    Then we expect to return True
    """

    inactivity_timer = "20"
    expected_output = True

    validation_result = ValidateData.is_divisible_by_nine(inactivity_timer)

    assert validation_result == expected_output


class TestOptInValidation:

  @pytest.mark.parametrize(
    "opt_in, expected_output",
    [("False", "False"), ("false", "false"), ("True", "True"), ("true", "true")]
  )
  def test_is_valid_opt_in_with_valid_optIn_value(self, opt_in, expected_output):
    """
    Given a valid optIn value
    When we run it through is_valid_opt_in()
    Then we expect to return the optIn value
    """

    validation_result = ValidateData.is_valid_opt_in(opt_in)

    assert validation_result == expected_output

  def test_is_valid_opt_in_with_invalid_optIn_value(self):
    """
    Given an invalid optIn value
    When we run it through is_valid_opt_in()
    Then we expect to return False
    """

    opt_in = "not a boolean"
    expected_output = False

    validation_result = ValidateData.is_valid_opt_in(opt_in)

    assert validation_result == expected_output
  