from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, ListView
from delivery.decorators import store_required, driver_required
from delivery.forms import StoreSignUpForm, DriverSignUpForm
from delivery.models import User, Order


class StoreSignUpView(CreateView):
    model = User
    form_class = StoreSignUpForm
    template_name = 'storesignup.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'store'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

class DriverSignUpView(CreateView):
    model = User
    form_class = DriverSignUpForm
    template_name = 'driver_sign_up.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'driver'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def home(request):
    if request.user.is_authenticated:
            if request.user.is_store:
                return redirect('storehome')
            else:
                return redirect('driverhome')
    return render(request, 'home.html')


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator([login_required, store_required], name='dispatch')
class OrderCreateView(CreateView):
    model = Order
    fields = ['customername','desc', 'orderfee', 'phone', 'adder']
    template_name = 'neworder.html'


    def form_valid(self, form):
        order = form.save(commit=False)
        order.store = self.request.user.store
        order.save()
        messages.success(self.request, 'تم تسجيل الطلبية بنجاح')
        return redirect('home')


@method_decorator([login_required, store_required], name='dispatch')
class OrderListView(ListView):
    model = Order
    template_name = 'my_orders.html'

    def get_queryset(self):
        compeltedstatus = ['DE', 'CA']
        return Order.objects.filter(store=self.request.user.store).exclude(status__in=compeltedstatus)


@method_decorator([login_required, store_required], name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    fields = ['desc', 'orderfee', 'phone', 'adder']
    context_object_name = 'order'
    template_name = 'updateorder.html'

    def get_queryset(self):
        compeltedstatus = ['NE', 'PN']
        s = self.request.user.store
        orders = Order.objects.filter(store=s).filter(status__in=compeltedstatus)
        return orders

    def get_success_url(self):
        return reverse('home')

@method_decorator([login_required, driver_required], name='dispatch')
class DriverOrderListView(ListView):
    model = Order
    template_name = 'driverorders.html'

    def get_queryset(self):
        compeltedstatus = ['DE', 'CA']
        return Order.objects.filter(driver=self.request.user.driver).exclude(status__in=compeltedstatus)

@login_required
@driver_required
def updateOrderStatus(request,pk):
    order =Order.objects.filter(pk=pk).first()
    if order.driver and  order.driver  == request.user.driver:
        if order.status == 'SH':
            order.status = 'DE'
        if order.status =='PN':
         order.status='SH'

        order.save()
    return redirect('home')
