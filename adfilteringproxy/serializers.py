from rest_framework import serializers

from customersdata.models.customer_ids import CustomerId
from customersdata.models.customer_details import CustomerDetails

class CustomerIdSerializer(serializers.HyperlinkedModelSerializer):
  class Meta:
    model = CustomerId
    fields = ["id", "customer_id"]
  
class SwaggerDocsDataFieldsInputSerializer(serializers.ModelSerializer):
  customerId = serializers.CharField(max_length=12)
  optIn = serializers.CharField(max_length=5)
  inactivityTimer = serializers.CharField(max_length=10)

  class Meta:
    model = CustomerDetails
    fields = ["customerId", "optIn", "inactivityTimer"]