from django.shortcuts import render, redirect

products = [

    {"id": 1, "name": "Apple", "price": 40, "image": "images/apple.jpg.jpg", "quantity": 0},
    {"id": 2, "name": "Banana", "price": 20, "image": "images/banana.jpg.jpeg", "quantity": 0},
    {"id": 3, "name": "Mango", "price": 60, "image": "images/mango.jpg.jpeg", "quantity": 0},
    {"id": 4, "name": "Orange", "price": 35, "image": "images/orange.jpg.jpeg", "quantity": 0},
    {"id": 5, "name": "Grapes", "price": 50, "image": "images/Grapes.jpg.jpeg", "quantity": 0},

    {"id": 6, "name": "Vanilla Ice Cream", "price": 100, "image": "images/vanilla.jpg.jpeg", "quantity": 0},
    {"id": 7, "name": "Chocolate Ice Cream", "price": 110, "image": "images/chocolate.jpg.jpeg", "quantity": 0},
    {"id": 8, "name": "Strawberry Ice Cream", "price": 105, "image": "images/strawberry.jpg.jpeg", "quantity": 0},
    {"id": 9, "name": "Kulfi", "price": 90, "image": "images/kulfi.jpg.jpeg", "quantity": 0},
    {"id": 10, "name": "Cone Ice Cream", "price": 85, "image": "images/cone.jpg.jpeg", "quantity": 0},
]
def home(request):
    total = 0
    for product in products:
        product["subtotal"] = product["price"] * product["quantity"]
        total += product["subtotal"]

    return render(request, "home.html", {"products": products, "total": total})


def add_to_cart(request, product_id):
    for product in products:
        if product["id"] == product_id:
            product["quantity"] += 1
    return redirect("home")


def remove_from_cart(request, product_id):
    for product in products:
        if product["id"] == product_id and product["quantity"] > 0:
            product["quantity"] -= 1
    return redirect("home")


def checkout(request):
    return render(request, "checkout.html")