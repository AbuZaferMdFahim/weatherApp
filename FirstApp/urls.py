'''from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
    path('myapi/', views.ContactList.as_view(), name='contact-list'),
    path('details/<int:pk>/', views.GenericApiDetail.as_view()),
    path('', views.api_root),
])


from django.urls.conf import include
from FirstApp import views
from FirstApp.views import ContactViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contact', ContactViewSet, basename='contact')

urlpatterns = [
    path('',include(router.urls))
]'''

from django.urls import path 
from . import views

urlpatterns =[
    path('',views.index)
]
