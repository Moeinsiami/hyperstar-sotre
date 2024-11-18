from django.urls import path
from . import views


app_name = 'store'
urlpatterns = [
    path('', views.index, name='index'),
    path('contact-us', views.contact_us, name='contact_us'),
]
