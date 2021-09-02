""" from schemas.mutation import Mutation """
from schemas.query import Query
from flask import Flask
from flask_graphql import GraphQLView
from graphene import Schema

app = Flask(__name__)

""" Adding GraphQL route """
app.add_url_rule('/api', view_func=GraphQLView.as_view(
    'api',
    schema=Schema(query=Query),
    graphiql=True
))

if __name__ == "__main__":
    app.run(debug=True, port=80)