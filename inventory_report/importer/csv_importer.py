from csv import DictReader
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        list_path = path.split(".")
        file_type = list_path[-1]
        if file_type == "csv":
            with open(path, encoding="utf-8") as file:
                listProds = DictReader(file)
                return [row for row in listProds]
        else:
            raise ValueError("Arquivo inválido")
