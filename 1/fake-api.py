#!/usr/bin/env python

''' fake-api.py: A fake API to simulate a cricket match '''
__author__ = 'Somsubhra Bairi'
__email__ = 'mail@somsubhra.com'

# All imports
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from json import dumps
from threading import Timer
from random import random
from math import floor

# Define all constants
PORT_NUMBER = 8080
OVERS = 20
OVER_DURATION = 1

# Global variables
scores = [{"name": "A", "runs": 0, "overs": 0}, {"name": "B", "runs": 0, "overs": 0}]
number_of_overs = 0
current_batting_team = 0

# Generate the scores
def generate_scores():

    # Run the timer continuously
    Timer(OVER_DURATION, generate_scores).start()

    # Global variables
    global number_of_overs
    global current_batting_team

    # End of match
    if number_of_overs == OVERS * 2 or scores[1]["runs"] > scores[0]["runs"]:
        return

    # One team finished batting
    if number_of_overs == OVERS:
        current_batting_team = 1

    # Increment number of overs
    number_of_overs += 1

    # Generate random number of runs in an over
    runs_in_over = floor(random() * 12)

    # Set the score in dictionary
    scores[current_batting_team]["runs"] += runs_in_over
    scores[current_batting_team]["overs"] += 1

# Call the score generator
generate_scores()

# The API Handler class
class APIHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/json')
        self.end_headers()

        # Send the json response
        self.wfile.write(dumps(scores))
        return

try:
    #Create a web server and define the handler to manage the
    #incoming request
    server = HTTPServer(('', PORT_NUMBER), APIHandler)
    print 'Started cricket score API server on port ' , PORT_NUMBER

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print '^C received, shutting down the API server'
    server.socket.close()