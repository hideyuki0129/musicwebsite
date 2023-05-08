import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from flask import Flask, render_template, request, redirect, url_for
import requests

load_dotenv()
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

app = Flask(__name__)
# Replace 'your_access_token' with the actual access token obtained in step 2
access_token = 'BQC9R3B_743NYPDxFiY9ECu2uK9hIgmEsz7wMsVPLEKFGSdyYuiRGbgY8orE1IND4DjnnaqkUj1VcH3ip7ZIQvxC_5cU8qh_PSyrtckIHqRpvDdg3iW9'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST', 'GET'])
def search(page=1):
    if request.method == 'POST':
        query = request.form['query'] # Change this line
        return redirect(url_for('search', query=query, page=1))

    query = request.args.get('query')
    page = int(request.args.get('page', 1)) # Get the page number from query string or default to 1
    results_per_page = 20
    offset = (page - 1) * results_per_page

    # Update the search API call to include the 'limit' and 'offset' parameters
    search_results = sp.search(q=query, type='track', limit=results_per_page, offset=offset)
    tracks = search_results['tracks']['items']

    return render_template('results.html', query=query, tracks=tracks, page=page, results_per_page=results_per_page)


if __name__ == '__main__':
    app.run(debug=True)