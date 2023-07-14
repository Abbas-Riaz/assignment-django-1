from django.urls import path
from . import views

app_name ='ab'

urlpatterns = [
    path('detail/' , views.home,name="detail"),
    path ('index/'  , views.index , name="index"),
    path('1' ,views.red , name="abb"),
]