"""bit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import transaction, LoginAPIView, create_transaction, eth_api, bch_api, xlm_api, usdt_api, usd_api, available_btc, remaining_btc

urlpatterns = [
    path('admin/', admin.site.urls),
    path('transactions/', transaction, name='transaction'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('create/', create_transaction, name='create'),
    path('eth-api/', eth_api, name='eth-api' ),
    path('bch-api/', bch_api, name='bch-api' ),
    path('usdt-api/', usdt_api, name='usdt-api' ),
    path('xlm-api/', xlm_api, name='xlm-api' ),
    path('usd-api/', usd_api, name='usd-api' ),
    path('available/', available_btc, name='available-btc' ),
    path('remaining/<tran>/', remaining_btc, name='remaining'),
]
