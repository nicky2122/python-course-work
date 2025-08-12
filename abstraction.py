from abc import ABC,abstractmethod
class upload(ABC):
    @abstractmethod
    def compress(self):
        pass
class Image(upload):
    def compress(self):
        print("Image is compressed to 2mb")
class Reel(upload):
    def compress(self):
        print("Reel is compressed to 4mb")
r=Reel()
i=Image()
r.compress()
i.compress()  


from abc import ABC,abstractmethod
class Order(ABC):
    @abstractmethod
    def process_order(self):
        pass
class FoodOder(Order):
    def process_order(self):
        print("processing Food Oder: check chef availability, estimate time,")
class GroceryOrder(Order):
    def process_order(self):
        print("processing Grocery Oder: check inventory per item, bag &dispat" ) 
class MedicineOrder(Order):
    def process_order(self):
        print("") 
class CloudkitchenOrder(Order):
    def process_order(self):
        print("processing CloudkitchenOrder: ")
class TiffinOrder(Order):
    def process_order(self):
        print("processing Tiffin Order:")                
class PetsuppliesOrder(Order):
    def process_order(self):
        print("processing Pet Supplies Order: check pet product categories and")
class MetaOrder(Order):
    def process_order(self):
        print("processing Meta/Seafood Oder: confirm freshness,assign chilled")
class CakeOrder(Order):
    def process_order(self):
        print("processing Cake Order:Custom baking, time-senstive packaing.")
class PartyOrder(Order):
    def process_order(self):
        print("processing party order: Bulk cooking,team coordination,special")
class JuiceOrder(Order):
    def process_order(self):
        print("processing Fresh Juice Order: Immediate prep, cold packaging.")
def handle_order(order: Order):
    order.process_order()
orders=[FoodOder(),GroceryOrder(),MedicineOrder(),CloudkitchenOrder(),TiffinOrder(),PetsuppliesOrder(),MetaOrder(),
        CakeOrder(),PartyOrder(),JuiceOrder()]
for order in orders:
    handle_order(order)                                                                    



from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def make_Payment(self,amount):
        pass
class CreditCardPayment(Payment):
    def make_Payment(self,amount):
        print(f"paid $ {amount} using Credit Card")
class PayPalPayment(Payment):
    def make_Payment(self, amount):
        print(f"paid $ {amount} using Via PayPal")
def Process_Payment(Payment, amount):
    Payment.make_Payment(amount)
Process_Payment(CreditCardPayment(),100)
Process_Payment(PayPalPayment(),200)                    