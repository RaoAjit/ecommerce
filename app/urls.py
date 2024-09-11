from django.urls import path
from django.conf.urls.static import static
from app import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm,PasswordResetForm,SetPasswordForm
from .form import chpassword,passwordre
from app.form import loginn
urlpatterns = [
    path('', views.home),
    path('product-detail/<int:id>',views.product_detail.as_view(), name='product-detail'),
    path('add-to-cart/',views.add_to_cart,name='add-to-cart'),
    path('show-cart/',views.showcart,name="show-cart"),
    path('pluscart/',views.plus_cart,name='pluscart'),
    path('search/',views.search,name='search'),
    path('minus-cart/',views.minus_cart),
    path('remove-cart/',views.remove_cart),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('laptop/', views.laptop, name='laptop'),
    path('passwordreset',auth_views.PasswordResetView.as_view(template_name="app/passwordreset.html",form_class=passwordre),name="passwordreset"),
    path('passwordreset/done',auth_views.PasswordResetDoneView.as_view(template_name="app/passwordresetdone.html"),name="password_reset_done"),
    path('passwordreset/confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="app/passwordreconfirm.html",form_class=SetPasswordForm),name="password_reset_confirm"),
    path('passwordreset/completed',auth_views.PasswordResetCompleteView.as_view(template_name="app/passwordrecompl.html"),name="password_reset_complete"),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passchange.html',form_class=chpassword ,success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passchangedone.html'),name='passwordchangedone'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=loginn), name='login'),
    path('logout/',views.log_out, name='logout'),
    path('customerregistration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/',views.paymentdone,name='paymentdone'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
