from django.urls import path
from . import views


urlpatterns = [
    path('',views.listItems.as_view(),name='home'),
    path('checkout',views.checkout.as_view(),name='chekout'),
    path('reports',views.report_view,name='report'),
    path('cart_list',views.cart_list,name='cart-list'),
    path('add_order',views.place_order,name='place_order'),
    path('<pk>',views.ItemDetail.as_view()),
    path('add_to_cart/<pk>',views.add_to_cart,name='add-to-cart'),
    path('remove_from_cart/<pk>',views.remove_from_cart,name='remove_item'),
    path('remove_from_cart/<pk>/<int:single_item>',views.remove_from_cart,name='remove_single_item'),
   
    
]
