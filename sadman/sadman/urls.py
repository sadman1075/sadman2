"""
URL configuration for sadman project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from myapp import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('userwork', views.userwork, name='userwork'),
    path('', views.home, name='home'),

    path('login', views.loginpage, name='login'),
    path('glasswaste', views.glasswaste1, name='glasswaste'),
    path('plasticswaste', views.plasticswaste1, name='plasticswaste'),
    path('medicalwaste', views.medicalwaste2, name='medicalwaste'),
    path('constructionwaste', views.constructionwaste1, name='constructionwaste'),
    path('singup', views.singuppage, name='singup'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('contract',views.contract,name='contract')


]+static(settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT)
