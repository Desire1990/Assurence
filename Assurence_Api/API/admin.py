from django.contrib import admin
from .models import *

admin.site.register(Profile)
# admin.site.register(Photo)
admin.site.register(Payment)
admin.site.register(Automobile)
admin.site.site_header = "Assurence Automobile"