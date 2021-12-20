from flask import Blueprint
from flask_restx import Api

from book_api.book import api as book_ns

blueprint = Blueprint('book_api_v1', __name__, url_prefix='/api/v1/')
api = Api(blueprint,
          title='book API v1',
          version='1.0',
          description='This is version 1.0 for book Api',
          )

api.add_namespace(book_ns)

