from django.urls import include,path

from .views import ProductDetail,ProductList

app_name="products"

urlpatterns = [
    
    path('',ProductList.as_view()),
    path('<int:pk>',ProductDetail.as_view())
]





