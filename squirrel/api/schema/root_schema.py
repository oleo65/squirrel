import graphene
from .transaction import TransactionQuery


class Query(TransactionQuery, graphene.ObjectType):
    version = graphene.String(default_value="v0.1.0")


schema = graphene.Schema(query=Query)
