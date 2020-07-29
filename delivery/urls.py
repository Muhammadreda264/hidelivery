from django.urls import include, path

from delivery import views
from delivery.views import StoreSignUpView, OrderDetailView,DriverSignUpView,OrderListView


urlpatterns = [

    path('store/signup/', views.StoreSignUpView.as_view(), name='storesignup'),
    path('driver/signup/', views.DriverSignUpView.as_view(), name='driversignup'),
    path('neworder/', views.OrderCreateView.as_view(), name='neworder'),
    path('editorder/<int:pk>/', views.OrderUpdateView.as_view(), name='editorder'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('myorders/', OrderListView.as_view(), name='myorders'),
    path('',views.home,name='home')

]
