# Notes-API
a flask-RESTful service to manage notes.

## Working
Run the API
```
python api.py
```
Now open Another terminal

Get the Notes (in json format)
```
curl http://localhost:5000/notes
```
Get a Single Note
```
curl http://localhost:5000/notes/note1
```
Delete a Note
```
curl http://localhost:5000/notes/note1 -X DELETE -v
```
Add A new Note
```
curl http://localhost:5000/notes -d "note=do something new" -X POST -v
```
Update a Note
```
curl http://localhost:5000/notes/note3 -d "note=something different" -X PUT -v
```
