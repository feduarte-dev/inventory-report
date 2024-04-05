from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json


class Importer(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def import_data(self) -> list[Product]:
        raise NotImplementedError


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        result = []
        with open(self.path) as file:
            data = json.load(file)
            for product in data:
                product_obj = Product(
                    product["id"],
                    product["product_name"],
                    product["company_name"],
                    product["manufacturing_date"],
                    product["expiration_date"],
                    product["serial_number"],
                    product["storage_instructions"],
                )
                result.append(product_obj)

        return result


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}

JSON_DATA = "inventory_report/data/inventory.json"

teste = JsonImporter(JSON_DATA)
print(teste.import_data())
