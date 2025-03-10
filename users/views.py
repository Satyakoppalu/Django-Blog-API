from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated




class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class LoginView(generics.GenericAPIView):
    def post(self, request):
        username=request.data.get('username')
        password=request.data.get('password')

        user=User.objects.filter(username=username).first()

        if user and user.check_password(password):
            refresh=RefreshToken.for_user(user)
            return Response(
                {
                    'access_token':str(refresh.access_token),
                    'refresh_token':str(refresh),
                }
            )
        return Response({'error':'Invalid credentials'}, status=400)
    
class LogoutView(generics.GenericAPIView):
    permissions_classes=[IsAuthenticated]

    def post(self, request):
        try:
            refresh_token=request.COOKIES.get('refresh_token')

            if not refresh_token:
                return Response({'error':'No request token found'}, status=400)
            
            token=RefreshToken(refresh_token)
            token.blacklist()

            response=Response({'message':'Succesfully logged out.'})
            response.delete_cookie('refresh_token')
            return response
        except Exception as e:
            return Response({'error':str(e)}, status=400)