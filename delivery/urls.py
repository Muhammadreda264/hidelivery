from django.urls import include, path

from delivery import views
from delivery.views import ViewPDF, OrderDetailView, DriverSignUpView, OrderListView, DriverOrderListView, \
    CompeltedOrderListView, DriverCompeltedOrderListView

urlpatterns = [

    path('store/signup/', views.StoreSignUpView.as_view(), name='storesignup'),
    path('driver/signup/', views.DriverSignUpView.as_view(), name='driversignup'),
    path('neworder/', views.OrderCreateView.as_view(), name='neworder'),
    path('editorder/<int:pk>/', views.OrderUpdateView.as_view(), name='editorder'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('store/home', OrderListView.as_view(), name='storehome'),
    path('store/completedorders', CompeltedOrderListView.as_view(), name='completedorders'),
    path('driver/completedorders', DriverCompeltedOrderListView.as_view(), name='drivercompletedorders'),
    path('',views.home,name='home'),
    path('driver/home',DriverOrderListView.as_view(),name='driverhome'),
    path('updateorderstatus/<int:pk>/', views.updateOrderStatus, name='updateorderstatus'),
    path('printorder/', ViewPDF.as_view(), name='printorder'),


]
