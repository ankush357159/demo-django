from django.urls import path

import views
from student.views import MyView, MyCreateView

urlpatterns = [
    path('', views.hello),
    path('about/', MyCreateView),
]