from django.db import models
from django.contrib.auth.models import User


class ProxyUser(User):

    class Meta:
        proxy = True
