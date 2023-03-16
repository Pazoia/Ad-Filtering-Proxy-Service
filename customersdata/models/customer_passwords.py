from django.db import models

from customersdata.models.customer_ids import CustomerId

class CustomerPassword(models.Model):

  customer_password = models.CharField(max_length=10)
  customer = models.OneToOneField(CustomerId, on_delete=models.CASCADE)

  class Meta:
    db_table = "customer_passwords"