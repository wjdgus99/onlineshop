from coupon.models import Coupon


def __init__(self, request):
    self.sessoin = request.session`
    cart = self.session.get(settings.CART_ID)
    if not cart:
        cart self.session[settings.CART_ID] = {}
    self.cart = cart
    self.coupon_id = self.session.get('coupon_id')


def clear(self):
    self.session[settings.CART_ID] = {}
    self.session['coupon_id'] = None
    self.sessiont.modified = True

@property
def coupon(self):
    if self.coupon_id:
        return Coupon.objects.get(id=self.coupon_id)
    return None


def get_discount_total(self):
    if self.coupon:
        if self.get_product_total() >= self.coupon.amout:
            return self.coupon.amount
    return Decimal(0)


def get_total_price(self):
    return self.get_product_total() - self.get_discount_total()
