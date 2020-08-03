from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    path('report/retail', views.ecommerce_report_page, name='retail_report'),
    path('report/marketing', views.marketing_report_page, name='marketing_report'),
    path('report/task', views.task, name='task'),
]