from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products_list):
        log = super().generate(products_list)
        empresas = []
        empresas_quant = ""

        for product in products_list:
            empresas.append(product["nome_da_empresa"])

        contador = Counter(empresas).most_common()

        for empresa, quantidade in contador:
            empresas_quant += f"- {empresa}: {quantidade}\n"

        return (
            f"{log}\n"
            f"Produtos estocados por empresa:\n"
            f"{empresas_quant}"
        )
