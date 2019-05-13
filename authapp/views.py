from rest_framework.decorators import api_view
from rest_framework.response import Response
import os
from authlib import Requests_Holder


@api_view(['POST'])
def user_token(request):
    """
    user token
    """
    response = {'testenv': os.getenv("LD_LIBRARY_PATH", 'test'), 'ORACLE_HOME': os.getenv("ORACLE_HOME", 'test')}
    return Response(response, status=200)

@api_view()
def test_api(request):
    request_obj = Requests_Holder()
    response = request_obj.auth_obj.verify_token("Token")
    print("hello")
    print(response)
    # response = {'response': response, }
    return Response(response, status=200)

