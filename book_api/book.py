from flask_restx import Namespace,Resource
from services.book_service import BookAPIService
from flask import Flask
from api_models.book_model import BookModel
from flask import request
book_service_obj = BookAPIService()

api=Namespace(name="books",description="A simple REST API for books")



#@api.expect(BookModel.paylaod(api))

@api.route('/')
class Books(Resource):

    # @api.marshal_list_with(book_model,code=200,envelope="books")
    def get(self):
        ''' Get all books '''
        
        response = book_service_obj.get_book_record()
        return response

    @api.expect(BookModel.paylaod(api))
    def post(self):
        ''' Create a new book '''
       
        request_payload = api.payload
        
        response = book_service_obj.add_book_record(request_payload)
        return response
