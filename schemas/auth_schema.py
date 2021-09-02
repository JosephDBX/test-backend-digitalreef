from graphene import ObjectType, String, Int, Mutation, Boolean, Field

""" User definition """
class User(ObjectType):
    id = Int()
    email = String()
    password = String()
    name = String()
    last_name = String()

""" Response definition """
class UserResponse(ObjectType):
    ok = Boolean()
    message = String()
    user = Field(User)
    token = String()

""" User queries """
def sign_in(email, password):
    memory_email = 'mail@mail.com'
    memory_password = 'qwerty'

    ok = True
    message = ''
    user = None
    token = None

    if (memory_email == email and memory_password == password):
        user=User(id=1, email=email, name='Fulanito', last_name='de Tal')
    else:
        ok = False
        message = 'Wrong email or password!'

    return UserResponse(
        ok=ok,
        message=message,
        user=user,
        token=token
    )

""" User mutations """
""" class CreateUser(Mutation):
    class Arguments:
        email = String()
        password = String()
        name = String()
        last_name = String()

    ok = Boolean()
    user = Field(lambda: User)

    def mutate(root, info, email, password, name, last_name):
        user = User(email, password, name, last_name)
        ok = True

        return CreateUser(ok, user) """