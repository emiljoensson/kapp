#!/usr/bin/env python3

import config
import kapp

app = kapp.create_app(config)

# This is only used when running locally. When running live, gunicorn runs
# the application.
if __name__ == '__main__':
    app.run()
