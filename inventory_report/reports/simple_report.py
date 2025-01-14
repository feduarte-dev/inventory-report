from datetime import datetime, date
from collections import Counter

from .report import Report
from inventory_report.inventory import Inventory


class SimpleReport(Report):
    def __init__(self) -> None:
        super().__init__()
        self.stocks = []

    def add_inventory(self, inventory: Inventory) -> None:
        self.stocks.append(inventory)

    def aux_find_stocks_values(self):
        companies_list = []
        lista_de_produtos = []
        for inventory in self.stocks:
            lista_de_produtos.extend(inventory.data)

        manufacturing_dates = [
            datetime.strptime(product.manufacturing_date, "%Y-%m-%d").date()
            for product in lista_de_produtos
        ]
        expiration_dates = [
            datetime.strptime(product.expiration_date, "%Y-%m-%d").date()
            for product in lista_de_produtos
        ]

        filtered_dates = [
            product_date
            for product_date in expiration_dates
            if product_date >= date.today()
        ]

        oldest = min(manufacturing_dates)
        youngest = min(filtered_dates)

        companies_counter = Counter(
            [product.company_name for product in lista_de_produtos]
        )
        largest_inventory_company = companies_counter.most_common(1)[0][0]

        for company in companies_counter:
            companies_list.append(f"- {company}: {companies_counter[company]}")

        return {
            "oldest": oldest,
            "youngest": youngest,
            "company": largest_inventory_company,
            "companies_list": "\n".join(companies_list),
        }

    def generate(self) -> str:
        data = self.aux_find_stocks_values()
        return (
            f"Oldest manufacturing date: {data['oldest']}\n"
            f"Closest expiration date: {data['youngest']}\n"
            f"Company with the largest inventory: {data['company']}\n"
        )
