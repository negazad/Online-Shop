from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, user_name, first_name, last_name, age, password):
        if not phone_number:
            raise ValueError('user must have a phone number')

        if not email:
            raise ValueError('user must have an email')

        if not user_name:
            raise ValueError('user must have an user name')

        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            user_name=user_name,
            first_name=first_name,
            last_name=last_name,
            age=age
        )
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, email, user_name, first_name, last_name, age, password):
        user = self.create_user(phone_number, email, user_name, first_name, last_name, age, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
