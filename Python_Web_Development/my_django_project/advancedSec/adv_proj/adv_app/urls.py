from django.urls import path
from adv_app import views

app_name = 'adv_app'

urlpatterns =[
    path('',views.SchoolList.as_view(),name='list'),
    path('<int:pk>/',views.SchoolDetail.as_view(),name='detail'),
    # int:pk is for when you click on a schools name and it
    # references the primary key of the school
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    path('update/<int:pk>/',views.SchoolUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',views.SchoolDeleteView.as_view(),name='delete'),

]
