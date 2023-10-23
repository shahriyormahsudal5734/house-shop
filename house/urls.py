from .views import homepage,detail,Detailpage,Add
from django.urls import path

urlpatterns = [
    path('', homepage, name='home'),
    path('viloyat/', detail, name='detail'),
    path('viloyat/<pk>/', Detailpage.as_view(), name='pageid'),
    path('add/', Add.as_view(), name='add'),

]
