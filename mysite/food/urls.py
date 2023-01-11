from django.urls import path

from mysite.food.views import item, create_item, update_item, delete_item, IndexClassView, FoodDetail

urlpatterns = [
    path('', IndexClassView.as_view(), name='index'),
    path('item/', item, name='item'),
    path('<int:pk>/', FoodDetail.as_view(), name='detail'),
    path('add',create_item, name= 'create_item'),
    path('update/<int:item_id>/', update_item, name='update_item'),
    path('delete/<int:item_id>/' ,delete_item, name= 'delete_item'),
]
