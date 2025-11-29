
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('trash',views.trash,name='trash'),
    path('complete',views.complete,name='complete'),
    path('delete_/<int:pk>',views.delete_,name='delete_'),
    path('update/<int:pk>',views.update,name='update'),
    
    path('p_delete/<int:pk>',views.p_delete,name='p_delete'),#new

    path('restore/<int:pk>',views.restore,name='restore'),#new

    path('restore_all',views.restore_all,name='restore_all'),#new

    path('clear_all',views.clear_all,name='clear_all'),#new



]