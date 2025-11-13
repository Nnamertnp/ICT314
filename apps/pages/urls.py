from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # หน้า Service (ใหม่)
    path('docs/service/', views.docs_service, name='docs_service'),
]
