import os
from dotenv import load_dotenv

load_dotenv()  # load .env directly


class Product:
    def __init__(
        self,
        id: int,
        name: str,
        price: float,
        description: str,
        category_id: int,
    ):
        self.id = id
        self.name = name
        self.base_price = price
        self.description = description
        self.category_id = category_id

        # env variables (used directly)
        self.currency = os.getenv("CURRENCY", "USD")
        self.tax_rate = float(os.getenv("TAX_RATE", 0.0))
        self.price_multiplier = float(os.getenv("PRICE_MULTIPLIER", 1.0))

        self.price = self.calculate_final_price()

    def calculate_final_price(self) -> float:
        price = self.base_price * self.price_multiplier
        tax = price * self.tax_rate
        return round(price + tax, 2)
