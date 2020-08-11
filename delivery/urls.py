from django.urls import include, path

from delivery import views
from delivery.views import StoreSignUpView, OrderDetailView, DriverSignUpView, OrderListView, DriverOrderListView

urlpatterns = [

    path('store/signup/', views.StoreSignUpView.as_view(), name='storesignup'),
    path('driver/signup/', views.DriverSignUpView.as_view(), name='driversignup'),
    path('neworder/', views.OrderCreateView.as_view(), name='neworder'),
    path('editorder/<int:pk>/', views.OrderUpdateView.as_view(), name='editorder'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('store/home', OrderListView.as_view(), name='storehome'),
    path('',views.home,name='home'),
    path('driver/home',DriverOrderListView.as_view(),name='driverhome'),
    path('updateorderstatus/<int:pk>/', views.updateOrderStatus, name='updateorderstatus'),


]
