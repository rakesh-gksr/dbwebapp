from rest_framework.decorators import api_view
from rest_framework.response import Response
import os


@api_view()
def user_token(request):
    """

    """
    response = {'test env': os.getenv("TEST_ENV", 'test')}
    tet = {'test env': 'gdfgsdfg'}
    return Response(tet, status=200)