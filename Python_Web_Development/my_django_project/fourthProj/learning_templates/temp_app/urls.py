from django.urls import path
from temp_app import views

# Template tagging
app_name = 'temp_app'

urlpatterns = [
    path('relative/',views.relative,name='relative'),
    path('index/',views.index,name='index'),
    path('other/',views.other,name='other'),

]
