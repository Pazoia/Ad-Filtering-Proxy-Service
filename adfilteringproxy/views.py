from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import views
from drf_yasg.utils import swagger_auto_schema

from adfilteringproxy.data_handlers.customer_data_handler import HandleCustomerData
from adfilteringproxy.data_handlers.data_validator import ValidateData
from adfilteringproxy.serializers import (
  SwaggerDocsDataFieldsInputSerializer,
  CustomerIdSerializer,
)

from customersdata.models.customer_ids import CustomerId

class DeliverTargetedAd(views.APIView):
  serializer_class = SwaggerDocsDataFieldsInputSerializer

  @swagger_auto_schema(method="get", query_serializer=serializer_class)
  @api_view(["GET"])
  def deliver_targeted_ad(request):

    optIn = request.query_params["optIn"]
    inactivityTimer = request.query_params["inactivityTimer"]
    customerId = request.query_params["customerId"]

    valid_opt_in_value = ValidateData.is_valid_opt_in(optIn)
    valid_customer_id = ValidateData.is_valid_customer_id(customerId)
    valid_inactivity_timer = ValidateData.is_seconds_input_valid(inactivityTimer)

    """
    Serializing customer ids from database to
    validate if customer id exist in database.
    """
    customer_ids = CustomerId.objects.all()
    customer_ids_serializer = CustomerIdSerializer(customer_ids, many=True)

    customer_id_in_db = ValidateData.is_customer_id_in_db(valid_customer_id, customer_ids_serializer)

    [validated_user_input, response] = HandleCustomerData.handling_invalid_user_input_errors(
      optIn,
      valid_opt_in_value,
      customerId,
      valid_customer_id,
      inactivityTimer,
      valid_inactivity_timer,
      customer_id_in_db,
    )

    match validated_user_input:
      case False:
        return response
      case True:

        response = {}

        CUSTOMER_CHOICE = valid_opt_in_value
        ORIGINAL_AD_ALREADY_TARGETED = ValidateData.is_divisible_by_seven(valid_customer_id)
        CUSTOMER_IS_ACTIVE = ValidateData.is_active(valid_inactivity_timer)
        AD_DECISION_SYSTEM_OFFLINE = ValidateData.is_divisible_by_nine(valid_inactivity_timer)

        match HandleCustomerData.request_targeted_ad(
          CUSTOMER_CHOICE,
          ORIGINAL_AD_ALREADY_TARGETED,
          CUSTOMER_IS_ACTIVE,
          AD_DECISION_SYSTEM_OFFLINE,
        ):
          case False:
            response["value"] = False
            return Response(response)
          case True:
            response["value"] = True
            return Response(response)
        
