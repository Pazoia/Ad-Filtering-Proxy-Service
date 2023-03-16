import pytest

from tests.factories.models_factory import (
  CustomerIdFactory,
  CustomerDetailsFactory,
  CustomerPasswordFactory,
)

@pytest.fixture(autouse=True)
def reset_factory_boy_sequences():
  """
  Resetting factory sequences before each test runs.
  """
  CustomerIdFactory.reset_sequence()
  CustomerPasswordFactory.reset_sequence()


class TestCustomerId:
  @pytest.mark.django_db
  def test_customer_id_model(self):
    """
    Given a customer_ids model
    When we add data to it via a model factory
    Then we expect the database to be populated with the given data
    """

    mocked_customer_ids = CustomerIdFactory.create_batch(5)

    [customer1, customer2, customer3, customer4, customer5] = mocked_customer_ids

    assert len(mocked_customer_ids) == 5
    assert customer1.customer_id == "000000000000"
    assert customer2.customer_id == "000000000001"
    assert customer3.customer_id == "000000000002"
    assert customer4.customer_id == "000000000003"
    assert customer5.customer_id == "000000000004"


class TestCustomerDetails:
  @pytest.mark.django_db
  def test_customer_details_model(self):
    """
    Given a customer_details model
    When we add data to it via a model factory
    Then we expect the database to be populated with the given data
    """

    mocked_customer_details = CustomerDetailsFactory.create(
      first_name = "Santa",
      last_name = "Claus",
      email = "santa.claus@lapland.com",
      receiving_targeted_ads = "True",
      remote_last_used = "2022-12-01 15:30:00",
    )

    assert mocked_customer_details.first_name == "Santa"
    assert mocked_customer_details.last_name == "Claus"
    assert mocked_customer_details.email == "santa.claus@lapland.com"
    assert mocked_customer_details.receiving_targeted_ads == "True"
    assert mocked_customer_details.remote_last_used == "2022-12-01 15:30:00"


class TestCustomerPassword:
  @pytest.mark.django_db
  def test_customer_password_model(self):
    """
    Given a customer_passwords model
    When we add data to it via a model factory
    Then we expect the database to be populated with the given data
    """

    mocked_customer_passwords = CustomerPasswordFactory.create_batch(5)

    [customer1, customer2, customer3, customer4, customer5] = mocked_customer_passwords

    assert len(mocked_customer_passwords) == 5
    assert customer1.customer_password == "Password 0"
    assert customer2.customer_password == "Password 1"
    assert customer3.customer_password == "Password 2"
    assert customer4.customer_password == "Password 3"
    assert customer5.customer_password == "Password 4"


