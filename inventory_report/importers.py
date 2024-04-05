from typing import Dict, Type
from abc import ABC, abstractmethod
from inventory_report.product import Product
import json
import csv


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


class CsvImporter(Importer):
    def import_data(self) -> list[Product]:
        result = []
        with open(self.path) as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
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


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
