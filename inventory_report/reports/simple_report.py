from datetime import datetime
from collections import Counter


class SimpleReport:
    # def __init__(self):
    def generate(products_list):
        # data_de_fabricacao_antiga = products_list[0].data_de_fabricacao
        data_fab_list = []
        data_val_list = []
        # today = datetime.today()

        for product in products_list:
            data_fab_list.append(product["data_de_fabricacao"])
            data_val_list.append(product["data_de_validade"])

        data_de_fabricacao_antiga = min(data_fab_list)

        dates = [datetime.strptime(date, "%Y-%m-%d") for date in data_val_list]

        data_de_validade_proxima = datetime(9999, 5, 17)

        # for date in dates:
        #     if date > today and date < data_de_validade_proxima:
        #         data_de_validade_proxima = date

        for date in dates:
            if date < data_de_validade_proxima:
                data_de_validade_proxima = date

        empresas = []

        for product in products_list:
            empresas.append(product["nome_da_empresa"])

        contador = Counter(empresas).most_common(1)

        formated = data_de_validade_proxima.strftime("%Y-%m-%d")

        return (
            f"Data de fabricação mais antiga: {data_de_fabricacao_antiga}\n"
            f"Data de validade mais próxima: {formated}\n"
            f"Empresa com mais produtos: {contador[0][0]}"
        )
