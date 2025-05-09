from django.urls import path
from . import views   # type: ignore

urlpatterns = [path('', views.catalog, name='catalog'),]