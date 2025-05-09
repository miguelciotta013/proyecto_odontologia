from django.urls import path
from catalog import views   # type: ignore

urlpatterns = [path('', views.catalog, name='catalog'),]