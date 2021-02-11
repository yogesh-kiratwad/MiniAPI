from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views
from rest_framework import urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()
router.register('product',views.ProductAPI,basename='ProductModel')
router.register('cart',views.CartAPI,basename='Cart')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('gettoken/',TokenObtainPairView.as_view(),name="TokenObtain"),
    path('refreshtoken/',TokenRefreshView.as_view(), name="RefreshToken"),
    path('verifytoken/',TokenVerifyView.as_view(), name="VerifyToken")
]
