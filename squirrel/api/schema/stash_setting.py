# pylint: disable=import-error

import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from stash.models import StashSetting


class StashSettingNode(DjangoObjectType):

    class Meta:
        model = StashSetting
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'name': ['icontains',],
        }


class StashSettingQuery(graphene.ObjectType):
    stash_settings = DjangoFilterConnectionField(StashSettingNode)
