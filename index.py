#!/usr/bin/python

import sys
import socketio
import pprint

pp = pprint.PrettyPrinter(indent=4)
sio = socketio.Client()

server_url = 'https://api.sec-api.io:3334'
api_key = str(sys.argv[1])
connection_string = server_url + '?apiKey=' + api_key


@sio.on('connect', namespace='/all-filings')
def on_connect():
    print("Connected to https://api.sec-api.io:3334")


@sio.on('filing', namespace='/all-filings')
def on_filing(filing):
    formatted = pp.pformat(filing)
    print(formatted)


@sio.on('error', namespace='/all-filings')
def on_error(error):
    print("Error", error)


@sio.event
def disconnect():
    print('Disconnected from server')


sio.connect(connection_string, namespaces=['/all-filings'])
sio.wait()
