from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.ProductionHome, name='home-production'),
    path('new/<int:id>', views.CreateProduction, name='create-production'),
    path('<int:id>/edit', views.EditProduction, name='edit-production'),
    path('<int:id>/increment', views.ProductionMaterialIncrement, name='increment'),
    path('<int:id>/decrement', views.ProductionMaterialDecrement, name='decrement'),
    path('<int:id>/detail', views.DetailProduction, name='detail-production'),
    path('<int:id>/filter', views.ProductionStockFilter, name='production-filter'),
    path('<int:id>/stockin', views.ProductionStockIn, name='stockin'),
    path('comments/<int:id>', views.ProductionComments, name='comments'),
    path('status/<int:id>', views.ProductionStatus, name='status'),
    path('order/', views.HomeOrders, name='home-orders'),
    path('order/create', views.CreateOrder, name='create-order'),
    path('order/edit/<int:id>', views.EditOrder, name='edit-order'),
    path('order/detail/<int:id>', views.DetailOrder, name='detail-order'),
    path('order/search', views.SearchOrder.as_view(), name='search-order')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
