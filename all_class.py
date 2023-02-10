class Account:
    def __init__(self, id, password):
        self.__id = id
        self.__password = password  
        
class Person:
    def __init__(self, prefix, name, surname, email, phone_number):
        self._prefix = prefix
        self._name = name
        self._surname = surname
        self._email = email
        self._phone_number = phone_number

class Customer(Person):
    def __init__(self, prefix, name, surname, email, phone_number, creditcard_info):
        Person.__init__(self, prefix, name, surname, email, phone_number)
        self._creditcard_info = creditcard_info
    
class Admin(Person):
    def __init__(self, prefix, name, surname, email, phone_number, update_hotel):
        Person.__init__(self, prefix, name, surname, email, phone_number) 
        self.__update_hotel= update_hotel

class Report:
    def __init__(self, phone, user, complaint_details):
        self._phone = phone
        self._user = user
        self._complaint_details = complaint_details

class Hotel():
    def __init__(self):
        self._name_hotel = []
        self._rating = []
        self._number_room = []
        self._hotel_picture = []
        
class HotelCatalog():
    def __init__(self):
        self.__hotel_list = []

class Room():
    def __init__(self):
        self._room_type = []
        self._price_room = []
        self._facilities_detail = []
        self._bed_type = []
        self._room_picture = []

class RoomStatus():
    def __init__(self):
        self.__room_number = []
        self.__room_status = []

class Addons:
    def __init__(self):
        self.__detail = []
        self.__add_on_list  =[]

class BreakfastService():
    def __init__(self):
        self.__type_food = []
        self.__price_food = []

class SpaService:
    def __init__(self):
        self.__resrve_spa = []
        self.__price_service = []

class ActivityService:
    def __init__(self):
        self.__data_activity = []
        self.__price_activity = []
        self.__num_person = []

class TaxiService:
    def __init__(self):
        self.__number_taxi = []
        self.__fees_taxi = []
        self.__contact_taxi = []

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

class TypeCoupon:
    def __init__(self, value_coupon, pr, coupon_description):
        self._value_coupon = value_coupon
        self._pr=pr
        self._coupon_description=coupon_description

class DiscountNumRoom:
    def __init__(self, num_room_discount, value_discount):
        self.__num_room_discount = num_room_discount
        self.__value_discount = value_discount