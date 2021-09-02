""" from schemas.auth_schema import CreateUser
from graphene import ObjectType

class Mutation(ObjectType):
    create_user = CreateUser.Field() """