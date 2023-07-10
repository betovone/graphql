from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType
    
from ariadne.explorer import ExplorerPlayground

PLAYGROUND_HTML = ExplorerPlayground(title="Cool API").html(None)
import json
from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import JsonResponse, HttpResponse

from .functions import listPosts_resolver

query = ObjectType("Query")
query.set_field("listPosts", listPosts_resolver)


type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, snake_case_fallback_resolvers
)

class PlayGroundView(TemplateView):
    template_name = 'prueba/playground.html'


class GraphQLServerView(View):
    def get(self, request, **kwargs):
        return HttpResponse(PLAYGROUND_HTML)
    
    
    def post(self, *args, **kwargs):
        params = self.request.body.decode()
        data = json.loads(params)
        success, result = graphql_sync(
            schema,
            data,
            context_value=self.request,
            debug=1
        )
        return JsonResponse(result)
