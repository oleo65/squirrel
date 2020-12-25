# pylint: disable=import-error

import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from stash.models import Product


class ProductNode(DjangoObjectType):

    class Meta:
        model = Product
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'name': ['icontains',],
        }


class ProductQuery(graphene.ObjectType):
    products = DjangoFilterConnectionField(ProductNode)
