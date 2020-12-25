# pylint: disable=import-error

import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from stash.models import ProductGroup


class ProductGroupNode(DjangoObjectType):

    class Meta:
        model = ProductGroup
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'name': ['icontains',],
        }


class ProductGroupQuery(graphene.ObjectType):
    product_groups = DjangoFilterConnectionField(ProductGroupNode)
