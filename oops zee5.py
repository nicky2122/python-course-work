from abc import ABC,abstractmethod
#---------------encapsulation---------------
class movie:
    def __init__(self,title,genre,duration):
        self.title=title
        self.genre=genre
        self.duration=duration
    def get_details(self):
        return f"{self.title}|genre{self.genre}|{self.duration}"

    def set_duration(self,ne_duration):
        if new_duration>0:
            self.new_duratuion=new_duration
        else:
            raise ValueError("duration must be positive")
#------------inheritance-----------
class user:
    def __init__(self,username,email):
        self.usename=username
        self.email=email 
    def user_type(self):
        return "basic zee5 user"
class freeuser:
    def __init__(self,username,email):
        super(). __init__(username , email)
        self.ads_enabled=True
    def user_type(self):
        return "freeuser - ads enabled"    
class premiumuser:
    def __init__(self,username,email):
        super().__init__(username,email)
        self.ads_enabled=False
        self.download_enbled=True
    def user_type(self):
        return "premiumuser -ads enabled - download enabled"
class familyuser(premiumuser):
    def __init__(self,username,email,gamily_member):
        super().__init__(username,email)
        self.family_member=family_member
    def user_type(self):
        return "familyuser - {self.family_member}member"
#---------abstract----------
class paymentmethod(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass
class creditcardpayment(paymentmethod):
        def process_payment(self,amount):
            return f"processing {amount} via credit card"
class upipayment(paymentmethod):
    def __init__(self,amount):
        return f"processing{amount} via upi"
class netbankingpayment(paymentmethod):
    def __init__(self,amount):
        return f"processing{amount} via netbanking"
#---------polymorphism------------
def process_user_payment(payment_obj,amount):
    print(payment_obj.process_payment(amount))

#----------menu drive ZEE5 simulation---------
if __name__ == "__main__":
    # Sample data
    movie1 = movie("RRR", "Action", 180)
    movie2 = movie("Kantara", "Drama", 150)
    movie3 = movie("KGF Chapter 2", "Action", 170)

    user1 = freeuser("nikhitha", "nikhi@example.com")
    user2 = premiumuser("arjun", "arjun@example.com")
    user3 = familyuser("megha", "megha@example.com", 4)

    while True:
        print("\n===== ZEE5 OOP Demo =====")
        print("1. View Movie List (Encapsulation)")
        print("2. View User Types (Inheritance)")
        print("3. Process Payment (Abstract + Polymorphism)")
        print("4. Update Movie Duration (Encapsulation Setter)")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Movie List ---")
            print(movie1.get_details())
            print(movie2.get_details())
            print(movie3.get_details())

        elif choice == "2":
            print(f"{user1.username} is a {user1.user_type()}")
            print(f"{user2.username} is a {user2.user_type()}")
            print(f"{user3.username} is a {user3.user_type()}")

        elif choice == "3":
            print("\nSelect Payment Method:")
            print("1. Credit Card")
            print("2. UPI")
            print("3. Net Banking")
            method = input("Enter method: ")
            amount = int(input("Enter amount: ₹"))
            if method == "1":
                process_user_payment(CreditCardPayment(), amount)
            elif method == "2":
                process_user_payment(UpiPayment(), amount)
            elif method == "3":
                process_user_payment(NetBankingPayment(), amount)
            else:
                print("Invalid payment method")

        elif choice == "4":
            print("\nWhich movie to update?")
            print("1. RRR")
            print("2. Kantara")
            print("3. KGF Chapter 2")
            movie_choice = input("Enter choice: ")
            new_duration = int(input("Enter new duration (min): "))
            try:
                if movie_choice == "1":
                    movie1.set_duration(new_duration)
                elif movie_choice == "2":
                    movie2.set_duration(new_duration)
                elif movie_choice == "3":
                    movie3.set_duration(new_duration)
                print("Duration updated successfully!")
            except ValueError as e:
                print("Error:", e)

        elif choice == "5":
            print("Exiting ZEE5 OOP Demo. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


        




