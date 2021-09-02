""" from schemas.mutation import Mutation """
from schemas.query import Query
from schemas.mutation import Mutation
from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema
from flask_graphql_auth import GraphQLAuth

app = Flask(__name__)

""" Authentication """
app.config["JWT_SECRET_KEY"] = "secret_key"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = 60*24
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = 1

auth = GraphQLAuth(app)

""" Adding GraphQL route """
schema = Schema(query=Query, mutation=Mutation)

app.add_url_rule('/api', view_func=GraphQLView.as_view('api', schema=schema, graphiql=True))

if __name__ == "__main__":
    app.run(debug=True, port=80)