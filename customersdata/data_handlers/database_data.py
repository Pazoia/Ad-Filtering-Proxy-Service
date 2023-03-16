from customersdata.models import (
  CustomerId,
  CustomerDetails,
  CustomerPassword,
)

class HandleDatabaseData:
  def save_data_to_db(customers_data):
    for customer in customers_data:
      CustomerId.objects.create(
        customer_id=customer["customer_id"],
      )

      customer_id_row = CustomerId.objects.get(customer_id=customer["customer_id"])

      CustomerDetails.objects.create(
        first_name=customer["first_name"],
        last_name=customer["last_name"],
        email=customer["email"],
        receiving_targeted_ads=customer["receiving_targeted_ads"],
        remote_last_used=customer["remote_last_used"],
        customer_id=customer_id_row.id,
      )

      CustomerPassword.objects.create(
        customer_password=customer["customer_password"],
        customer_id=customer_id_row.id,
      )
      