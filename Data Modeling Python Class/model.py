from enum import Enum
from typing import List

class User:
    """Class representing a user."""
    
    def __init__(self, name: str, email: str, password: str):
        self.name = name
        self.email = email
        self.password = password
        
class ProductCategory(Enum):
    """Enumeration for product categories."""
    APPAREL = 'Apparel'
    ACCESSORIES = 'Accessories'
    HOME = 'Home'
    TECH = 'Tech'
    BEAUTY = 'Beauty'
    FOOD = 'Food'
    OTHERS = 'Others'


class Product:
    """Class representing a product."""

    def __init__(self, title: str, description: str, price: float,
                 available_date: str, stock_quantity: int,
                 images: List[str], category: ProductCategory):
        self.title = title
        self.description = description
        self.price = price
        self.available_date = available_date
        self.stock_quantity = stock_quantity
        self.images = images
        self.category = category

class CustomizedProduct(Product):
    """Class representing a customized product."""

    def __init__(self, title, description, price, available_date, stock_quantity, images, attributes=None, brand=None):
        super().__init__(title, description, price, available_date, stock_quantity, images, attributes)
        self.brand = brand

class PromotionalProduct:
    """Class representing a promotional product."""

    def __init__(self, customized_product, customization_options=None):
        self.base_product = customized_product

class MicroStore:
    """Class representing a MicroStore."""

    def __init__(self, name: str, user: str, promotional_products: List[PromotionalProduct]):
        self.name = name
        self.user = user
        self.promotional_products = promotional_products


class Storefront:
    """Class representing a Storefront."""

    def __init__(self, name: str, user: str, products: List[CustomizedProduct]):
        self.name = name
        self.user = user
        self.products = products


class ProductFilter(Enum):
    """Enumeration for product filters."""
    CATEGORY = 'category'
    NEWEST = 'newest'
    OLDEST = 'oldest'
    IN_STOCK = 'in_stock'
    OUT_OF_STOCK = 'out_of_stock'


class ProductListingPage:
    """Class representing a product listing page."""

    def __init__(self, products: List[CustomizedProduct]):
        self.products = products

    def filter_by(self, filter_type: ProductFilter) -> List[CustomizedProduct]:
        """Filter products by filter type."""
        if filter_type == ProductFilter.CATEGORY:
            return [product for product in self.products if product.category == filter_type.value]
        elif filter_type == ProductFilter.NEWEST:
            return sorted(self.products, key=lambda product: product.available_date, reverse=True)
        elif filter_type == ProductFilter.OLDEST:
            return sorted(self.products, key=lambda product: product.available_date)
        elif filter_type == ProductFilter.IN_STOCK:
            return [product for product in self.products if product.stock_quantity > 0]
        elif filter_type == ProductFilter.OUT_OF_STOCK:
            return [product for product in self.products if product.stock_quantity == 0]
        else:
            raise ValueError(f"Invalid product filter type: {filter_type}")
