from typing import List
from inventory_report.importers import JsonImporter, CsvImporter
from inventory_report.inventory import Inventory
from inventory_report.reports import SimpleReport, CompleteReport


def load_inventory(file_paths: List[str]) -> Inventory:
    inventory = Inventory()
    for path in file_paths:
        if path.endswith(".json"):
            json_data = JsonImporter(path).import_data()
            inventory.add_data(json_data)
        elif path.endswith(".csv"):
            csv_data = CsvImporter(path).import_data()
            inventory.add_data(csv_data)
    return inventory


def create_report(report_type: str, inventory: Inventory) -> str:
    if report_type == "simple":
        report = SimpleReport()
    elif report_type == "complete":
        report = CompleteReport()
    else:
        raise ValueError("Report type is invalid.")
    report.add_inventory(inventory)
    return report.generate()


def process_report_request(file_paths: List[str], report_type: str) -> str:
    inventory = load_inventory(file_paths)
    return create_report(report_type, inventory)
