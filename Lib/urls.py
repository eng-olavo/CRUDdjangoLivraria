from django.urls import path
from Lib import views

urlpatterns=[
    path('getLivraria',views.LibList, name='listagem'),
    path('postLivraria',views.LibPost, name='envio'),
    path('putLivraria/<str:pk>/',views.LibPut, name='atualizar'),
    path('deleteLivraria/<str:pk>',views.LibDelete, name='deletar'),


]