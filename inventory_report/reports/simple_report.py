from datetime import datetime, date
from collections import Counter

from inventory_report.reports import Report
from inventory_report.inventory import Inventory

# from inventory_report.importers import JsonImporter


class SimpleReport(Report):
    stocks = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.stocks.append(inventory)

    def aux_find_stocks_values(self):
        for inventory in self.stocks:
            manufacturing_dates = [
                datetime.strptime(
                    product.manufacturing_date, "%Y-%m-%d"
                ).date()
                for product in inventory.data
            ]

            expiration_dates = [
                datetime.strptime(product.expiration_date, "%Y-%m-%d").date()
                for product in inventory.data
            ]

            filtered_dates = [
                product_date
                for product_date in expiration_dates
                if product_date >= date.today()
            ]

            oldest = min(manufacturing_dates)
            youngest = min(filtered_dates)

            companies_counter = Counter(
                [product.company_name for product in inventory.data]
            )
            largest_inventory_company = companies_counter.most_common(1)[0][0]

            return {
                "oldest": oldest,
                "youngest": youngest,
                "company": largest_inventory_company,
            }

    def generate(self) -> str:
        data = self.aux_find_stocks_values()
        return (
            f"Oldest manufacturing date: {data['oldest']}\n"
            f"Closest expiration date: {data['youngest']}\n"
            f"Company with the largest inventory: {data['company']}"
        )


# DATA = "inventory_report/data/inventory.json"
# json_importer = JsonImporter(DATA)
# products = json_importer.import_data()
# inventorio = Inventory(products)
# report = SimpleReport()
# report.add_inventory(inventorio)
# print(report.generate())
