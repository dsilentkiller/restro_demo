from django.contrib import admin
from django.urls import path
from inventory import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'inventory'


urlpatterns = [
    path('', views.base, name='base'),
    # ==================inventory=================================
    path('create/', views.InventoryCreateView.as_view(), name='create'),
    path('list/', views.InventoryListView.as_view(), name='inventory_list'),
    path('update/<int:pk>', views.InventoryUpdateView.as_view(), name='update'),
    path('detail/<int:pk>', views.InventoryDetailView.as_view(),
         name='inventory_detail'),
    path('delete/<int:pk>', views.InventoryDeleteView.as_view(),
         name='inventory_delete'),
    path('inventory/search',
         views.InventorySearchView.as_view(), name='inventory_search'),
]
if settings.DEBUG:  # new
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
