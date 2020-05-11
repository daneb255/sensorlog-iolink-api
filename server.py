from waitress import serve
import flask_server

serve(flask_server.app, host='0.0.0.0', port=5001)
