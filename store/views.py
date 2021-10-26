from django.shortcuts import render
from django.views.generic import ListView, DetailView
from store.models import Category, Product, ProductImages


class HomeListView(ListView):
    model = Product
    template_name = 'store/index.html'
    context_object_name = 'products'


# class-based view
class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_images'] = ProductImages.objects.filter(product=self.object.id)
        return context

# function-based view
# def product_details(request, pk):
#     item = Product.objects.get(id=pk)
#     photos = ProductImages.objects.filter(product=item).order('-created')
#     context = {
#         'item': item,
#         'photos': photos,
#     }
#     return render(request, 'store/product.html', context)
