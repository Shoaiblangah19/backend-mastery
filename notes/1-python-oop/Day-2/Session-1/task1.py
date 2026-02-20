'''
### ⚡ Micro Task 1 (7 min)

Create a `Product` class with name, price, and stock quantity. Write these methods in the correct category:

**Modifiers:**
- Restock (add to stock quantity)
- Sell (reduce stock, but only if enough available — raise error otherwise)
- Apply discount (reduce price by percentage)

**Accessors:**
- Get formatted price (return string like `"$29.99"`)
- Get stock status (return `"In Stock"`, `"Low Stock"` if under 5, or `"Out of Stock"`)

**Validators:**
- Is available (True if stock > 0)
- Is affordable (takes a budget amount, returns True if price is within budget)

Create a product. Restock it, sell some, check status. Try to sell more than available — verify it raises an error.
'''
class Product:
    def __init__(self, name: str, price: float, stock: int):
        self.name = name
        self.price = price
        self.stock = stock
    
    def restock(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Restock quantity must be positive")
        self.stock += quantity
    
    def sell(self, quantity: int) -> None:
        if quantity <= 0:
            raise ValueError("Sell quantity must be positive")
        if quantity > self.stock:
            raise ValueError("Insufficient stock")
        self.stock -= quantity
    
    def apply_discount(self, percent: float) -> None:
        if percent < 0 or percent > 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        self.price = self.price * (1 - percent / 100)
    
    def formatted_price(self) -> str:
        return f"${self.price:.2f}"
    
    def stock_status(self) -> str:
        if self.stock == 0:
            return "Out of Stock"
        elif self.stock < 5:
            return "Low Stock"
        else:
            return "In Stock"
    
    def is_available(self) -> bool:
        return self.stock > 0
    
    def is_affordable(self, budget: float) -> bool:
        return self.price <= budget

# Test the Product class
if __name__ == "__main__":
    # Create a product
    laptop = Product("Laptop", 999.99, 3)
    
    # Restock the product
    laptop.restock(7)  # Stock becomes 10
    
    # Sell some items
    laptop.sell(4)  # Stock becomes 6
    print(laptop.stock_status())  # Should print "In Stock"
    
    # Apply discount
    laptop.apply_discount(10)  # Price becomes 899.991
    print(laptop.formatted_price())  # Should print "$899.99"
    
    # Check affordability
    print(laptop.is_affordable(900))  # Should print True
    print(laptop.is_affordable(800))  # Should print False
    
    # Try to sell more than available
    try:
        laptop.sell(10)
    except ValueError as e:
        print(f"Error: {e}")  # Should print "Error: Insufficient stock"