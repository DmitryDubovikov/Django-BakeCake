import os
import secrets
import string

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from twilio.rest import Client


class UserManager(BaseUserManager):
    @staticmethod
    def make_random_password():
        alphabet = string.ascii_letters + string.digits
        while True:
            password = "".join(secrets.choice(alphabet) for i in range(6))
            if (
                any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3
            ):
                break
        return password

    @staticmethod
    def send_sms(phone, raw_password):
        account_sid = os.environ["TWILIO_ACCOUNT_SID"]
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        from_number = os.environ["TWILIO_PHONE_NUMBER"]
        client = Client(account_sid, auth_token)

        message = client.messages.create(
            body=f"Hello from BakeCake. Your login is {phone}, your password is {raw_password}",
            from_=from_number,
            to=phone,
        )

        print(message.sid)

    def create_user(self, phone, password=None):
        use_twilio = False

        if not phone:
            raise ValueError("Необходимо указать телефон")

        if not password:
            if use_twilio:
                raw_password = UserManager.make_random_password()
                UserManager.send_sms(phone, raw_password)
            else:
                raw_password = "123"
            password = make_password(raw_password)

        user = self.model(phone=phone)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone, password=None):
        user = self.create_user(phone, password)
        user.is_admin = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    phone = PhoneNumberField(verbose_name="Телефон", unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone"

    def __str__(self):
        return f"{self.phone}"

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin
