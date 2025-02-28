from django.urls import path 
from cart import views

urlpatterns = [
    path('me/' ,views.GetUserCart.as_view() ,name = 'get-user-cart'),
    path('add/' ,views.AddItemToCart.as_view() ,name = 'add-to-cart'),
    path('count/' ,views.CartCount.as_view() ,name = 'count'),
    path('delete/' ,views.RemoveItemFromCart.as_view() ,name = 'delete'),
    path('update/' ,views.UpdateCartItemQuantitiy.as_view() ,name = 'update-count'),

]