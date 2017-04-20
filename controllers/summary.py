from flask import *
from extensions import *
import json, requests
import re
summary = Blueprint('summary', __name__, template_folder='templates', url_prefix=URL_PREFIX)

@summary.route('/summary')
def summary_route():

	return render_template("summary.html")




@summary.route('/api/json')
def timeline_json():
	cursor = db.cursor()
	cursor.execute('SELECT * FROM Timeline')
	json = cursor.fetchall()

	events = []
	for event in json:
		current_event = {}
		media = {}
		start_date = {}
		text = {}
		media['url'] = event['url']
		media['caption'] = event['caption']
		media['credit'] = event['credit']
		start_date['month'] = event['month']
		start_date['day'] = event['day']
		start_date['year'] = event['year']
		text['headline'] = event['headline']
		text['text'] = event['description']

		current_event['media'] = media
		current_event['start_date'] = start_date
		current_event['text'] = text
		events.append(current_event)



	print(events)


	return jsonify(events = events);
	



	