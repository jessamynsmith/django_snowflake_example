from django.urls import path

from example import views


urlpatterns = [
    path('', views.ReasonListView.as_view(), name='reason-list'),
]
