
from django.urls import path
from order import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'order'

urlpatterns = [
    # ======================= table=============

    path('table/create/', views.TableCreateView.as_view(), name='table_create'),
    path('table/list/', views.TableListView.as_view(), name='table_list'),
    path('table/update/<int:pk>',
         views.TableUpdateView.as_view(), name='table_update'),
    path('table/delete/<int:pk>', views.TableDeleteView.as_view(),
         name='table_delete'),
    #     path('item/search',
    #          views.ItemSearchView.as_view(), name='item_search'),
    path('table/search',
         views.SearchView, name='table_search'),

    # ==================inventory=================================
    # path('create/', views.InventoryCreateView.as_view(), name='create'),
    # path('list/', views.InventoryListView.as_view(), name='inventory_list'),
    # path('update/<int:pk>', views.InventoryUpdateView.as_view(), name='update'),
    # path('detail/<int:pk>', views.InventoryDetailView.as_view(),
    #      name='inventory_detail'),
    # path('delete/<int:pk>', views.InventoryDeleteView.as_view(),
    #      name='inventory_delete'),
    # path('inventory/search',
    #      views.InventorySearchView.as_view(), name='inventory_search'),
    # =========================item==================
    # path('item/create/', views.ItemCreateView.as_view(), name='item_create'),
    # path('item/list/', views.ItemListView.as_view(), name='item_list'),
    # path('item/update/<int:pk>', views.ItemUpdateView.as_view(), name='item_update'),
    # path('item/detail/<int:pk>', views.ItemDetailView.as_view(), name='item_detail'),
    # path('item/delete/<int:pk>', views.ItemDeleteView.as_view(),
    #      name='item_delete'),
    # #     path('item/search',
    # #          views.ItemSearchView.as_view(), name='item_search'),
    # path('item/search',
    #      views.SearchView, name='item_search'),




    # ===================  order================================
    path('list/', views.OrderListView.as_view(), name='order_list'),
    path('create/',
         views.OrderCreateView.as_view(), name='order_create'),

    path('update/<int:pk>',
         views.OrderUpdateView.as_view(), name='order_update'),
    path('detail/<int:pk>',
         views.OrderListView.as_view(), name='order_detail'),
    path('cancel/<int:pk>',
         views.OrderCancelView.as_view(), name='order_cancel'),
    path('search/',
         views.OrderListView.as_view(), name='order_search'),

    path('create/login', views.LoginView.as_view(), name='user_login'),





    # =================================  purchase===============================
    # path('purchase/list/', views.PurchaseListView.as_view(), name='purchase_index'),
    # path('purchase/create/',
    #      views.PurchaseCreateView.as_view(), name='purchase_create'),

    # path('purchase/update/',
    #      views.PurchaseUpdateView.as_view(), name='purchase_update'),
    # path('purchase/detail/', views.PurchaseListView.as_view(),
    #      name='purchase_detail'),
    # path('purchase/search', views.PurchaseSearchView, name='purchase_search'),

    # ================================stock report ===================
    #     path('stock/report', views.StockReportListView.as_view(),
    #          name='stock_report'),
    #     path('stock/search', views.StockReportSearchView,
    #          name='stock_search'),


]
