from wsgiref.validate import validator
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from .models import User
from django.contrib.auth import get_user_model
from .serializer import UserSerializer


from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class ExampleView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)




class LoginView(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        print(request.user)
        return Response({'user': f'{request.user}'})
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = get_user_model().objects.filter(username=username).first()
        if user is not None:
            if user.check_password(password):
                resp = Response(status=200)
                resp.set_cookie(key="id", value=user.id, httponly=True)
                resp.data = {
                    "ok":True
                }
                # token, created = Token.objects.get_or_create(user=user)
                # return Response({'token': token.key})
                return resp
        return Response({'error': 'Parol xato'}, status=400)


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username')
        if get_user_model().objects.filter(username=username).exists():
            return Response({'error': 'User with this username already exists'}, status=400)

        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        password = request.data.get('password')
        number = request.data.get('number')

        user = get_user_model().objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        token = Token.objects.create(user=user)
        User.objects.create(
            user=user,
            phone_number=number
        )
        return Response({'token': token.key})


class GetUser(APIView):
    def get(self, request, pk):
        # id = request.data.get('id')
        user = User.objects.get(id=pk)
        ser = UserSerializer(data=user)
        if ser.is_valid():
            return Response(ser.data)
        return Response(ser.data)