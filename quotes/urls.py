from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list_quotes"),
    path('get_quotes_by_ticker_and_frequency/', views.by_ticker_and_frequency, name="get_quotes_by_ticker_and_frequency")
]