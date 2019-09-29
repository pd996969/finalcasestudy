from rest_framework import (status, views)
from rest_framework.response import Response
from processedorders.models import ProcessedOrder
from processedorders.serializers import ProcessedOrdersSerializer
from rest_framework import permissions
from rest_framework_simplejwt import authentication
import requests
import json
# importing the requests library



class ProcessedOrdersView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    authentication_classes = (authentication.JWTTokenUserAuthentication,)

    def get(self, request):
        processedorders = ProcessedOrder.objects.all().order_by('orderId')
        serializer = ProcessedOrdersSerializer(processedorders, many=True)
        responseData = serializer.data
        response = Response(responseData, status=status.HTTP_200_OK)

        return response

    def post(self, request):
        requestBody = request.data
        print(requestBody)
        if not(requestBody is None):
            amount=requestBody['amount']
            customer_id=requestBody['customerId']
                
            customerResponse = requests.post(url ="https://okerircn3m.execute-api.us-east-1.amazonaws.com/default/user8lambda", json = {
                                                 "customerId": customer_id})
            finalResponse=customerResponse.text
            jsonFinal=json.loads(finalResponse)
            credit= jsonFinal['credit']
        
            if(amount>credit):
                requestBody['status']="Okay.Ready to go"
                processedorderSerializer = ProcessedOrdersSerializer(data=requestBody)
                print(processedorderSerializer)
                if(processedorderSerializer.is_valid()):
                    processedorder = ProcessedOrder(**requestBody)
                    print(processedorder)
                    ProcessedOrder.save(processedorder)
                    response = Response(processedorderSerializer.data,
                                        status=status.HTTP_200_OK)                    
                else:
                    response = Response(
                        'Invalid Customer Details',
                        status=status.HTTP_400_BAD_REQUEST)
            else:
                response = Response(
                    'Error:Insufficient Amount ', status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return response
         
        

