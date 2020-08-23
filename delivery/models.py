from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from datetime import date


class User(AbstractUser):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        verbose_name='اسم المستخدم',
        max_length=150,
        unique=True,
        help_text=('يتطلب 150 حرف أو أقل .يمكن أن يحتوي أحرف أو ارقام أو @/./+/-/_ فقط.'),
        validators=[username_validator],
        error_messages={
            'unique': ("اسم المستخدم موجود بالفعل"),
        },
    )
    is_store = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    phone = models.CharField(max_length=30, verbose_name="رقم الجوال ")


class Store(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    adder = models.CharField(max_length=1000, default='', verbose_name="عنوان المتجر ")
    name = models.CharField(max_length=500, verbose_name="اسم المتجر ")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "متاجر"
        verbose_name = 'متجر'


class Driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    city = models.CharField(max_length=1000, default='')
    name = models.CharField(max_length=500)

    def __str__(self):
        return f" {self.name}, {self.city}."

    class Meta:
        verbose_name_plural = "سائقين"
        verbose_name = 'سائق'


class Order(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, blank=True, null=True)
    desc = models.TextField(default="", verbose_name="وصف الطلب")
    customername = models.CharField(max_length=300, default='', verbose_name="اسم العميل")
    deliverfee = models.IntegerField(default=0,verbose_name="مصاريف الشحن")
    orderfee = models.IntegerField(default=0, verbose_name="سعر الطلبية", help_text='اتركه فارغ لو كانت الطلبية مدفوعة')
    driverfee=models.IntegerField(default=20,verbose_name="حساب السائق")
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    phone = models.CharField(max_length=30, verbose_name="رقم جوال العميل")
    adder = models.CharField(max_length=1000, default='', verbose_name="عنوان العميل ")
    delivered_at = models.DateTimeField(null=True, blank=True)


    class Status(models.TextChoices):
        NEW = 'NE', 'جديدة لم يعين سائق'
        PENDING = 'PN', 'في انتظار وصول السائق للمتجر'
        SHIPPED = 'SH', 'تم الشحن للتسليم'
        DELIVERED = 'DE', 'استلمها العميل'
        CANCELLED = 'CA', 'ملغية'

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.NEW,
    )

    def save(self, *args, **kwargs):
        if self.driver and self.status == 'NE':
            self.status = 'PN'
        if not self.delivered_at and self.status == 'DE':
            self.delivered_at=date.today()
        super().save(*args, **kwargs)

    def __str__(self):
        return f" {self.store}."

    class Meta:
        verbose_name_plural = "طلبات"
        verbose_name = 'طلب'
