from dataclasses import dataclass
from typing import List, Dict, Optional

# --- 1. DOMAIN LAYER (Untouched Information Experts) ---
@dataclass
class Product:
    name: str
    price: float
    tax_rate: float

    def get_price_with_tax(self) -> float:
        return self.price + (self.price * self.tax_rate)

@dataclass
class OrderItem:
    product: Product
    quantity: int

    def get_subtotal(self) -> float:
        return self.product.get_price_with_tax() * self.quantity

class Order:
    def __init__(self, shipping_flat_rate: float = 10.00):
        self.items: List[OrderItem] = []
        self.shipping_flat_rate = shipping_flat_rate

    def add_item(self, product: Product, quantity: int) -> None:
        self.items.append(OrderItem(product, quantity))

    def get_grand_total(self) -> float:
        return sum(item.get_subtotal() for item in self.items) + self.shipping_flat_rate


# --- 2. CONTROLLER LAYER (The GRASP Controller) ---
class ShoppingSessionController:
    """
    Use-Case Controller: Coordinates the 'Shopping & Checkout' workflow.
    It separates the UI/API from the internal Domain Model.
    """
    def __init__(self, product_catalog: Dict[str, Product]):
        self.catalog = product_catalog
        self.current_order: Optional[Order] = None

    # System Event: User opens the checkout screen
    def start_new_session(self) -> None:
        self.current_order = Order(shipping_flat_rate=15.00)

    # System Event: User clicks "Add to Cart" on the web page / UI
    def handle_add_to_cart(self, product_sku: str, quantity: int) -> bool:
        if not self.current_order:
            raise RuntimeError("No active shopping session.")
            
        # 1. Controller coordinates fetching data from infrastructure/catalog
        product = self.catalog.get(product_sku)
        if not product:
            return False  # Product not found
            
        # 2. Controller DELEGATES business logic to the Domain Expert (Order)
        self.current_order.add_item(product, quantity)
        return True

    # System Event: User clicks "Submit Order"
    def handle_checkout(self) -> Dict[str, float]:
        if not self.current_order:
            raise RuntimeError("No active shopping session.")
            
        # Coordinates final calculations, database saving, or payment gateway calls
        total = self.current_order.get_grand_total()
        
        # We return simple data to the UI, never exposing domain objects directly
        return {"status": "SUCCESS", "amount_charged": total}


# --- 3. UI / CLIENT LAYER ---
if __name__ == "__main__":
    # Simulate a database catalog
    fake_db_catalog = {
        "SKU-MAC": Product("MacBook Pro", 2000.00, 0.10),
        "SKU-BOOK": Product("LLD Design Patterns", 50.00, 0.05)
    }

    # The UI only talks to the Controller!
    controller = ShoppingSessionController(fake_db_catalog)
    
    # Simulate User UI actions:
    controller.start_new_session()
    controller.handle_add_to_cart("SKU-MAC", 1)
    controller.handle_add_to_cart("SKU-BOOK", 2)
    
    receipt = controller.handle_checkout()
    print(f"Checkout Status: {receipt['status']} | Total: ${receipt['amount_charged']:.2f}")