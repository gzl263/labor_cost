"""定义labor_costs的URL模式"""

from django.urls import path

from . import views

app_name = 'labor_costs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    # 导入新数据的页面
    path('new_data/', views.new_data, name='new_data'),
]