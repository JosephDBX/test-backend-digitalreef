from schemas.auth_schema import AuthMutation
from graphene import ObjectType

class Mutation(ObjectType):
    auth = AuthMutation.Field()