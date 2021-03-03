from django import template

register = template.Library()


@register.filter(name='is_in_cart')
def is_in_cart(product, cart):
    keys = cart.keys()
    print(product, cart)
    for id in keys:
        if int(id) == product.id:
            return True
    return False


@register.filter(name='cart_count')
def cart_count(product, cart):
    keys = cart.keys()
    print(product, cart)
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)
    return 0


@register.filter(name='cart_price_per_product')
def cart_price_per_product(product, cart):
    return product.price * cart_count(product,cart)
    


@register.filter(name='total_cart_price')
def total_cart_price(products, cart):
    sum=0
    for p in products:
        sum+= cart_price_per_product(p,cart)
    return sum