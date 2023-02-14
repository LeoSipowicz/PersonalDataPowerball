from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.get_data, name='personal-data-input'),
    path('big-spin/', views.big_spin),
    path('big-spin/lotto-results/', views.lotto_results),
]
