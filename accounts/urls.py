from django.conf.urls import url
from .import views

app_name = 'accounts'

urlpatterns = [
    url(r'^signup/$', views.signup_view, name='signup'), #http://127.0.0.1:8000/accounts/signup/
    url(r'^testing/$', views.testing_view, name='testing') #http://127.0.0.1:8000/accounts/testing/
]
