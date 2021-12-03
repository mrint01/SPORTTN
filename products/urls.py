from django.urls import path
from . import views

urlpatterns = [
    path('proteine/',views.ProtAction , name="product"),
     path('proteine/<int:pk>/',views.ProtDetailAction , name="productDetails"),
]