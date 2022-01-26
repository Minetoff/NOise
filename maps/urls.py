from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.default_map, name='default'),
    path('points/', views.PointsList.as_view()),
    path('points/<int:pk>/', views.PointsDetail.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)