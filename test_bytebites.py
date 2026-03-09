import unittest
from models import Customer, FoodItem, Menu, Transaction

class TestTransactionLogic(unittest.TestCase):
    """Test Transaction calculation logic - Happy Path"""
    
    def setUp(self):
        """Set up test data"""
        self.customer = Customer("C001", "Alice")
        self.burger = FoodItem("F001", "Spicy Burger", 10.00, "Entrees", 4.5)
        self.soda = FoodItem("F002", "Large Soda", 5.00, "Drinks", 4.0)
    
    def test_calculate_total_with_multiple_items(self):
        """Test: $10 burger + $5 soda = $15 total"""
        transaction = Transaction("T001", self.customer)
        transaction.addItem(self.burger)
        transaction.addItem(self.soda)
        
        self.assertEqual(transaction.getTotalCost(), 15.00)
    
    def test_order_total_is_zero_when_empty(self):
        """Test: empty transaction total equals $0"""
        transaction = Transaction("T001", self.customer)
        self.assertEqual(transaction.getTotalCost(), 0)


class TestFoodItemValidation(unittest.TestCase):
    """Test FoodItem validation logic - Edge Cases"""
    
    def test_invalid_popularity_rating_too_high(self):
        """Test: popularityRating above 5 raises ValueError"""
        with self.assertRaises(ValueError):
            FoodItem("F003", "Chocolate Cake", 5.99, "Desserts", 6.0)
    
    def test_invalid_popularity_rating_negative(self):
        """Test: negative popularityRating raises ValueError"""
        with self.assertRaises(ValueError):
            FoodItem("F004", "Vanilla Ice Cream", 4.99, "Desserts", -1)


class TestMenuFiltering(unittest.TestCase):
    """Test Menu filtering by category"""
    
    def setUp(self):
        """Set up test menu with items"""
        self.menu = Menu()
        self.burger = FoodItem("F001", "Spicy Burger", 10.00, "Entrees", 4.5)
        self.soda = FoodItem("F002", "Large Soda", 5.00, "Drinks", 4.0)
        self.cake = FoodItem("F003", "Chocolate Cake", 5.99, "Desserts", 4.8)
    
    def test_filter_menu_by_category_drinks(self):
        """Test: filtering menu returns only Drinks category"""
        self.menu.addItem(self.burger)
        self.menu.addItem(self.soda)
        self.menu.addItem(self.cake)
        
        drinks = self.menu.filterByCategory("Drinks")
        
        self.assertEqual(len(drinks), 1)
        self.assertEqual(drinks[0].getName(), "Large Soda")
    
    def test_filter_menu_by_category_desserts(self):
        """Test: filtering menu returns only Desserts category"""
        self.menu.addItem(self.burger)
        self.menu.addItem(self.soda)
        self.menu.addItem(self.cake)
        
        desserts = self.menu.filterByCategory("Desserts")
        
        self.assertEqual(len(desserts), 1)
        self.assertEqual(desserts[0].getName(), "Chocolate Cake")
    
    def test_filter_menu_by_category_entrees(self):
        """Test: filtering menu returns only Entrees category"""
        self.menu.addItem(self.burger)
        self.menu.addItem(self.soda)
        self.menu.addItem(self.cake)
        
        entrees = self.menu.filterByCategory("Entrees")
        
        self.assertEqual(len(entrees), 1)
        self.assertEqual(entrees[0].getName(), "Spicy Burger")


if __name__ == "__main__":
    unittest.main()