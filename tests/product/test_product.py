from inventory_report.product import Product


def test_create_product() -> None:
    product = Product(
        "1",
        "Leite",
        "Parmalat",
        "10/01/2024",
        "10/02/2024",
        "1821318274",
        "Guardar em lugar ventilado e longe do sol",
    )

    assert product.id == "1"
    assert product.product_name == "Leite"
    assert product.company_name == "Parmalat"
    assert product.manufacturing_date == "10/01/2024"
    assert product.expiration_date == "10/02/2024"
    assert product.serial_number == "1821318274"
    assert (
        product.storage_instructions
        == "Guardar em lugar ventilado e longe do sol"
    )
