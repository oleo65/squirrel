# pylint: disable=import-error

import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from stash.models import InventoryItem


class InventoryItemNode(DjangoObjectType):

    class Meta:
        model = InventoryItem
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'name': ['icontains',],
            'product': ['exact',],
        }


class InventoryItemQuery(graphene.ObjectType):
    inventory_items = DjangoFilterConnectionField(InventoryItemNode)
