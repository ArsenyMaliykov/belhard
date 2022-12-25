from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView

from .models import Category, Product
from .forms import Calculator, FeedbackForm


mixin = {
    'facebook': 'https://facebook.com',
    'twitter': 'https://twitter.com',
    'brand_name': 'BelHard'
}


def index(request: HttpRequest):
    categories = Category.objects.all().order_by('-name')
    products = Product.objects.all()
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, 'app/index.html', {
        'categories': categories,
        'products': products,
        'feedback_form': FeedbackForm()
    } | mixin)


class ContextMixin:
    content = {
        'facebook': 'https://facebook.com',
        'twitter': 'https://twitter.com',
        'brand_name': 'BelHard'
    }


class IndexView(ContextMixin, View):

    template_name = 'app/index.html'

    def get(self, request: HttpRequest) -> HttpResponse:
        categories = Category.objects.all().order.by('-name')
        products = Product.objects.all()
        content = self.content
        content.update(
            {
                'categories': categories,
                'products': products,
                'feedback_form': FeedbackForm()
            }
        )
        return render(
            request=request,
            template_name=self.template_name,
            context=content
        )

    def post(self, request: HttpRequest) -> HttpResponse:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request=request)


class IndexListView(ListView):
    model = Product
    template_name = 'app/index.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        return Product.objects.filter(is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        content = super(IndexListView, self).get_context_data()
        content['categories'] = Category.objects.all().order.by('-name')
        content['feedback_form'] = FeedbackForm()
        return content

    def post(self, request: HttpRequest) -> HttpResponse:
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
        return self.get(request=request)


def error404(request, exception):
    return HttpResponse('<b>404</b>')

