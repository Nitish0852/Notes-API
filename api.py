from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

NOTES = {
    'note1': {'title': 'Commonly used HTTP methods', 'content' : ' GET, POST, PUT, DELETE' },
    'note2': {'title': 'CRUD', 'content': 'Create | Read | Update | Delete'},
    'note3': {'title': 'Flask-RESTful','content': 'An Extension for Flask that adds support for quickly building REST APIs.'},
}


def abort_if_note_doesnt_exist(note_id):
    """Abort request if note_id does not exist in NOTES"""
    if note_id not in NOTES:
        abort(404, message="Note {} doesn't exist".format(note_id))


# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('task')


# Note
# shows a single note item and lets you updatae or delete a note item
class Note(Resource):
    def get(self, note_id):
        """Return the specified note item given the note_id
        Example:
            # In the terminal
            $ curl http://localhost:5000/notes/note1
            OR
            # Python
            requests.get('http://localhost:5000/notes/note1').json()
        """
        abort_if_note_doesnt_exist(note_id)
        return NOTES[note_id]

    def delete(self, note_id):
        """Deletes an existing task
        Example:
            # In the terminal
            $ curl http://localhost:5000/notes/note1 -X DELETE -v
            OR
            # Python
            requests.delete('http://localhost:5000/notes/note4')
        """
        abort_if_note_doesnt_exist(note_id)
        del NOTES[note_id]
        # 204: SUCCESS; NO FURTHER CONTENT
        return '', 204

    def put(self, note_id):
        """Updates existing task
        Example:
            # In the terminal
            $ curl http://localhost:5000/notes/note1 -d "task=Remember the milk" -X PUT -v
            OR
            # Python
            requests.put('http://localhost:5000/notes/note1',
                         data={'task': 'Remember the milk'}).json()
        """

        # parser
        abort_if_note_doesnt_exist(note_id)
        args = parser.parse_args()
        task = {'task': args['task']}
        NOTES[note_id] = task
        # 201: CREATED
        return task, 201


# NoteList
# shows a list of all notes, and lets you POST to add new tasks
class NoteList(Resource):
    def get(self):
        """Return the current NOTE dictionary
        Example:
            # In the terminal
            $ curl http://localhost:5000/notes
            OR
            # Python
            requests.get('http://localhost:5000/notes').json()
        """
        return NOTES

    def post(self):
        """Adds task to NOTE
        Example:
            # In the terminal
            $ curl http://localhost:5000/notes -d "task=Remember the milk" -X POST -v
            OR
            # Python
            requests.post('http://localhost:5000/notes',
                         data={'task': 'Remember the milk'}).json()
        """
        args = parser.parse_args()
        note_id = int(max(NOTES.keys()).lstrip('note')) + 1
        note_id = 'note%i' % note_id
        NOTES[note_id] = {'task': args['task']}
        # 201: CREATED
        return NOTES[note_id], 201


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(NoteList, '/notes')
api.add_resource(Note, '/notes/<note_id>')


if __name__ == '__main__':
    app.run(debug=True)
