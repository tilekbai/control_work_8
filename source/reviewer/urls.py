from django.urls import path
from .views import IndexView

app_name = "reviewer"

urlpatterns = [
    path('', IndexView.as_view(), name="good-list")
]