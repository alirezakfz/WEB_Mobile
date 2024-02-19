from django.urls import path
from . import views

from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
    path('book/', views.book, name="book"),
    path('api/menu-items', views.menu_items, name="menu-items"),
    path('api/menu-items/<int:id>', views.single_item),
    path('api/cls-items', views.MenuList.as_view()),
    path('api/cls-items/<int:pk>', views.SingleMenuItem.as_view()),
    path('api/generic', views.MenuItemViews.as_view()),
    path('api/generic/<int:pk>', views.SingleMenuItemsView.as_view()),
    path('api/category/<int:pk>',views.category_detail, name="category-detail"),
    path('api/htmlmenu',views.menu_html, name="html-menu-display"),
    path('api/',views.welcome, name="html-menu-display"),
    path('api/menu-items-viewset',views.MenuItemsViewSet.as_view({'get':'list'})),
    path('api/menu-items-viewset/<int:pk>',views.MenuItemsViewSet.as_view({'get':'retrieve'})),
    path('api/categories', views.CategoriesView.as_view()),
    path('api/secret', views.secret, name="secret-msg"),
    path('api/api-token-auth/', obtain_auth_token), # Only Accepts POST
    path('api/manager-view/', views.manager_view, name="manager-view"), 
    path('api/throttle-check/', views.throttle_check, name="throttle-check"),
    path('api/throttle-check-auth/', views.throttle_check_auth, name="throttle-check-auth"),
    path('api/menu-items-viewset-auth',views.MenuItemsViewSetAuth.as_view({'get':'list'})),
    path('api/menu-items-viewset-auth/<int:pk>',views.MenuItemsViewSetAuth.as_view({'get':'retrieve'})),
    path('api/groups/manager/users', views.add_to_managers, name="add-manager"),    
]