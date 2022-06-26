from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="list_tickers"),
    path('new/', views.new, name="new_ticker"),
    path('get_ticker_info/', views.ticker_info, name="get_ticker_info")
]
