from django.http.response import HttpResponse
from django.views.generic.base import View
from graphql.utils import schema_printer

from .schema import schema


class ApiSchema(View):

    def get(self, request):
        """Returns the current GraphQL Schema definition."""
        schema_json = schema_printer.print_schema(schema)
        return HttpResponse(schema_json, content_type='application/json')
