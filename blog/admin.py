# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Posts, Comments, Subscribers


# Register your models here.
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Subscribers)
