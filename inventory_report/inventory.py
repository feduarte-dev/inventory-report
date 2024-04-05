from inventory_report.product import Product


class Inventory:
    def __init__(self, data: list[Product] = []) -> None:
        self.data = data

    def add_data(self, products_list: list[Product]):
        for product in products_list:
            self.data.append(product)
