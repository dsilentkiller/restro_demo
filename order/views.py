from django.shortcuts import render
from order.models import Order,  Table
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from order.forms import OrderForm, TableForm
from menu.models import Recipe
from inventory.models import Inventory
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

######################## table ###########################


class TableListView(ListView):
    model = Table
    template_name = 'table/table_list.html'
    success_url = reverse_lazy('order:table_list')


class TableCreateView(CreateView):
    model = Table
    form_class = TableForm
    template_name = 'table/table_form.html'
    success_url = reverse_lazy('order:table_list')


class TableUpdateView(UpdateView):
    model = Table
    form_class = TableForm
    template_name = 'table/table_form.html'
    success_url = reverse_lazy('order:table_list')


# class TableDetailView(DetailView):
#     model = Table
#     template_name = 'item/item_detail.html'
#     success_url = reverse_lazy('order:item_list')


class TableDeleteView(DeleteView):
    model = Table
    template_name = 'table/table_delete.html'
    success_url = reverse_lazy('order:table_list')

# inventory search using function


class LoginView(ListView):
    model = User
    # template_name = 'user/login.html'
    success_url = reverse_lazy('order:order_create')


class TableSearchView(ListView):
    model = Table
    template_name = "table/table_list.html"
    context_object_name = "table"

    # success_url = reverse_lazy('order:item_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    # def get_queryset(self, request):
    #     query = self.request.GET.get("q", "")
    #     results = Item.objects.none()
    #     if query:
    #         results = Item.objects.filter(name__icontains=query)
    #         return render(request, 'item/item_list.html', {'item': results})
    #     else:
    #         results = Item.objects.none()


def SearchView(request):
    query = request.GET.get('q', '')  # retrieve the search query
    results = Table.objects.none()  # initialize an empty queryset

    if query:

        results = Table.objects.filter(name__icontains=query)

        return render(request, 'table/table_list.html', {'object_list': results})
    else:
        results = Table.objects.none()

# ================================================order -============================================================================


class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    success_url = reverse_lazy('order:order_list')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order:order_list')
    order = Order.objects.all()

    def form_valid(self, form):
        response = super().form_valid(form)
        order_id = self.object.pk
        try:
            order_item = Order.objects.get(pk=order_id)
            # get associated menu item
            menu_item = order_item.order_item
            # get recipe for menu
            recipes = Recipe.objects.filter(menu_item=menu_item)
            # calculate ingredient usage and update available quantity
            for requirement in recipes:
                ingredient = requirement.ingredient
                quantity_used = requirement.quantity * order_item.quantity
                ingredient.available_qty -= quantity_used
                ingredient.save()
            total_price = order_item.quantity * order_item.order_item .price
            context = {
                'total_price': total_price
            }
        except Order.DoesNotExist:
            # Handle the case where the OrderItem does not exist
            # For example, redirect to an error page or display an error message
            return HttpResponseRedirect('/error/')

        # Redirect the user to a success page
        return render(self.request, 'menu/calculation_ingredient.html', context)
        # order = form.save(commit=False)
        # order.save()
        # # get order item
        # order_items = Recipe.objects.filter(food_item=order.order_item)
        # for order_item in order_items:
        #     quantity_used = order.order_quantity * order_item.recipe_quantity
        #     inventory_item = Inventory.objects.get(
        #         ingredient_name=order.order_item)

        #     inventory_item.quantity -= quantity_used
        #     inventory_item.save()
        # return super().form_valid(form)
    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     order = form.save(commit=False)
    #     order.save()

    #     recipes = Recipe.objects.filter(food_name=order.order_item)
    #     for recipe in recipes:
    #         inventory_item = Inventory.objects.get(
    #             ingredient_name=recipe.ingredient_name)
    #         new_quantity = inventory_item.quantity - \
    #             (recipe.quantity * order.quantity)
    #         if new_quantity >= 0:
    #             inventory_item.quantity = new_quantity
    #             inventory_item.save()
    #         else:
    #             print('insufficient quantity')

    #     return response


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('order:order_list')


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_detail.html'
    success_url = reverse_lazy('order:order_list')


class OrderCancelView(DeleteView):
    model = Order
    template_name = 'order/order_cancel.html'
    success_url = reverse_lazy('order:order_list')
