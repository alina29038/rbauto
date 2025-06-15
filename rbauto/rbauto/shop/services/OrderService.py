from shop.models import Order, Product

class OrderService:
    def createOrder(data, product_id, user=None):
        order = Order()
        order.contact_name = data.get("contact_name")
        order.contact_phone = data.get("contact_phone")
        order.contact_email = data.get("contact_email")
        product = Product.objects.get(pk=product_id)
        order.product = product
        order.order_type = "order"
        order.order_status = "opened"
        order.owner = user
        order.save()

    def getUserOrders(user):
        return Order.objects.filter(owner=user)