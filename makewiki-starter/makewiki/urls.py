from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Admin Site
    path('accounts/login/', admin.site.urls),

    # Wiki App
    path('', include('wiki.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
