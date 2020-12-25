import graphene
from .transaction import TransactionQuery
from .product import ProductQuery


class Query(ProductQuery, TransactionQuery, graphene.ObjectType):
    version = graphene.String(default_value="v0.1.0")


schema = graphene.Schema(query=Query)
