#!/usr/bin/env python

''' server.py: A server with a fake API to simulate a cricket match '''
__author__ = 'Somsubhra Bairi'
__email__ = 'mail@somsubhra.com'

# All imports
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from json import dumps
from threading import Timer
from random import random
from math import floor
from os import curdir, sep

# Define all constants
PORT_NUMBER = 8080
OVERS = 50
OVER_DURATION = 1

# Global variables
scores = [{"name": "A", "runs": []}, {"name": "B", "runs": []}]
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
    if len(scores[0]["runs"]) > 0 and len(scores[1]["runs"]) > 0:
        if number_of_overs == OVERS * 2 or scores[1]["runs"][-1] > scores[0]["runs"][-1]:
            return

    # One team finished batting
    if number_of_overs == OVERS:
        current_batting_team = 1

    # Increment number of overs
    number_of_overs += 1

    # Generate random number of runs in an over
    runs_in_over = int(floor(random() * 12))

    # Set the score in dictionary
    score_array = scores[current_batting_team]["runs"]

    previous_runs = 0

    if len(score_array) > 0:
        previous_runs = score_array[-1]

    current_runs = runs_in_over + previous_runs
    score_array.append(current_runs)

# Call the score generator
generate_scores()

# The API Handler class
class APIHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):

        if self.path == '/api':
            # API Called
            self.send_response(200)
            self.send_header('Content-type','text/json')
            self.end_headers()

            # Send the json response
            self.wfile.write(dumps(scores))
            return
        else:
            # Default operation for any other path called

            # Set index.html as the default file
            if self.path == "/":
                self.path = "/index.html"

            try:
                #Check the file extension required and
                #set the right mime type
                sendReply = False
                if self.path.endswith(".html"):
                    mimetype='text/html'
                    sendReply = True
                if self.path.endswith(".js"):
                    mimetype='application/javascript'
                    sendReply = True
                if self.path.endswith(".css"):
                    mimetype='text/css'
                    sendReply = True

                if sendReply == True:
                    #Open the static file requested and send it
                    f = open(curdir + sep + self.path) 
                    self.send_response(200)
                    self.send_header('Content-type',mimetype)
                    self.end_headers()
                    self.wfile.write(f.read())
                    f.close()
                return

            except IOError:
                # File not found
                self.send_error(404,'File Not Found: %s' % self.path)

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
