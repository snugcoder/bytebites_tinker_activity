# ByteBites UML Class Diagram

```mermaid
classDiagram
    class Customer {
        -name: String
        -purchaseHistory: Transaction[]
        +getName(): String
        +getPurchaseHistory(): Transaction[]
        +addTransaction(transaction: Transaction): void
    }
    
    class FoodItem {
        -name: String
        -price: double
        -category: String
        -popularityRating: double
        +getName(): String
        +getPrice(): double
        +getCategory(): String
        +getPopularityRating(): double
    }
    
    class Menu {
        -items: FoodItem[]
        +addItem(item: FoodItem): void
        +removeItem(item: FoodItem): void
        +getAllItems(): FoodItem[]
        +filterByCategory(category: String): FoodItem[]
    }
    
    class Transaction {
        -items: FoodItem[]
        -totalCost: double
        +addItem(item: FoodItem): void
        +removeItem(item: FoodItem): void
        +getItems(): FoodItem[]
        +getTotalCost(): double
        +calculateTotal(): void
    }
    
    Customer "1" --> "*" Transaction: has
    Transaction "*" --> "*" FoodItem: contains
    Menu "1" --> "*" FoodItem: manages
```

## Key Relationships

- **Customer → Transaction** (1-to-many): Each customer has multiple transactions in their purchase history
- **Transaction → FoodItem** (many-to-many): Each transaction contains multiple food items
- **Menu → FoodItem** (1-to-many): The menu manages all available food items with filtering capability
