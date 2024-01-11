from django.contrib import admin
from django.urls import path,  include
from Products.views import  category, product
from Accounts.views import register, login
from Accounts.views import  activate
from Products.views import home
from Products.models import Products
from Products.views import home, cart,reserved
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


from Products.views import save_reserved_product





urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home, name='home'),
    path('category/<int:id>/', category, name="category"),
    path('product/<int:id>/', product, name="product"),
    path('register/', register, name="register"),
    #path('register/owner/', registerPageOwner, name="register_owner"),
    path('login/', login, name="login"),
    path('accounts/', include('allauth.urls')),
    path('cart/', cart, name='cart'),
    path('reserved/', reserved, name="reserved"),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('activate/<uidb64>/<token>', activate, name='activate'),
    #path('accounts/profile/', login_required(ProfileView.as_view()), name='profile'),
    # path('save_reserved_product/', SaveReservedProductView.as_view(), name='save_reserved_product'),
    #path('reserve/', reserve_products, name='reserve_products'),
    path('save_reserved_product/', save_reserved_product, name='save_reserved_product'),
]
