import pytest

from adfilteringproxy.serializers import (
  CustomerIdSerializer,
  SwaggerDocsDataFieldsInputSerializer,
)
from tests.factories.models_factory import (CustomerIdFactory)

@pytest.fixture(autouse=True)
def reset_factory_boy_sequences():
  """
  Resetting factory sequences before each test runs.
  """
  CustomerIdFactory.reset_sequence()


class TestCustomerIdSerializer:

  @pytest.mark.django_db
  def test_customer_ids_serializer(self):
    """
    Given we create a set of mocked customer ids
    When we serialize this data set with CustomerIdSerializer
    Then we expect serializer to:
      - be a valid serializer
      - to not have any serializer errors
      - and the serialized data to match the expected_serialized_data_set 
    """
    
    mocked_customer_ids = CustomerIdFactory.create_batch(5)
    mocked_customer_ids_data = []
    for customer in  mocked_customer_ids:
      mocked_customer_ids_data.append({"customer_id": customer.customer_id})

    customer_ids_serializer = CustomerIdSerializer(data=mocked_customer_ids_data, many=True)

    expected_serialized_data_set = [
      {"customer_id": "000000000000"},
      {"customer_id": "000000000001"},
      {"customer_id": "000000000002"},
      {"customer_id": "000000000003"},
      {"customer_id": "000000000004"}
    ]
    
    assert customer_ids_serializer.is_valid()
    assert customer_ids_serializer.validated_data == expected_serialized_data_set
    assert customer_ids_serializer.data == expected_serialized_data_set
    assert customer_ids_serializer.errors == []


class TestSwaggerDocsDataFieldsInputSerializer:

  @pytest.mark.django_db
  def test_swagger_docs_data_fields_input_serializer(self):
    """
    Given we a set of mocked customer data
    When we serialize this data set with SwaggerDocsDataFieldsInputSerializer
    Then we expect serializer to:
      - be a valid serializer
      - to not have any serializer errors
      - and the serialized data to match the expected_serialized_data_set 
    """
    
    mocked_customer_data = [
      {
        "customerId": "000000000001",
        "optIn": "True",
        "inactivityTimer": "750",
      },
      {
        "customerId": "000000000002",
        "optIn": "False",
        "inactivityTimer": "500",
      }
    ]

    customer_data_serializer = SwaggerDocsDataFieldsInputSerializer(data=mocked_customer_data, many=True)

    assert customer_data_serializer.is_valid()
    assert customer_data_serializer.validated_data == mocked_customer_data
    assert customer_data_serializer.data == mocked_customer_data
    assert customer_data_serializer.errors == []