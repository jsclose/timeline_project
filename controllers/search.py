from flask import *
from extensions import *
import requests
import json
import urllib2

search = Blueprint('search', __name__, template_folder='templates', url_prefix=URL_PREFIX)

@search.route('/form', methods = ['POST', 'GET'])
def form_route():
    print("form route")
    event = request.args.to_dict()
    print (event)
    if event:
    	url = event['songid']
    	caption = event['caption']
    	credit = event['songname']
    	month = event['month']
    	day = event['day']
    	year = event['year']
    	headline = event['headline']
    	description = event['description']
    	cursor = db.cursor()
    	cursor.execute('INSERT into Timeline(year, month, day, headline, description, url, caption, credit) values( %s, %s, %s, %s, %s, %s, %s, %s)', (year, month, day, headline, description, url, caption, credit));

   
    return render_template("form.html")



@search.route('/song', methods = ['POST', 'GET'])
def song_route():
    print("song route")

    val = request.args.to_dict()['query']
    print (val)
    
    if val:
        song = val
        song = song.replace(" ", "+")
        print(song)
        url = 'https://api.spotify.com/v1/search?q=' + song + '&type=track'
        json_obj = urllib2.urlopen(url)
        data = json.load(json_obj)


        #print(data['tracks']['items'][0])
        #gives albums
        print(data['tracks']['items'][0]['artists'][0]['external_urls']['spotify'])
        artist = data['tracks']['items'][0]['artists'][0]['name']
        #url = data['tracks']['items'][0]['artists'][0]['external_urls']['spotify']
        url = data['tracks']['items'][0]['external_urls']['spotify']
        print(url)
        image = data['tracks']['items'][0]['album']['images'][0]['url']
        preview = data['tracks']['items'][0]['preview_url']
        print(image)
        track = data['tracks']['items'][0]['name']

    
   
        return render_template("form.html", preview = preview, url = url, image = image, artist = artist, track = track)

    return render_template("form.html")


