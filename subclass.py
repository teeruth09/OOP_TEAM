class Booking:
    def __init__(self, check_in, check_out, price, location, country, creditcard_info):
        self._check_in=check_in
        self._check_out=check_out
        self._price=price
        self._location=location
        self._country=country
        self._creditcard_info=creditcard_info

class Order:
    def __init__(self, check_in, check_out, price, location, country, creditcard_info, update_booking, status_payment):
        Booking.__init__(self, check_in, check_out, price, location, country, creditcard_info)
        self.__update_booking = update_booking
        self.__status_payment = status_payment
        
class History:
    def __init__(self, status_payment, update_reserve):
        self.__update_reserve=update_reserve
        self.__status_payment=status_payment

class Payment:
    def __init__(self, total, transaction_id, payment_method, card_number, card_name, card_expire, cvv_card, vat):
        self.__total=total
        self.__transaction_id = transaction_id
        self.__payment_method = payment_method
        self.__card_number = card_number
        self.__card_name = card_name
        self.__card_expire = card_expire
        self.__cvv_card = cvv_card
        self.__vat = vat

class Promotion:
    def __init__(self, typecoupon, discountnumroom):
        self.__total_coupon= typecoupon #list of Typecoupon
        self.__total_discount_num_room_list = discountnumroom #list of discountnumroo 

class Typecoupon:
    def __init__(self, value_coupon, pr, coupon_description):
        self._value_coupon = value_coupon
        self._pr=pr
        self._coupon_description=coupon_description

class Discountnumroom:
    def __init__(self, num_room_discount, value_discount):
        self.__num_room_discount = num_room_discount
        self.__value_discount = value_discount
    