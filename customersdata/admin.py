from django.contrib import admin

from customersdata.models.customer_ids import CustomerId
from customersdata.models.customer_details import CustomerDetails
from customersdata.models.customer_passwords import CustomerPassword


class CustomerDetailsInLine(admin.TabularInline):
  model = CustomerDetails

class CustomerPasswordInLine(admin.TabularInline):
  model = CustomerPassword

class CustomerDetailsAdmin(admin.ModelAdmin):
  list_display = ["first_name"]

class CustomerIdAdmin(admin.ModelAdmin):
  inlines = [CustomerDetailsInLine, CustomerPasswordInLine]
  list_display = ["customer_id"]


admin.site.register(
  CustomerId,
  CustomerIdAdmin
)
admin.site.register(CustomerDetails, CustomerDetailsAdmin)
admin.site.register(CustomerPassword)