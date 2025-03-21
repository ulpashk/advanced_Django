from django.contrib import admin

# Register your models here.
from .models import User

admin.site.site_header = "My Custom Admin"
admin.site.site_title = "My Custom Admin Portal"
admin.site.register(User)