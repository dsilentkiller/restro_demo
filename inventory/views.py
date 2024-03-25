
from django.shortcuts import render
from inventory.models import Inventory
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from inventory.forms import InventoryForm
# from menu.models import Recipe


def base(request):
    return render(request, 'inventory/base.html')
# ===============================================inventory =========================================##


class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory/inventory_list.html'
    success_url = reverse_lazy('inventory:inventory_list')


class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:inventory_list')


class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('inventory:inventory_list')


class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory/inventory_detail.html'
    success_url = reverse_lazy('inventory:inventory_list')


class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory/inventory_delete.html'
    success_url = reverse_lazy('inventory:inventory_list')

# inventory search using function


class InventorySearchView(ListView):
    model = Inventory
    template_name = "inventory/inventory_list.html"
    context_object_name = "inventory"

    success_url = reverse_lazy('inventory:inventory_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return self.model.objects.filter(
            ingredient__name__contains=self.request.GET.get(
                "ingredient__name", ""), )  # key value
        # foreign key bhakole search garna milena
        # item__name__icontains=self.request.GET.get("item_name", ""),)
        # price__contains=self.request.GET.get("price", ""),
        # quantity__contains=self.request.GET.get("quantity", ""),
