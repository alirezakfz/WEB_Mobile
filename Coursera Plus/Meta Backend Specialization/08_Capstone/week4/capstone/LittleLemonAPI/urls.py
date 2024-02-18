from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

#from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r"tables/bookings", views.BookingViewSet, basename="tables-bookings")


urlpatterns = [
    path('menu-items', views.MenuItemViews.as_view(), name = "menu-items"),
    path('menu-items/<int:pk>', views.SingleMenuItemsView.as_view(), name = "menu-item"),
    path('categories/', views.CategorItemsView.as_view(), name= "categories"),
    path('groups/manager/users', views.ManagerUsersView.as_view(), name="managers"),
    path('groups/manager/users/<int:pk>', views.SingleManagerUsersView.as_view(), name="manager"),
    path('groups/delivery-crew/users', views.DeliveryCrewView.as_view(), name="deliveries"),
    path('groups/delivery-crew/users/<int:pk>', views.SingleDeliveryCrewView.as_view(), name="delivery"),
    #path('token/login', obtain_auth_token), # Only Accepts POST
    # path('cart/menu-items', views.CartViewSet.as_view({'get':'list', 'post':'create', 'delete':'destroy'}), name="cart-items"), # Only Accepts POST
    path('cart/menu-items', views.CartView.as_view(), name="cart-view"), 
    path('orders', views.OrdersView.as_view(), name="orders"),
    path('orders/<int:pk>', views.OrderDetailView.as_view(), name="order-detail"),
    path('cart/orders', views.OrdersView.as_view(), name="cart-order"),
    path('cart/orders/<int:pk>', views.OrderItemView.as_view(), name="order-item"),
    path('menu/', views.menu, name="menu"),
    path('', views.home, name="home"),
    path('book/', views.book, name="book"),
    path('reservations/', views.reservations, name="reservations"),
    path('bookings', views.bookings, name='bookings'),
    path('about/', views.about, name="about"),
    path("", include(router.urls)),
]