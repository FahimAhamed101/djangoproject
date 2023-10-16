from django.contrib import admin
from .models import User,Userinfo,Transaction
# Register your models here.
admin.site.register(User)
admin.site.register(Userinfo)
admin.site.register(Transaction)