from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api()

courses = {
    1 : {"name" : "Physics", "videos" : 47},
    2 : {"name" : "Chemistry", "videos" : 35}
}


class Processor(Resource):
    def get(self, course_id):
        if not course_id:
            return courses
        return courses[course_id]
    def delete(self, course_id):
        del courses[course_id]
    def post(self, course_id):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type = str)
        parser.add_argument("videos", type = int)
        courses[course_id] = parser.parse_args()
        return courses
    def put(self, course_id):
        courses[course_id] = parser.parse_args()
        return courses
api.add_resource(Processor, "/api/courses/<int:course_id>")
api.init_app(app)

if __name__ == "__main__":
    app.run(debug = True, port = 3000, host = "127.0.0.1")