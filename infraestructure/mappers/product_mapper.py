from domain.model.product_domain import Product_domain
from infraestructure.schema.models_factory import Product


def to_domain_product(db_product: Product) -> Product_domain:
    return Product_domain(
        name=db_product.name,
        price=db_product.price,
        stock=db_product.stock
    )


def to_db_product(domain_product: Product_domain) -> Product:
    return Product(
        id=domain_product.get_id(),
        name=domain_product.get_name(),
        price=domain_product.get_price(),
        stock=domain_product.get_stock()
    )


def to_dict(domain_product: Product_domain) -> dict:
    return {
        "id": domain_product.get_id(),
        "name": domain_product.get_name(),
        "price": domain_product.get_price(),
        "stock": domain_product.get_stock()
    }
