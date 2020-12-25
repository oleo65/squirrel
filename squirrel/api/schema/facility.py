# pylint: disable=import-error

import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from stash.models import Facility


class FacilityNode(DjangoObjectType):

    class Meta:
        model = Facility
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'name': ['icontains',],
        }


class FacilityQuery(graphene.ObjectType):
    facilities = DjangoFilterConnectionField(FacilityNode)
