from schemas.auth_schema import UserResponse, sign_in
from graphene import ObjectType, Field, String

class Query(ObjectType):
    hello: String()
    sign_in = Field(UserResponse, email=String(required=True), password=String(required=True))

    def resolve_hello(parent, info):
        return 'Hello! Welcome to Digitalreef'

    def resolve_sign_in(parent, info, email, password):
        return sign_in(email=email, password=password)