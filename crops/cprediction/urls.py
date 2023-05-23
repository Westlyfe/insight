
from django.urls import path
from cprediction.views import Home,result

urlpatterns = [
    path("",view=Home,name="home"),
    path("result",view=result,name="result"),
]
