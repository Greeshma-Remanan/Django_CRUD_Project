"""
URL configuration for Mobile project.

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
from Work.views import MobileView,Mobilelist,MobileDetail,Mobile_delete,Mobile_update,Signup,SigninView,Signout
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add/',MobileView.as_view(),name='add'),
    path('mobile/all/',Mobilelist.as_view(),name='mobile-al'),
    path('mobiled/<int:pk>',MobileDetail.as_view(),name='mobile-det'),
    path('mobile/<int:pk>/remove',Mobile_delete.as_view(),name='mobile-del'),
    path('mobile/<int:pk>/edit',Mobile_update.as_view(),name='mobile-edit'),
    path('reg/',Signup.as_view()),
    path('',SigninView.as_view(),name='login'),
    path('logout/',Signout.as_view(),name='logout')
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
