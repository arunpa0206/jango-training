from django.conf.urls import url
from . import views

urlpatterns =[
    #http://127.0.0.1:8000/webapp/
    url(r'^$', views.index, name='index'),
    #http://127.0.0.1:8000/webapp/hey/
    url(r'^hey/', views.index, name='index'),
]
