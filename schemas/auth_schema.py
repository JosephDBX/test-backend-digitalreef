from graphene import ObjectType, String, Int, Boolean, Field, Mutation, Union
from werkzeug.security import safe_str_cmp
from flask_graphql_auth import create_access_token, create_refresh_token, AuthInfoField

class MessageField(ObjectType):
    message = String()


class ProtectedUnion(Union):
    class Meta:
        types = (MessageField, AuthInfoField)

    @classmethod
    def resolve_type(cls, instance, info):
        return type(instance)

""" User definition """
class User(ObjectType):
    id = Int()
    email = String()
    password = String()
    name = String()
    last_name = String()
    photo_url = String()

class AuthMutation(Mutation):
    class Arguments(object):
        username = String()
        password = String()

    ok = Boolean()
    user = Field(User)
    message = String()
    access_token = String()
    refresh_token = String()

    @classmethod
    def mutate(cls, _, info, username, password):
        memory_email = 'mail@mail.com'
        memory_password = 'qwerty'

        ok = True
        message = None
        user = None
        access_token=(None,)
        refresh_token=(None,)

        if (safe_str_cmp(memory_email.encode('utf-8'), username.encode('utf-8')) and safe_str_cmp(memory_password.encode('utf-8'), password.encode('utf-8'))):
            user=User(id=1, email=memory_email, name='Fulanito', last_name='López', photo_url='https://picsum.photos/600/600')

            access_token=create_access_token(username),
            refresh_token=create_refresh_token(username),
        else:
            ok = False
            message = 'Wrong email or password!'

        return AuthMutation(
            ok=ok,
            user=user,
            message=message,
            access_token=access_token[0],
            refresh_token=refresh_token[0],
        )