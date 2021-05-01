from django.urls import path
from .views import IndexView, GoodView, Good_updateView, Good_deleteView, GoodCreateView

app_name = "reviewer"

urlpatterns = [
    path('', IndexView.as_view(), name="good-list"),
    path('<int:pk>/', GoodView.as_view(), name="good-view"),
    path('<int:pk>/update', Good_updateView.as_view(), name="good-update"),
    path('<int:pk>/delete', Good_deleteView.as_view(), name="good-delete"),
    path('add_good/', GoodCreateView.as_view(), name="good-add"),
]