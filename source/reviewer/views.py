from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.utils.http import urlencode
from .models import Good, Review
from .forms import SearchForm, GoodForm, ReviewForm
# Create your views here.

class IndexView(ListView):
    template_name = "goods/index.html"
    model = Good
    context_object_name = "goods"
    ordering = ("summary")
    paginate_by = 10
    paginate_orphans = 1

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()

        return super(IndexView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_data:
            queryset = queryset.filter(
                Q(summary__icontains = self.search_data) |
                Q(description__icontains = self.search_data)
            )
        return queryset

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search_value"]
        return None


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search_form"] = self.form

        if self.search_data:
            context["query"] = urlencode({"search_value": self.search_data})

        return context


class GoodView(DetailView):
    model = Good
    template_name = 'goods/good_view.html'


class Good_updateView(PermissionRequiredMixin, UpdateView):    
    model = Good
    template_name = 'goods/good_update.html'
    form_class = GoodForm
    context_object_name = 'good'
    permission_required = 'reviewer.change_good'

    def get_success_url(self):
        return reverse('reviewer:good-view', kwargs={'pk': self.object.pk})


class Good_deleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'goods/good_delete.html'
    model = Good
    context_object_name = 'good'
    success_url = reverse_lazy('reviewer:good-list')
    permission_required = 'reviewer.delete_good'


class GoodCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'goods/add_good.html'
    model = Good
    form_class = GoodForm
    permission_required = 'reviewer.add_good'

    def form_valid(self, form):
        good = form.save(commit = False)
        good.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse('reviewer:good-view', kwargs={'pk': self.object.pk})


class Good_Review_CreateView(CreateView):
    model = Review
    template_name = 'reviews/review_create.html'
    form_class = ReviewForm
    
    def form_valid(self, form):
        good = get_object_or_404(Good, pk=self.kwargs.get('pk'))
        review = form.save(commit=False)
        review.good = good
        review.author = self.request.user
        review.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            'reviewer:good-view',
            kwargs={'pk': self.kwargs.get('pk')}
        )


class Review_deleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'reviews/review_delete.html'
    model = Review
    context_object_name = 'review'
    success_url = reverse_lazy('reviewer:good-list')
    permission_required = 'reviewer.delete_review'


class Review_UpdateView(PermissionRequiredMixin, UpdateView):    
    model = Review
    template_name = 'reviews/review_update.html'
    form_class = ReviewForm
    context_object_name = 'review'
    permission_required = 'reviewer.change_review'
    success_url = reverse_lazy('reviewer:good-list')