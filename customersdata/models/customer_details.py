from django.db import models

from customersdata.models.customer_ids import CustomerId

class CustomerDetails(models.Model):
  
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  email = models.EmailField(max_length=150)
  receiving_targeted_ads = models.BooleanField(default=False)
  remote_last_used = models.CharField(max_length=30)
  customer = models.OneToOneField(CustomerId, on_delete=models.CASCADE)

  class Meta:
    db_table = "customer_details"