from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    data = request.POST
    product_id = data.get("product_id")
    amount = data.get("amount")
    new_product = ProductInBasket.objects.create(session_key=session_key, product_id=product_id, nmb=amount)
    return_dict["products_total_amount"] = amount

    return JsonResponse(return_dict)