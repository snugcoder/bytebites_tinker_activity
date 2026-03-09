"""
SUMMARY OF CANDIDATE CLASSES

1. **Customer**: Represents the users of the ByteBites app, including their profiles, preferences, and interactions with the app.
2. **Transaction**: Represents the transaction details of the customers, including purchase history, payment methods, and transaction status.
3. **MenuItem**: Represents the items available on the ByteBites menu.
4. **FoodItem**: Represents the individual food items available for customers.

"""

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.preferences = {}
        self.purchase_history = []

    def getName(self):
        return self.name
    

    def addPurchase(self, transaction):
        self.transaction_history.append(transaction)
        
    def getTotalSpent(self):
        return total
        
        
        
def test_scaffold():
    # Create a customer
    customer = Customer("John Doe", "john.doe@example.com")
    print(f"Customer created: {customer.name}, {customer.email}")
    
print("Testing scaffold...")
test_scaffold()