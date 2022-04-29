from django.contrib import admin

from .models import Passwords
from .models import Store
from .models import NewUser
# Register your models here.
admin.site.register(Passwords)
admin.site.register(Store)
admin.site.register(NewUser)
