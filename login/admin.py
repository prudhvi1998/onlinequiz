# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Student,Teacher,File,Answer_table

admin.site.register(Teacher)
admin.site.register(File)
admin.site.register(Student)
admin.site.register(Answer_table)