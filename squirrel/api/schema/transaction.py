# pylint: disable=import-error

import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from stash.models import Transaction


class TransactionNode(DjangoObjectType):

    class Meta:
        model = Transaction
        interfaces = (graphene.relay.Node,)
        filter_fields = ['user', 'stash_location', 'product']


class TransactionQuery(graphene.ObjectType):
    transactions = DjangoFilterConnectionField(TransactionNode)
