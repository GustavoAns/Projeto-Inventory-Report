import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @classmethod
    def import_data(cls, path):
        list_path = path.split(".")
        file_type = list_path[-1]
        if file_type == "json":
            with open(path) as file:
                return json.load(file)
        else:
            raise ValueError("Arquivo inválido")
