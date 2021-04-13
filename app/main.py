from printer_listener import app

# -----------------------------------------------------------------------
# Use main.py to run on any WSGI server
# Example for manually run uwsgi-plugin-python3 with shell command:
#   $ uwsgi --http-socket 0.0.0.0:8080 --plugin python3 --module main:app
# -----------------------------------------------------------------------

if __name__ == "__main__":
    app.run()
