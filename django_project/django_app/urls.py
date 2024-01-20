from django.urls import path
from django_app import views

urlpatterns = [
    path("", views.home, name="home"),
    path("item_list/", views.home, name="item_list"),
    path("register/", views.register, name="register"),
    path("signin", views.sign_in, name="signin"),
    path("sign_out", views.sign_out, name="sign_out"),
    path("item_list", views.item_list, name="item_list"),
    path("category_list/", views.category_list, name="category_list"),
    path("category_list/<str:slug_name>/", views.items, name="items"),
    path("search/", views.search, name="search"),
    path("item/<str:item_id>/", views.item, name="item"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
    path("chat", views.chat, name="chat"),
    path("chat/<slug:room_slug>/", views.room, name="room"),
]
from django_app import views_a

websocket_urlpatterns = [
    path("ws/chat/<slug:room_name>/", views_a.ChatConsumer.as_asgi())
]
