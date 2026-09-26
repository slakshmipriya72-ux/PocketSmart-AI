# Simple recommendation module for the PocketMarts AI prototype

def recommend_products(category, products):
    """Return products matching the requested category."""
    return [
        product for product in products
        if product.get("category", "").lower() == category.lower()
    ]

if __name__ == "__main__":
    sample_products = [
        {"name": "Rice", "category": "Grocery"},
        {"name": "Milk", "category": "Dairy"},
        {"name": "Bread", "category": "Bakery"},
    ]
    print(recommend_products("Grocery", sample_products))
