from api_models.book_model import BookModel
from flask_restx import marshal


class BookConverters:
    def __init__(self):
        self._all_books = BookModel.InputPayLoad


    def convert_to_get_book(self,final_response):
        return marshal(final_response, self._all_books) 

    def convert_to_post_book(self,final_response):
        return marshal(final_response, self._all_books)
