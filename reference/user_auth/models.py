from django.contrib.auth.models import AbstractUser

# Create your models here.
class MyUserTable(AbstractUser):
    class Meta:
        verbose_name_plural = 'MyUserTable'