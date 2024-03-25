
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'app'

urlpatterns = [
    # ======================= order=============

    path('create/', views.MenuCreateView.as_view(), name='menu_create'),
    path('list/', views.MenuListView.as_view(), name='menu_list'),
    path('update/<int:pk>',
         views.MenuUpdateView.as_view(), name='menu_update'),
    path('delete/<int:pk>', views.MenuDeleteView.as_view(),
         name='menu_delete'),
    #     path('item/search',
    #          views.ItemSearchView.as_view(), name='item_search'),
    # path('search',
    #      views.SearchView, name='menu_search'),

    # ======================= inventory=============

    path('inventory/create/', views.InventoryCreateView.as_view(),
         name='ingredient_create'),
    path('inventory/list/', views.InventoryListView.as_view(),
         name='ingredient_list'),
    #     path('inventory/update/<int:pk>',
    #          views.InventoryUpdateView.as_view(), name='ingredient_update'),
    #     path('inventory/delete/<int:pk>', views.InventoryDeleteView.as_view(),
    #          name='ingredient_delete'),
    #     path('item/search',
    #          views.ItemSearchView.as_view(), name='item_search'),
    # path('inventory/search',
    #      views.SearchView, name='ingredient_search'),



    # ======================= recipe=============

    path('recipe/create/', views.RecipeRequirementCreateView.as_view(),
         name='recipe_create'),
    path('recipe/list/', views.RecipeRequirementListView.as_view(), name='recipe_list'),
    path('recipe/update/<int:pk>',
         views.RecipeRequirementUpdateView.as_view(), name='recipe_update'),
    #     path('recipe/delete/<int:pk>', views.RecipeDeleteView.as_view(),
    #          name='recipe_delete'),
    #     path('item/search',
    #          views.ItemSearchView.as_view(), name='item_search'),
    # path('recipe/search',
    #      views.SearchView, name='recipe_search'),

    # =======================menu=============

    path('menu/create/', views.OrderCreateView.as_view(), name='menu_create'),
    path('menu/list/', views.OrderListView.as_view(), name='menu_list'),
    path('menu/update/<int:pk>',
         views.OrderUpdateView.as_view(), name='menu_update'),
    #     path('order/delete/<int:pk>', views.OrderDeleteView.as_view(),
    #          name='order_delete'),
    #     path('item/search',
    #     #          views.ItemSearchView.as_view(), name='item_search'),
    #     path('order/search',
    #          views.SearchView, name='order_search'),


]
