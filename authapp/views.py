from rest_framework.decorators import api_view
from rest_framework.response import Response
import os


@api_view()
def user_token(request):
    """
    user token
    """
    response = {'test env': os.getenv("LD_LIBRARY_PATH", 'test')}
    print("hello")
    return Response(response, status=200)