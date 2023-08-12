from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, extra_fields):
        if not email:
            raise ValueError("email bo'lishi shart")
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("superuser, is_staff=True bo'lishi kerak")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("superuser, is_superuser=True bo'lishi kerak")
        return self._create_user(email, password, **extra_fields)




# class UserManager(BaseUserManager):
#     #   oddiy user
#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError("email kiritilishi shart")
#         user=self.model(
#             email=self.normalize_email(email)
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
    
#     #   super user
#     def create_superuser(self, email, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password
#         )
#         user.set_password(password)

#         user.is_admin=True
#         user.is_staff=True
#         user.is_superuser=True
#         user.save(using=self._db)
#         return user