# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import Users

class Friends(models.Model):
    user = models.ForeignKey(Users, related_name = "creator")
    friend = models.ForeignKey(Users, related_name = "friends")
    block = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)