from django.contrib import admin
from proj_app.models import AccessRecord,Topic,WebPage
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(Topic)
