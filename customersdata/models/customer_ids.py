from django.db import models

class CustomerId(models.Model):

  customer_id = models.CharField(max_length=12)

  class Meta:
    db_table = "customer_ids"