# A-Web-API-using-Flask-MongoDB

It is a Flask Web API that simulates the behavior of an audio file 
server while using MongoDB.

Audio file type can be one of the following:
1 – Song
2 – Podcast
3 – Audiobook

Song file fields:
- ID
- Name of the song 
- Duration in number of seconds 
- Uploaded time

Podcast file fields:
- ID 
- Name of the podcast
- Duration in number of seconds 
- Uploaded time
- Host 
- Participants

Audiobook file fields:
- ID
- Title of the audiobook 
- Author of the title 
- Narrator 
- Duration in number of seconds 
- Uploaded time 

I have implemented CRUD : Create, Read, Upload, and Delete endpoints for an audio file as defined 
below:

Create API:
The request will have the following fields:
- audioFileType – mandatory, one of the 3 audio types possible
- audioFileMetadata – mandatory, dictionary, contains the metadata for one of the three audio files (song, podcast, audiobook)

Delete API:- 
The route will be in the following format:“<audioFileType>/<audioFileID>”

Update API:
- The route be in the following format: “<audioFileType>/<audioFileID>”
- The request body will be the same as the upload

Get API:
- The route “<audioFileType>/<audioFileID>” will return the specific audio file
- The route “<audioFileType>” will return all the audio files of that type
