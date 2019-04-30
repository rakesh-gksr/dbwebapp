import jwt,json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User


@api_view(['POST'])
def login(request):
    """
    Login API
    :param request:
    :return:
    """
    if not request.data:
        return Response({'Error': "Please provide username/password"}, status="400")

    username = request.data['username']
    # password = request.data['password']
    try:
        user = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response({'Error': "Invalid username/password"}, status="400")
    if user:
        payload = {'id': user.id, 'email': user.email,}
        jwt_token = {'token': jwt.encode(payload, "SECRET_KEY")}
        return Response(
          jwt_token,
          status=200,
          content_type="application/json"
        )
    else:
        return Response(
          json.dumps({'Error': "Invalid credentials"}),
          status=400,
          content_type="application/json"
        )