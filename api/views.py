from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductSerializer, CartSerializer
from .models import ProductModel, Cart
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from .pagination import MyPagination
from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class ProductAPI(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

    #FILTERING AND SEARCHING
    filterset_fields = ['brand','category']
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name','brand','category']
    
    #PAGINATION
    pagination_class = MyPagination
    
class CartAPI(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # Session Authentication 
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticatedOrReadOnly]

    #JWT Authentication
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    