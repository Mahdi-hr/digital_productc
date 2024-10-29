from django.urls import path
from .views import (
    ProductListView,ProductDeteailView,CategoryDeteailView,CategoryListView,
    FileListView,FileDetailView
                    )

urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='product-list'),
    path('categories/<int:pk>/', CategoryDeteailView.as_view(), name='product-detail'),

    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDeteailView.as_view(), name='product-detail'),

    path('products/<int:product_pk>/files/', FileListView.as_view(), name='file-list'),
    # مسیر یک فایل خاص از محصول
    path('products/<int:product_pk>/files/<int:pk>/', FileDetailView.as_view(), name='file-detail'),
]