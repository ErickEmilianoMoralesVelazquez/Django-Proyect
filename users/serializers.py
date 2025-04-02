from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializer para obtener el token y datos del usuario al iniciar sesión
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['email'] = user.email
        # Puedes agregar más datos al token si lo deseas
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        # Agrega los datos del usuario al response
        data['user'] = {
            'id': self.user.id,
            'email': self.user.email,
            'name': self.user.name,
            'surname': self.user.surname,
        }
        return data


# Serializer del modelo CustomUser
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'name',
            'surname',
            'control_number',
            'age',
            'tel',
            'join_date'
        ]
