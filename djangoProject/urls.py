"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from Sky_Django import views
from views import auth, setting, data

urlpatterns = [
    path("api/login", auth.login_api),
    path("api/resign", auth.resign_api),
    path("api/set_password", setting.xg_password),
    path("api/set_name", setting.set_name),
    path("api/set_zone", setting.set_zone),
    path("api/zone_data", data.zone_data),
    path("api/normalModel",data.normalModel),
    path("api/knn_data", data.KnnModel),
    path("api/User_data", data.Get_User_Api),
    path("api/today_data",data.get_today_data)
]
