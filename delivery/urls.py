from django.urls import include, path

from delivery import views
from delivery.views import StoreSignUpView, OrderDetailView, OrderListView,DriverSignUpView


urlpatterns = [

    path('store/registar/', views.StoreSignUpView.as_view(), name='storeregistar'),
    path('driver/registar/', views.DriverSignUpView.as_view(), name='driverregistar'),
    path('neworder/', views.OrderCreateView.as_view(), name='neworder'),
    path('editorder/<int:pk>/', views.OrderUpdateView.as_view(), name='editorder'),
    path('<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('myorders/', OrderListView.as_view(), name='myorders'),
    path('home',views.home,name='home')

]
