
from django.shortcuts import render
from menu.models import Menu, Recipe
from django.views.generic import CreateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from menu.forms import MenuForm, RecipeForm


class MenuListView(ListView):
    model = Menu
    template_name = 'menu/menu_list.html'
    success_url = reverse_lazy('menu:menu_list')
    # queryset = Menu.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menus'] = self.queryset
        return context

    # def total_recipe_quantity(self):
    #     total_quantity = self.recipe.count()
    #     return total_quantity

        # menu_item = Menu.menu_objects.get(id=1)
        # print(menu_item)

        # total_quantity = menu_item.total_recipe_quantity()
        # print(total_quantity)


class MenuCreateView(CreateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/menu_item_form.html'
    success_url = reverse_lazy('menu:menu_list')


class MenuUpdateView(UpdateView):
    model = Menu
    form_class = MenuForm
    template_name = 'menu/menu_item_form.html'
    success_url = reverse_lazy('menu:menu_list')


class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu/menu_item_detail.html'
    success_url = reverse_lazy('menu:menu_list')


class MenuDeleteView(DeleteView):
    model = Menu
    template_name = 'menu/menu_item_delete.html'
    success_url = reverse_lazy('menu:menu_list')


def MenuSearchView(request):
    query = request.GET.get('q', '')  # retrieve the search query
    results = Menu.objects.none()  # initialize an empty queryset

    if query:

        results = Menu.objects.filter(name__icontains=query)

        return render(request, 'menu/menu_list.html', {'object_list': results})
    else:
        results = Menu.objects.none()
# ======================================================================recipe=======================


class RecipeListView(ListView):
    model = Recipe
    template_name = 'menu/recipe/recipe_list.html'
    success_url = reverse_lazy('menu:menu_list')
    queryset = Recipe.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recipe'] = self.queryset
        return context


class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'menu/recipe/recipe_form.html'
    success_url = reverse_lazy('menu:menu_list')


    def form_valid(self,form):
        food_item_id =self.kwargs['food_item_id']
        food_item=Menu.objects.get(pk=food_item_id)
        form.instance.food_item =food_item
        return super().form_valid(form)

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'menu/recipe/recipe_form.html'
    success_url = reverse_lazy('menu:recipe_list')


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'menu/recipe/recipe_detail.html'
    success_url = reverse_lazy('menu:recipe_list')


class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'menu/recipe/recipe_delete.html'
    success_url = reverse_lazy('menu:recipe_list')

# =========================== category==============================


# class CategoryListView(ListView):
#     model = Category
#     template_name = 'menu/category/category_list.html'
#     success_url = reverse_lazy('menu:category_list')
#     # queryset = Recipe.objects.all()

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['recipe'] = self.queryset
#     #     return context


# class CategoryCreateView(CreateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = 'menu/category/category_form.html'
#     success_url = reverse_lazy('menu:category_list')


# class CategoryUpdateView(UpdateView):
#     model = Category
#     form_class = CategoryForm
#     template_name = 'menu/category/category_form.html'
#     success_url = reverse_lazy('menu:category_list')


# class CategoryDetailView(DetailView):
#     model = Category
#     template_name = 'menu/category/category_detail.html'
#     success_url = reverse_lazy('menu:category_list')


# class CategoryDeleteView(DeleteView):
#     model = Category
#     template_name = 'menu/category/category_delete.html'
#     success_url = reverse_lazy('menu:category_list')


# def SearchView(request):
#     query = request.GET.get('q', '')  # retrieve the search query
#     results = Category.objects.none()  # initialize an empty queryset

#     if query:

#         results = Category.objects.filter(name__icontains=query)

#         return render(request, 'menu/category/category_list.html', {'object_list': results})
#     else:
#         results = Category.objects.none()

# # ================================ ingredient ===========================


# class IngredientListView(ListView):
#     model = Ingredient
#     template_name = 'menu/ingredient/ingredient_list.html'
#     success_url = reverse_lazy('menu:ingredient_list')
#     # queryset = Recipe.objects.all()

#     # def get_context_data(self, **kwargs):
#     #     context = super().get_context_data(**kwargs)
#     #     context['recipe'] = self.queryset
#     #     return context


# class IngredientCreateView(CreateView):
#     model = Ingredient
#     form_class = IngredientForm
#     template_name = 'menu/ingredient/ingredient_form.html'
#     success_url = reverse_lazy('menu:ingredient_list')


# class IngredientUpdateView(UpdateView):
#     model = Ingredient
#     form_class = IngredientForm
#     template_name = 'menu/ingredient/ingredient_form.html'
#     success_url = reverse_lazy('menu:ingredient_list')


# class IngredientDetailView(DetailView):
#     model = Ingredient
#     template_name = 'menu/ingredient/ingredient_detail.html'
#     success_url = reverse_lazy('menu:ingredient_list')


# class IngredientDeleteView(DeleteView):
#     model = Ingredient
#     template_name = 'menu/ingredient/ingredient_delete.html'
#     success_url = reverse_lazy('menu:ingredient_list')


# def IngredientSearchView(request):
#     query = request.GET.get('q', '')  # retrieve the search query
#     results = Ingredient.objects.none()  # initialize an empty queryset

#     if query:

#         results = Ingredient.objects.filter(name__icontains=query)

#         return render(request, 'menu/ingredient/ingredient_list.html', {'object_list': results})
#     else:
#         results = Ingredient.objects.none()
