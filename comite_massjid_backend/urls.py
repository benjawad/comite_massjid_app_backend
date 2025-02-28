from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pv_reunion.admin import PVReunionAdmin  

from rest_framework_simplejwt import views as jwt_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/" , include("djoser.urls") ),
    path("auth/" , include("djoser.urls.authtoken") ),
    path('api/', include('event.urls')),
    path('auth/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  
    path('api/products/', include('product.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/pv_reunion/', include('pv_reunion.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
