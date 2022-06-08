from inventory_report.inventory.product import Product


def test_relatorio_produto():
    new_product = Product(
        1,
        "Cadeira",
        "Casa do Código",
        "01/01/2020",
        "01/01/2021",
        "123456789",
        "na cozinha",
    )

    message = "O produto Cadeira fabricado em 01/01/2020 por Casa do Código " \
        "com validade até 01/01/2021 precisa ser armazenado na cozinha."

    assert str(new_product) == message
