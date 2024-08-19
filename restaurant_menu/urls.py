from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name="home"),
    path('', views.About.as_view(), name="about"),
    path('item/<int:pk>/', views.MenuItemDetail.as_view(), name="menu_item"),
]


