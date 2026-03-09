"""
SUMMARY OF CANDIDATE CLASSES

1. **Customer**: Represents the users of the ByteBites app, including their profiles, preferences, and interactions with the app.
2. **Transaction**: Represents the transaction details of the customers, including purchase history, payment methods, and transaction status.
3. **MenuItem**: Represents the items available on the ByteBites menu.
4. **FoodItem**: Represents the individual food items available for customers.

"""
'''
CUSTOMER
This method takes in a customerId and name, and initializes a Customer object with an empty purchase history. Customers purchase history is a list of Transaction objects. They can be found by their customerId + name. 

TRANSACTION
This method takes in a transactionId, customer, selectedItems, and timestamp, and initializes a Transaction object. Manages the transcation details of the customers, including purchase history, payment methods, and transaction status.

FOODITEM
This method takes in an itemId, name, price, category, and popularityRating, and initializes a FoodItem object.


'''
class Customer:
    def __init__(self, customerId, name):
        if not customerId or not isinstance(customerId, str):
            raise ValueError("customerId must be a non-empty string")
        if not name or not isinstance(name, str):
            raise ValueError("name must be a non-empty string")
        
        self.customerId = customerId
        self.name = name
        self.purchaseHistory = []

    def getName(self):
        return self.name

    def addPurchase(self, transaction):
        if transaction is None:
            raise ValueError("transaction cannot be None")
        self.purchaseHistory.append(transaction)

    def getPurchaseHistory(self):
        return self.purchaseHistory

    def getTotalSpent(self):
        total = 0
        for transaction in self.purchaseHistory:
            total += transaction.getTotalCost()
        return total
    
class Transaction:
    def __init__(self, transactionId, customer, selectedItems=None, timestamp=None):
        from datetime import datetime
        
        if not transactionId or not isinstance(transactionId, str):
            raise ValueError("transactionId must be a non-empty string")
        if customer is None:
            raise ValueError("customer cannot be None")
        
        self.transactionId = transactionId
        self.customer = customer
        self.selectedItems = selectedItems if selectedItems is not None else []
        self.timestamp = timestamp if timestamp is not None else datetime.now()
        self.totalCost = 0

    def addItem(self, item):
        if item is None:
            raise ValueError("item cannot be None")
        self.selectedItems.append(item)

    def removeItem(self, itemId):
        self.selectedItems = [item for item in self.selectedItems if item.itemId != itemId]

    def getItems(self):
        return self.selectedItems

    def calculateTotal(self):
        total = 0
        for item in self.selectedItems:
            total += item.getPrice()
        return total

    def getTotalCost(self):
        self.totalCost = self.calculateTotal()
        return self.totalCost

    def getCustomer(self):
        return self.customer
    
class Menu:
    def __init__(self):
        self.items = []

    def addItem(self, item):
        if item is None:
            raise ValueError("item cannot be None")
        self.items.append(item)

    def removeItem(self, itemId):
        if not itemId or not isinstance(itemId, str):
            raise ValueError("itemId must be a non-empty string")
        self.items = [item for item in self.items if item.itemId != itemId]

    def getAllItems(self):
        return self.items

    def filterByCategory(self, category):
        if not category or not isinstance(category, str):
            raise ValueError("category must be a non-empty string")
        return [item for item in self.items if item.getCategory() == category]

    def getItemById(self, itemId):
        if not itemId or not isinstance(itemId, str):
            raise ValueError("itemId must be a non-empty string")
        for item in self.items:
            if item.itemId == itemId:
                return item
        return None
    
    
class FoodItem:
    def __init__(self, itemId, name, price, category, popularityRating=0.0):
        if not itemId or not isinstance(itemId, str):
            raise ValueError("itemId must be a non-empty string")
        if not name or not isinstance(name, str):
            raise ValueError("name must be a non-empty string")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("price must be a positive number")
        if not category or not isinstance(category, str):
            raise ValueError("category must be a non-empty string")
        if not isinstance(popularityRating, (int, float)) or popularityRating < 0 or popularityRating > 5:
            raise ValueError("popularityRating must be between 0 and 5")
        
        self.itemId = itemId
        self.name = name
        self.price = price
        self.category = category
        self.popularityRating = popularityRating

    def getName(self):
        return self.name

    def getPrice(self):
        return self.price

    def getCategory(self):
        return self.category

    def getPopularityRating(self):
        return self.popularityRating

    def setPopularityRating(self, rating):
        if not isinstance(rating, (int, float)) or rating < 0 or rating > 5:
            raise ValueError("rating must be between 0 and 5")
        self.popularityRating = rating
        
        
# Test script
if __name__ == "__main__":
    # Create a Menu and add FoodItems
    menu = Menu()
    burger = FoodItem("F001", "Spicy Burger", 12.99, "Entrees", 4.5)
    soda = FoodItem("F002", "Large Soda", 3.50, "Drinks", 4.0)
    cake = FoodItem("F003", "Chocolate Cake", 5.99, "Desserts", 4.8)
    
    menu.addItem(burger)
    menu.addItem(soda)
    menu.addItem(cake)
    
    print("=== Menu Items ===")
    print(f"All items: {len(menu.getAllItems())} items")
    print(f"Drinks: {[item.getName() for item in menu.filterByCategory('Drinks')]}")
    
    # Create a Customer
    customer = Customer("C001", "Alice")
    print(f"\n=== Customer ===")
    print(f"Customer: {customer.getName()}")
    
    # Create a Transaction and add items
    transaction1 = Transaction("T001", customer)
    transaction1.addItem(burger)
    transaction1.addItem(soda)
    
    print(f"\n=== Transaction 1 ===")
    print(f"Items: {[item.getName() for item in transaction1.getItems()]}")
    print(f"Total Cost: ${transaction1.getTotalCost():.2f}")
    
    # Add transaction to customer
    customer.addPurchase(transaction1)
    
    # Create another transaction
    transaction2 = Transaction("T002", customer)
    transaction2.addItem(cake)
    customer.addPurchase(transaction2)
    
    print(f"\n=== Customer Purchase History ===")
    print(f"Total transactions: {len(customer.getPurchaseHistory())}")
    print(f"Total spent: ${customer.getTotalSpent():.2f}")