from django.urls import path
from .views import IndexView, GoodView

app_name = "reviewer"

urlpatterns = [
    path('', IndexView.as_view(), name="good-list"),
    path('<int:pk>/', GoodView.as_view(), name="good-view")
]