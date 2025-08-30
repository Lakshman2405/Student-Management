from django.urls import path
from . import views

app_name='MedicalStudent'
urlpatterns =[
    path('manage/',views.manage_view,name='manage'),
    path('edit/<str:reg_num>/',views.edit_view,name='edit'),
    path('delete/<str:reg_num>/',views.delete_view,name='delete'),
]