from django.contrib import admin

from visa.models import Tag, Visa, VisaCategory

# Register your models here.
admin.site.register(Visa)
admin.site.register(Tag)
admin.site.register(VisaCategory)
