from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def signup(request):
    # start serializing the data from the request data from from api (converting from json to python object)    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        # if serializer is valid save the user to the database
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        # set and hash the password
        user.set_password(request.data['password'])
        # save user to the database
        user.save()
        return Response({"msg": "user created successfully","user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
        }},status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def protected_route(request):
    return Response({"msg": "you are able to access this route"},status=status.HTTP_200_OK)

# @api_view(['POST'])
# def login(request):
#     user = get_object_or_404(User, username=request.data['username'])
#     # checks the password 
#     if not user.check_password(request.data['password']):
#         return Response({"error": "username or password is invalid"},status=status.HTTP_400_BAD_REQUEST)
#     token, created = Token.objects.get_or_create(user=user)
#     return Response({"token": token.key,"user": UserSerializer(instance=user).data})


# @api_view(['GET'])
# @authentication_classes([SessionAuthentication, TokenAuthentication])
# @permission_classes([IsAuthenticated])
# def test_token(request):
#     return Response(f"passed! for email {request.user.email}")