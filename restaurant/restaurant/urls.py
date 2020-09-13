"""restaurant URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# For Media URL
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Access App's Urls
    path('access/', include('apps.access_apps.access.urls'), name='access'),

    # Backend App's Urls
    path('food/', include('apps.backend_apps.food.urls'), name='food'),
    path('order/', include('apps.backend_apps.order.urls'), name='order'),
    path('report/', include('apps.backend_apps.report.urls'), name='report'),

    # Frontend App's Urls
    #path('feedback/', include('apps.frontend_apps.feedback.urls'), name='feedback'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
