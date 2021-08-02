from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('project/alloc/',views.projectCreateView.as_view(), name="alloc"),
    path('project/alloc/viewalloc/', views.projectAllocView.as_view(), name="viewalloc"),

]