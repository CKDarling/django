from django.urls import path
from proj_app import views

urlpatterns = [
    path('fuck',views.form_name_view,name='form_name'),

    #path('search/',views.searchAccess,name='search'),
    path('search/',views.searchWebPage,name='search'),
]
