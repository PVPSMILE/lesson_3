from django.urls import path
from .views import login_page

urlpatterns = [
    path('login_page/', login_page, name='login_page'),
]
