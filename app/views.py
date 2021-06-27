from flask import request, jsonify
from flask.views import MethodView
from app import app
from app.validator import validate
from app.models import Ad, User
from app.schema import USER_CREATE
from app import db


class UserView(MethodView):

    def get(self, user_id):
        user = User.by_id(user_id)
        return jsonify(user.to_dict())

    @validate('json', USER_CREATE)
    def post(self):
        user = User(**request.json)
        user.set_password(request.json['password'])
        user.add()
        return jsonify(user.to_dict())


class AdView(MethodView):

    def get_ad(self, ad_id):
        ad = Ad.by_id(ad_id)
        return jsonify(ad.to_dict())

    def post_ad(self):
        ad = Ad(**request.json)
        ad.add()
        return jsonify(ad.to_dict())

    def delete_ad(self, ad_id):
        ad = Ad.by_id(ad_id)
        ad.delete()
        return jsonify({'message': 'Ad was deleted'})

    def update_ad(self, ad_id):
        ad = Ad.by_id(ad_id)
        ad.title = request.json['title']
        ad.description = request.json['description']
        db.session.commit()
        return jsonify({'message': 'Ad was updated'})


app.add_url_rule('/users/<int:user_id>', view_func=UserView.as_view('users_get'), methods=['GET', ])
app.add_url_rule('/users/', view_func=UserView.as_view('users_create'), methods=['POST', ])

app.add_url_rule('/ads/', view_func=AdView.as_view('ads_create'), methods=['POST', ])
app.add_url_rule('/ads/<int:ad_id>', view_func=AdView.as_view('ads_get'), methods=['GET', ])
app.add_url_rule('/ads/<int:ad_id>', view_func=AdView.as_view('ads_delete'), methods=['DELETE', ])
app.add_url_rule('/ads/<int:ad_id>', view_func=AdView.as_view('ads_update'), methods=['PATCH', ])
