from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from apps.organizations.models.Organization_Model import OrganizationModel

class UserModel(models.Model):
    user_id = models.CharField(primary_key=True)
    email = models.EmailField(unique=True)
    organization_id = models.ForeignKey(OrganizationModel, on_delete=models.SET_NULL, null=True, related_name='user')
