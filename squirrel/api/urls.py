from django.urls import path
from graphene_django.views import GraphQLView

from .views import ApiSchema

urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True)),
    path('graphql/schema', ApiSchema.as_view()),
]
