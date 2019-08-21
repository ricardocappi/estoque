from django.urls import path
from projeto.produto import views as v

app_core = 'produto'

urlpatterns = [
    path('', v.produto_list, name='produto_list'),
]

