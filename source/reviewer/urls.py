from django.urls import path
from .views import IndexView, GoodView, Good_updateView

app_name = "reviewer"

urlpatterns = [
    path('', IndexView.as_view(), name="good-list"),
    path('<int:pk>/', GoodView.as_view(), name="good-view"),
    path('<int:pk>/update', Good_updateView.as_view(), name="good-update")
]