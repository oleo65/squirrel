# pylint: disable=import-error

import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from stash.models import User


class UserNode(DjangoObjectType):

    class Meta:
        model = User
        interfaces = (graphene.relay.Node,)
        filter_fields = {
            'first_name': ['icontains',],
            'last_name': ['icontains',],
        }


class UserQuery(graphene.ObjectType):
    users = DjangoFilterConnectionField(UserNode)
