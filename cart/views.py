from django.shortcuts import render, get_object_or_404
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView
from profiles.models import Profile
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages


class ItemListView(ListView):
    model = Item
    queryset = Item.objects.all()
    context_object_name = 'items'
    template_name = "cart/item_list.html"


class ItemDetailView(DetailView):
    model = Item
    template_name = "cart/item_detail.html"


def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(
                request, "Cantidad actualizada en el carro de compras.")
        else:
            messages.info(request, "Item agregado al carro de compras.")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item agregado al carro de compras.")
        return redirect("cart:item-detail", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(request, "Item removido del carro de compras.")
            return redirect("cart:item-detail", slug=slug)
        else:
            messages.info(request, "Item no estaba en el carro de compras.")
            return redirect("cart:item-detail", slug=slug)
    else:
        # add message no order here
        messages.info(request, "Aún no tienes orden de compra.")
        return redirect("cart:item-detail", slug=slug)
