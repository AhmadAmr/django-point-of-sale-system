from django.urls import path
from . import views


urlpatterns = [
    path('',views.listItems.as_view(),name='home'),
    path('checkout',views.checkout.as_view(),name='chekout'),
    path('cart_list',views.cart_list,name='cart-list'),
    path('<pk>',views.ItemDetail.as_view()),
    path('add_to_cart/<pk>',views.add_to_cart,name='add-to-cart'),
    
]
