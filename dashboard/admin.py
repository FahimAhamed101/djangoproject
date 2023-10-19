from django.contrib import admin
from .models import User,Userinfo,Transaction,UserProfile
# Register your models here.
admin.site.register(User)
admin.site.register(Userinfo)
admin.site.register(Transaction)
admin.site.register(UserProfile)