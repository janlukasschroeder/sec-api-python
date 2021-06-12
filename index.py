import socketio
import pprint

pp = pprint.PrettyPrinter(indent=4)
sio = socketio.Client()

server_url = 'https://api.sec-api.io:3334'
api_key = '7d2ea0730f7b2a1fff304b1e91abf634cd020a14e0ed0b6535f22f2443a18f30'
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
