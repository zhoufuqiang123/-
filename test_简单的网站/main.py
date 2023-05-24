from flask import Flask, request
from flask import render_template
from test_flask.test_简单的网站 import cmd_mysql
from test_flask.test_简单的网站.router_file_version import router_file_version
from test_flask.test_简单的网站.router_db_version import router_db_version

from flask_cors import CORS

import base64
# #%%
# import os
# print(os.getcwd())
# #%%

app = Flask(__name__)
app.jinja_env.variable_start_string = '[[[['
app.jinja_env.variable_end_string = ']]]]'
CORS(app, supports_credentials=True)


# app.register_blueprint(router_file_version, url_prefix="/file_version")
app.register_blueprint(router_file_version)
app.register_blueprint(router_db_version)


if __name__ == '__main__':
    app.run(
        host='10.20.14.27',
        port=80,
        threaded=True,
        debug=True,
    )

# if __name__ == '__main__':
#     # path = os.listdir('./')
#     print(os.path.dirname(__file__))
#     print(os.getcwd())


