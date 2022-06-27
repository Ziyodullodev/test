from django.urls import path
from .views import LoginView, RegisterView, GetUser, ExampleView


urlpatterns = [
    path('login/', LoginView.as_view()),
    path('reg/', RegisterView.as_view()),
    path('get/<int:pk>', GetUser.as_view()),
    path('me/', ExampleView.as_view()),
]
