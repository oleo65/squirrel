from django.http.response import JsonResponse
from django.views.generic.base import View
from graphql.utils import schema_printer

from .schema import schema


class ApiSchema(View):

    def get(self, request):
        """Returns the current GraphQL Schema definition."""
        schema_json = schema_printer.print_schema(schema)
        return JsonResponse(schema_json)
