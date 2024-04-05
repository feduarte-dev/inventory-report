from .simple_report import SimpleReport


class CompleteReport(SimpleReport):
    def generate(self) -> str:
        data = super().aux_find_stocks_values()
        complete_report = super().generate()
        complete_report += "Stocked products by company:\n"
        complete_report += f"{data['companies_list']}\n"

        return complete_report
