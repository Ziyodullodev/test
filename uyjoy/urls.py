from django.urls import path
from .views import IjaraViewSet, IjaraUpdateViewSet
urlpatterns = [
    path('', IjaraViewSet.as_view()),
    path('update/<int:pk>', IjaraUpdateViewSet.as_view()),
    # path('api/users/', include('uyjoy.urls')),
]
