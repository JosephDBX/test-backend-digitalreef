from schemas.auth_schema import MessageField, ProtectedUnion
from graphene import ObjectType, String, Field
from flask_graphql_auth import query_jwt_required

class Query(ObjectType):
    protected = Field(type=ProtectedUnion, token=String())

    @query_jwt_required
    def resolve_protected(self, info):
        return MessageField(message="Hello. Welcome to Digitalreef!")