from django.shortcuts import render, reverse
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.utils.http import urlencode
from .models import Good, Review
from .forms import SearchForm, GoodForm
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


class Good_updateView(UpdateView):    
    model = Good
    template_name = 'goods/good_update.html'
    form_class = GoodForm
    context_object_name = 'good'

    def get_success_url(self):
        return reverse('reviewer:good-view', kwargs={'pk': self.object.pk})


class Good_deleteView(DeleteView):
    template_name = 'goods/good_delete.html'
    model = Good
    context_object_name = 'good'
    success_url = reverse_lazy('reviewer:good-list')