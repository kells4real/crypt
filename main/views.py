from django.shortcuts import render
from .models import Transaction, AuthUser
from .serializers import TransactionSerializer, LoginSerializer, TransactionCrudSerializer, AvailableSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, status, views, permissions
# Create your views here.
from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def transaction(request):
    user = request.user
    query = Transaction.objects.filter(user=user).order_by('-date')

    serializer = TransactionSerializer(query, many=True)

    return Response(serializer.data)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_transaction(request):
    user = request.user
    serializer = TransactionCrudSerializer(data=request.data)

    if serializer.is_valid():
        s = serializer.save(user=user)
        s.save()

        return Response ({"data": "Success"})
    else:
        return Response({"data": "Error"})

@api_view(['GET'])
def eth_api(request):
    url = "https://www.coindesk.com/price/ethereum"

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    result = soup.find('div', class_='price-large')

    #
    get_data = result.get_text()

    if ',' in get_data:
        value = get_data.split('$')[1].split(',')[0]
        value1 = get_data.split('$')[1].split(',')[1]

        value2 = float(value + value1)
    else:
        value = get_data.split('$')[1]
        value2 = float(value)
    return Response({'data': value2})

@api_view(['GET'])
def bch_api(request):
    url = "https://www.coindesk.com/price/bitcoin-cash"

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    result = soup.find('div', class_='price-large')
    #
    get_data = result.get_text()

    if ',' in get_data:
        value = get_data.split('$')[1].split(',')[0]
        value1 = get_data.split('$')[1].split(',')[1]

        value2 = float(value + value1)
    else:
        value = get_data.split('$')[1]
        value2 = float(value)
    return Response({'data': value2})


@api_view(['GET'])
def xlm_api(request):
    url = "https://www.coindesk.com/price/stellar"


    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    result = soup.find('div', class_='price-large')
    #
    get_data = result.get_text()

    if ',' in get_data:
        value = get_data.split('$')[1].split(',')[0]
        value1 = get_data.split('$')[1].split(',')[1]

        value2 = float(value + value1)
    else:
        value = get_data.split('$')[1]
        value2 = float(value)
    return Response({'data': value2})

@api_view(['GET'])
def usdt_api(request):
    url = "https://www.coindesk.com/price/tether"

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    result = soup.find('div', class_='price-large')
    #
    get_data = result.get_text()

    if ',' in get_data:
        value = get_data.split('$')[1].split(',')[0]
        value1 = get_data.split('$')[1].split(',')[1]

        value2 = float(value + value1)
    else:
        value = get_data.split('$')[1]
        value2 = float(value)
    return Response({'data': value2})


@api_view(['GET'])
def usd_api(request):
    url = "https://www.coindesk.com/price/usd-coin"

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    result = soup.find('div', class_='price-large')
    #
    get_data = result.get_text()

    if ',' in get_data:
        value = get_data.split('$')[1].split(',')[0]
        value1 = get_data.split('$')[1].split(',')[1]

        value2 = float(value + value1)
    else:
        value = get_data.split('$')[1]
        value2 = float(value)
    return Response({'data': value2})

from .models import AvailableBtc

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def available_btc(request):
    user = request.user
    available = AvailableBtc.objects.get(user=user)
    serializer = AvailableSerializer(available, many=False)

    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def remaining_btc(request, tran):
    user = request.user
    available = AvailableBtc.objects.get(user=user)
    available_after = available.btc - float(tran)
    available.btc = available_after

    available.save()

    return Response({'data': available_after})




