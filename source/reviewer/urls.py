from django.urls import path
from .views import IndexView, GoodView, Good_updateView, Good_deleteView, GoodCreateView, Good_Review_CreateView, Review_deleteView, Review_UpdateView

app_name = "reviewer"

urlpatterns = [
    path('', IndexView.as_view(), name="good-list"),
    path('<int:pk>/', GoodView.as_view(), name="good-view"),
    path('<int:pk>/update', Good_updateView.as_view(), name="good-update"),
    path('<int:pk>/delete', Good_deleteView.as_view(), name="good-delete"),
    path('add_good/', GoodCreateView.as_view(), name="good-add"),
    path('<int:pk>/review_add', Good_Review_CreateView.as_view(), name="review-add"),
    path('delete_review/<int:pk>', Review_deleteView.as_view(), name="review-delete"),
    path('update_review/<int:pk>', Review_UpdateView.as_view(), name="review-update"),
]