from django.shortcuts import render
from app.models import RecipeRequirement, Order, Inventory, Menu
from app.forms import OrderForm, RecipeRequirementForm, InventoryForm, MenuForm
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

# ================================================Order -============================================================================


class OrderListView(ListView):
    model = Order
    template_name = 'order/order_list.html'
    success_url = reverse_lazy('app:order_list')


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'order/order_form.html'
    success_url = reverse_lazy('app:order_list')
    Order = Order.objects.all()

    def form_valid(self, form):
        response = super().form_valid(form)
        Order_id = self.object.pk
        try:
            Order_item = Order.objects.get(pk=Order_id)
            # get associated menu item
            menu_item = Order_item.Order_item
            # get recipe for menu
            recipes = RecipeRequirement.objects.filter(menu_item=menu_item)
            # calculate ingredient usage and update available quantity
            for requirement in recipes:
                ingredient = requirement.ingredient
                quantity_used = requirement.quantity * Order_item.quantity
                ingredient.available_qty -= quantity_used
                ingredient.save()
            total_price = Order_item.quantity * Order_item.Order_item .price
            context = {
                'total_price': total_price
            }
        except Order.DoesNotExist:
            # Handle the case where the OrderItem does not exist
            # For example, redirect to an error page or display an error message
            return HttpResponseRedirect('/error/')

        # Redirect the user to a success page
        return render(self.request, 'menu/calculation_ingredient.html', context)
        # Order = form.save(commit=False)
        # Order.save()
        # # get Order item
        # Order_items = Recipe.objects.filter(food_item=Order.Order_item)
        # for Order_item in Order_items:
        #     quantity_used = Order.Order_quantity * Order_item.recipe_quantity
        #     inventory_item = Inventory.objects.get(
        #         ingredient_name=Order.Order_item)

        #     inventory_item.quantity -= quantity_used
        #     inventory_item.save()
        # return super().form_valid(form)
    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     Order = form.save(commit=False)
    #     Order.save()

    #     recipes = Recipe.objects.filter(food_name=Order.Order_item)
    #     for recipe in recipes:
    #         inventory_item = Inventory.objects.get(
    #             ingredient_name=recipe.ingredient_name)
    #         new_quantity = inventory_item.quantity - \
    #             (recipe.quantity * Order.quantity)
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
    success_url = reverse_lazy('app:order_list')


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order/order_detail.html'
    success_url = reverse_lazy('app:order_list')


class OrderCancelView(DeleteView):
    model = Order
    template_name = 'order/order_cancel.html'
    success_url = reverse_lazy('app:order_list')


# ============================== recipe ================================

class RecipeRequirementListView(ListView):
    model = RecipeRequirement
    template_name = 'recipe/recipe_requirement_list.html'
    success_url = reverse_lazy('app:order_list')


class RecipeRequirementCreateView(CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = 'recipe/recipe_requirement_form.html'
    success_url = reverse_lazy('app:recipe_list')
    Order = Order.objects.all()


class RecipeRequirementUpdateView(UpdateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = 'recipe/recipe_requirement_form.html'
    success_url = reverse_lazy('app:recipe_list')


class RecipeRequirementDetailView(DetailView):
    model = RecipeRequirement
    template_name = 'recipe/recipe_requirement_detail.html'
    success_url = reverse_lazy('app:recipe_list')


class RecipeRequirementDeleteView(DeleteView):
    model = RecipeRequirement
    template_name = 'recipe/recipe_requirement_delete.html'
    success_url = reverse_lazy('app:recipe_list')

# =========================== inventory=======================================


class InventoryListView(ListView):
    model = Inventory
    template_name = 'inventory/inventory__list.html'
    success_url = reverse_lazy('app:order_list')


class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('app:recipe_list')
    Order = Order.objects.all()


class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = RecipeRequirementForm
    template_name = 'inventory/inventory_form.html'
    success_url = reverse_lazy('app:recipe_list')


class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory/inventory_detail.html'
    success_url = reverse_lazy('app:recipe_list')


class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory/inventory_delete.html'
    success_url = reverse_lazy('app:recipe_list')

# =========================== menu=======================================


class MenuListView(ListView):
    model = Menu
    template_name = 'menu/menu_list.html'
    success_url = reverse_lazy('app:order_list')


class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/menu_form.html'
    success_url = reverse_lazy('app:recipe_list')
    Order = Order.objects.all()


class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/menu_form.html'
    success_url = reverse_lazy('app:recipe_list')


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu/menu_detail.html'
    success_url = reverse_lazy('app:recipe_list')


class MenuDeleteView(DeleteView):
    model = Menu
    template_name = 'menu/menu_delete.html'
    success_url = reverse_lazy('app:recipe_list')
