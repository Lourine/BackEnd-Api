from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^api/customer/$', views.CustomerList.as_view()),
    url(r'^api/order/$', views.OrderList.as_view())
   ## url(r'^api/authenticate/$', views.OrderList.as_view())

]