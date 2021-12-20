from flask_restx import fields, Model


class BookModel:
    InputPayLoad = Model(
    'InputPayLoad',
    {
        'id':fields.Integer(),
        'title':fields.String(),
        'author':fields.String(),
        #'date_joined':fields.String(),
    }
    )



    @staticmethod
    def paylaod(api):
        
        api.models[BookModel.InputPayLoad.name] = BookModel.InputPayLoad
        return BookModel.InputPayLoad
