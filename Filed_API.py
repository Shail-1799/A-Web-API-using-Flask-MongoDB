from flask import Flask
import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId
from flask import jsonify, request
from flask_cors import CORS
import json
from bson import json_util


app = Flask(__name__)

cluster = MongoClient("mongodb+srv://filed_user:filed_pass_123@cluster0.0p4zo.mongodb.net/filed_db?retryWrites=true&w=majority")
db  = cluster["filed_db"]


## CREATE ##

# Adding Files : Always use a list when specifying the metadata to be added

@app.route("/add/<audioFileType>/<audioFileMetadata>", methods=["POST"])
def add_files(audioFileType,audioFileMetadata):

    file_type = audioFileType
    

    if file_type == 'song':

        collection = db["song"]

        
    elif file_type == 'podcast':

        collection = db["podcast"]

        
    else:

        collection = db["audiobook"]

        

    files = json.loads(audioFileMetadata)

    for file in files:
    
        collection.insert_one(file)

    return f"Files added successfully."


## GET ##

# Getting all Files

@app.route("/get_all/<audioFileType>",methods=["GET"])
def get_files(audioFileType):

    file_type = audioFileType
    

    if file_type == 'song':

        collection = db["song"]

        
    elif file_type == 'podcast':

        collection = db["podcast"]

        
    else:

        collection = db["audiobook"]


    all_files = list(collection.find({}))
    return  json.dumps(all_files, default=json_util.default)


# Getting a file using id

@app.route("/get/<audioFileType>/<audioFileID>",methods=["GET"])
def get_file(audioFileType, audioFileID):

    file_type = audioFileType
    

    if file_type == 'song':

        collection = db["song"]

        
    elif file_type == 'podcast':

        collection = db["podcast"]

        
    else:

        collection = db["audiobook"]


    file = collection.find_one({'_id':ObjectId(audioFileID)})
    resp = json_util.dumps(file)
    return resp


## UPDATE##

# Updating a file using id

@app.route("/update/<audioFileType>/<audioFileID>",methods=["PUT"])
def update_file(audioFileType, audioFileID):

    file_type = audioFileType
    

    if file_type == 'song':

        collection = db["song"]

        
    elif file_type == 'podcast':

        collection = db["podcast"]

        
    else:

        collection = db["audiobook"]
   
    
    file = request.get_json(force=True)
    collection.find_one_and_update({'_id':ObjectId(audioFileID)},{"$set": file})
    resp = jsonify("File updated successfully!")
    resp.status_code = 200
    return resp
    

## DELETE ##

# Deleting a file using id

@app.route("/delete/<audioFileType>/<audioFileID>",methods=["DELETE"])
def delete_file(audioFileType, audioFileID):

    file_type = audioFileType
    

    if file_type == 'song':

        collection = db["song"]

        
    elif file_type == 'podcast':

        collection = db["podcast"]

        
    else:

        collection = db["audiobook"]
   

    collection.delete_one({'_id':ObjectId(audioFileID)})
    resp = jsonify("File deleted successfully!")
    resp.status_code = 200
    return resp



# Error message

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status' : 404,
        'message' : 'Not Found: ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


####################################################################################################################################

if __name__ == "__main__":
    app.run(debug=True)