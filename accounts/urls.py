from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.index, name='accounts_index'),
    path('display/', views.display, name='accounts_display'),
]
