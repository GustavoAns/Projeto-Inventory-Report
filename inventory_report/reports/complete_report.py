from inventory_report.reports.simple_report import SimpleReport
# from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products_list):
        log = super().generate(products_list)
        print(log)
        return (
            f"{log}\n"
            f"Coisas legais"
        )
