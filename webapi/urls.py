from django.urls import path
from django.urls import include
from .views import ProductList
from rest_framework import routers

router = routers.DefaultRouter()
router.register ('products', ProductList)

urlpatterns = [
    path('/',include(router.urls)),
]
