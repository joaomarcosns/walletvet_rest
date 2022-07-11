# App
from users.models import User

# Framework
from rest_framework import serializers


class UserCreateSerializers(serializers.ModelSerializer):
    email_confirmation = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'name',
            'birth_date',
            'phone',
            'phone2',
            'city',
            'district',
            'street',
            'number',
            'uf',
            'email',
            'email_confirmation',
            'password',
        ]
        extra_kwargs = {
            'password': {'write_only': True},
            'email_confirmation': {'write_only': True},
        }

    def validate(self, value):
        data = self.get_initial()
        email = data.get('email')
        email_confirmation = value

        if email != email_confirmation:
            raise serializers.ValidationError(
                {"email_confirmation": "Emails must match"}, "email_confirmation_must_match")
        return value

    # def create(self, validated_data):

    #     name = validated_data['name']
    #     birth_date = validated_data['birth_date']
    #     phone =  validated_data['phone']
    #     phone2 =  validated_data['phone2']
    #     city =  validated_data['city']
    #     district =  validated_data['district']
    #     street =  validated_data['street']
    #     number =  validated_data['number']
    #     uf =  validated_data['uf']
    #     email = validated_data['email']
    #     password = validated_data['password']
    #     return User.objects.create(**validated_data)
