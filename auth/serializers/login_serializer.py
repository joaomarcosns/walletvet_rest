# Framework
from rest_framework.serializers import (
    Serializer,
    CharField,
    ValidationError
)

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

class AuthTokenSerializer(Serializer):
    """Serializer for the Authentication."""
    email = CharField(label=_("Email"), write_only=True)
    password = CharField(
        label=_("Password"), style={"input_type": "password"},
        trim_whitespace=False, write_only=True)
    token = CharField(label="Token", read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                username=email,
                password=password
            )

            if not user:
                msg = _("Unable to log in with provided credentials.")
                raise ValidationError(msg, code=_("authorization"))
            if not user.is_active:
                msg = _("Unable to log in with provided credentials.")
                raise ValidationError(msg, code=_("authorization"))
        else:
            msg = _("Must include \"username\" and \"password\".")
            raise ValidationError(msg, code=_("authorization"))

        data["user"] = user

        return data
