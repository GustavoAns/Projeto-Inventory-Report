from csv import DictReader
import json
import xmltodict
# from functools import lru_cache
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory():
    # @lru_cache
    @classmethod
    def read_csv(cls, path):
        with open(path, encoding="utf-8") as file:
            listProds = DictReader(file)
            return [row for row in listProds]

    # @lru_cache
    @classmethod
    def read_json(cls, path):
        with open(path) as file:
            return json.load(file)

    # @lru_cache
    @classmethod
    def read_xml(cls, path):
        with open(path) as file:
            return xmltodict.parse(file.read())["dataset"]["record"]

    @classmethod
    def getList(cls, path):
        list_path = path.split(".")
        file_type = list_path[-1]
        if file_type == "csv":
            return cls.read_csv(path)
        elif file_type == "json":
            return cls.read_json(path)
        elif file_type == "xml":
            return cls.read_xml(path)
        else:
            raise Exception("Invalid file type")

    @classmethod
    def import_data(cls, path, return_type):
        listProds = cls.getList(path)

        if return_type == "completo":
            return CompleteReport.generate(listProds)
        elif return_type == "simples":
            return SimpleReport.generate(listProds)
        else:
            raise Exception("Invalid return_type")
