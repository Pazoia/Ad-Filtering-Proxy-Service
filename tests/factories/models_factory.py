import factory

from factory.django import DjangoModelFactory


class CustomerIdFactory(DjangoModelFactory):

  customer_id = factory.Sequence(lambda n: "00000000000{0}".format(n))
  
  class Meta:
    model = "customersdata.CustomerId"
    django_get_or_create = ("customer_id",)
  


class CustomerDetailsFactory(DjangoModelFactory):

  first_name = ""
  last_name = ""
  email = ""
  receiving_targeted_ads = ""
  remote_last_used = ""
  customer = factory.SubFactory(CustomerIdFactory)

  class Meta:
    model = "customersdata.CustomerDetails"
    django_get_or_create = (
      "first_name",
      "last_name",
      "email",
      "receiving_targeted_ads",
      "remote_last_used",
      "customer",
    )



class CustomerPasswordFactory(DjangoModelFactory):

  customer_password = factory.Sequence(lambda n: "Password {0}".format(n))
  customer = factory.SubFactory(CustomerIdFactory)

  class Meta:
    model = "customersdata.CustomerPassword"
    django_get_or_create = ("customer_password", "customer",)
  
