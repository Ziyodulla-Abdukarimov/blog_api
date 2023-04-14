from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.exceptions import ValidationError
from datetime import datetime
from rest_framework.response import Response

from .serializers import SignUpSerializer
from .models import User, CODE_VERIFIED, INFORMATION_FILLED, DONE


class CreateUserView(CreateAPIView):
    model = User
    permission_classes = (AllowAny,)
    serializer_class = SignUpSerializer


class VerifyApiView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        user, code = request.user, request.data.get('code')
        self.check_verify(user, code)
        return Response(
            data={
                'success': True,
                'auth_status': user.auth_status,
                'access': user.tokens()['access'],
                'refresh': user.tokens()['refresh']
            }, status=200
        )

    @staticmethod
    def check_verify(user, code):
        verifies = user.verify_codes.filter(expiration_time__gte=datetime.now(), code=code, is_confirmed=False)
        if not verifies.exists():
            data = {
                'message': "Code is incorrect or expired"
            }
            raise ValidationError(data)
        verifies.update(is_confirmed=True)
        if user.auth_status not in (INFORMATION_FILLED, DONE):
            user.auth_status = CODE_VERIFIED
            user.save()
        return True
