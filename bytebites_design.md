# ByteBites UML Class Diagram

```mermaid
classDiagram
    class Customer {
        -customerId: String
        -name: String
        -purchaseHistory: Transaction[]
        +getName() String
        +addPurchase(transaction: Transaction) void
        +getPurchaseHistory() Transaction[]
        +getTotalSpent() double
    }

    class FoodItem {
        -itemId: String
        -name: String
        -price: double
        -category: String
        -popularityRating: double
        +getName() String
        +getPrice() double
        +getCategory() String
        +getPopularityRating() double
        +setPopularityRating(rating: double) void
    }

    class Menu {
        -items: FoodItem[]
        +addItem(item: FoodItem) void
        +removeItem(itemId: String) void
        +getAllItems() FoodItem[]
        +filterByCategory(category: String) FoodItem[]
        +getItemById(itemId: String) FoodItem
    }

    class Transaction {
        -transactionId: String
        -customer: Customer
        -selectedItems: FoodItem[]
        -timestamp: Date
        -totalCost: double
        +addItem(item: FoodItem) void
        +removeItem(itemId: String) void
        +getItems() FoodItem[]
        +calculateTotal() double
        +getTotalCost() double
        +getCustomer() Customer
    }

    Customer "1" --> "many" Transaction : makes
    Transaction "1" --> "many" FoodItem : contains
    Menu "1" --> "many" FoodItem : manages
```

## Class Descriptions

**Customer**: Manages user identity and purchase tracking
- Stores customer ID and name
- Maintains purchase history for user verification
- Provides methods to retrieve transaction history and total spending

**FoodItem**: Represents individual menu items
- Tracks name, price, category, and popularity rating
- Allows popularity rating to be updated dynamically
- Provides access to all item properties

**Menu**: Manages the complete collection of food items
- Stores all available items
- Supports adding and removing items
- Enables filtering by category (e.g., "Drinks", "Desserts")
- Allows lookup by item ID

**Transaction**: Groups selected items into a single purchase
- Links to a customer and their selected items
- Tracks transaction timestamp
- Calculates and stores total cost
- Provides access to transaction details

## Relationships

- **Customer → Transaction** (1 to many): Each customer makes multiple transactions
- **Transaction → FoodItem** (1 to many): Each transaction contains multiple food items
- **Menu → FoodItem** (1 to many): The menu manages all available food items
