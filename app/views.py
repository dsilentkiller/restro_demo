from django.shortcuts import render
from app.models import RecipeRequirement, Order, Inventory, Menu
from app.forms import OrderForm, RecipeRequirementForm, InventoryForm, MenuForm
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from django.http import Http404
from rest_framework.views import APIView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
# serializer
from app.models import Menu
from app.serializers import MenuSerializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
app_name = 'app'
# ================================================Order -============================================================================

@login_required(login_url="/login")
def base(request):
    return render(request, 'app/base.html')

def sign_up(request):
    # form =RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('inventory_list')
        else:
            form = RegisterForm()
    # context ={'form':form}

    return render(request,'registration/register.html' ,{'form':form})
    

class OrderListView(ListView):
    model = Order
    template_name = 'app/order/order_list.html'
    success_url = reverse_lazy('app:order_list')


class OrderCreateView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrderForm
    template_name = 'app/order/order_form.html'
    success_url = reverse_lazy('app:order_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        order_id = self.object.pk
        try:
            order_item = Order.objects.get(pk=order_id)
            # get associated menu item
            menu_item = order_item.order_item
            # get recipe for menu
            recipes = RecipeRequirement.objects.filter(
                menu_item_name=menu_item)  # recipe ko menu_item_name == orderitemko order_item anusar filter gareko
            # calculate ingredient usage and update available quantity
            for requirement in recipes:
                ingredient = requirement.ingredient
                quantity_used = requirement.quantity * order_item.order_quantity
                ingredient.available_qty -= quantity_used
                ingredient.save()
            total_price = order_item.order_quantity * order_item.order_item .price
            context = {
                'total_price': total_price
            }
        except Order.DoesNotExist:
            # Handle the case where the OrderItem does not exist
            # For example, redirect to an error page or display an error message
            return HttpResponseRedirect('/error/')

        # Redirect the user to a success page
        return render(self.request, 'app/calculation_ingredient.html', context)
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


class OrderUpdateView(UpdateView):
    model = Order
    form_class = OrderForm
    template_name = 'app/order/order_form.html'
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


class RecipeRequirementCreateView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    form_class = RecipeRequirementForm
    template_name = 'recipe/recipe_requirement_form.html'
    success_url = reverse_lazy('app:recipe_list')
    Order = Order.objects.all()


class RecipeRequirementUpdateView(LoginRequiredMixin, UpdateView):
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
    template_name = 'app/inventory/inventory_list.html'
    success_url = reverse_lazy('app:inventory_list')


class InventoryCreateView(CreateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'app/inventory/inventory_form.html'
    success_url = reverse_lazy('app:inventory_list')


class InventoryUpdateView(UpdateView):
    model = Inventory
    form_class = InventoryForm
    template_name = 'app/inventory/inventory_form.html'
    success_url = reverse_lazy('app:inventory_list')


class InventoryDetailView(DetailView):
    model = Inventory
    template_name = 'inventory/inventory_detail.html'
    success_url = reverse_lazy('app:inventory_list')


class InventoryDeleteView(DeleteView):
    model = Inventory
    template_name = 'inventory/inventory_delete.html'
    success_url = reverse_lazy('app:inventory_list')

# =========================== menu=======================================


class MenuListView(ListView):
    model = Menu
    template_name = 'app/menu/menu_list.html'
    success_url = reverse_lazy('app:menu_list')


class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'app/menu/menu_form.html'
    success_url = reverse_lazy('app:menu_list')
    Order = Order.objects.all()


class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'app/menu/menu_form.html'
    success_url = reverse_lazy('app:menu_list')


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'app/menu/menu_detail.html'
    success_url = reverse_lazy('app:menu_list')


class MenuDeleteView(DeleteView):
    model = Menu
    template_name = 'app/menu/menu_delete.html'
    success_url = reverse_lazy('app:menu_list')


################################ serializers view ###############################
class MenuList(APIView):
    '''list all menu or create a new menu'''

    def get(self, request, format=None):
        menu = Menu.objects.all()
        serializer = MenuSerializers(menu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MenuSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuDetail(APIView):
    '''retrive update or delete menu instance'''

    def get_object(self, pk):
        try:
            return Menu.objects.get(pk=pk)
        except Menu.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        menu = self.get_object(pk)
        serializer = MenuSerializers(menu)
        return Response(serializer.data)
    # put

    def put(self, request, pk, format=None):
        menu = self.get_object(pk)
        serializer = MenuSerializers(menu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        menu = self.get_object(pk)
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # delete
