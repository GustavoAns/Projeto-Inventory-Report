from inventory_report.inventory.product import Product


def test_cria_produto():
    new_product = Product(
        3,
        "Cadeira",
        "Casa do Código",
        "01/01/2020",
        "01/01/2021",
        "123456789",
        "na cozinha",
    )

    assert new_product.id == 3
    assert new_product.nome_do_produto == "Cadeira"
    assert new_product.nome_da_empresa == "Casa do Código"
    assert new_product.data_de_fabricacao == "01/01/2020"
    assert new_product.data_de_validade == "01/01/2021"
    assert new_product.numero_de_serie == "123456789"
    assert new_product.instrucoes_de_armazenamento == "na cozinha"
