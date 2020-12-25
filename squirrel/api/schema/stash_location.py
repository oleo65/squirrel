# pylint: disable=import-error

import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from stash.models import StashLocation


class StashLocationNode(DjangoObjectType):

    class Meta:
        model = StashLocation
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'name': ['icontains',],
        }


class StashLocationQuery(graphene.ObjectType):
    stash_locations = DjangoFilterConnectionField(StashLocationNode)
