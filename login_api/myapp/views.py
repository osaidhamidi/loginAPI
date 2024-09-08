from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Authentication successful
            return Response({"message": "Login successful!"}, status=status.HTTP_200_OK)
        else:
            # Authentication failed
            return Response({"error": "Invalid username or password."}, status=status.HTTP_400_BAD_REQUEST)
