from inventory_report.product import Product


def test_product_report(capsys) -> None:
    product = Product(
        "1",
        "Leite",
        "Parmalat",
        "10/01/2024",
        "10/02/2024",
        "1821318274",
        "Guardar em lugar ventilado e longe do sol",
    )

    print(product)
    captured = capsys.readouterr()

    assert captured.out == (
        "The product 1 - Leite with serial number 1821318274"
        " manufactured on 10/01/2024 by the company Parmalat"
        " valid until 10/02/2024 must be stored according to"
        " the following instructions: Guardar em lugar ventilado"
        " e longe do sol.\n"
    )
