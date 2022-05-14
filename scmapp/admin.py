from django.contrib import admin
from .models import User,Book_ground,Admin
# Register your models here.
admin.site.register(User)
admin.site.register(Book_ground)
admin.site.register(Admin)