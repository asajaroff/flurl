import os
import hashlib

from flask import Flask, jsonify

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    @app.route("/")
    def index():
        return "<p>flurl thingy</p>"

    @app.route("/dashboard")
    def dashboard():
        return "<a href='./hash/sha256/hashme'>sha256</a><br><a href='./hash/sha3_512/hashme'>sha3_512</a>"

    @app.route("/hash/sha256/<string:input_string>")
    def generate_hash_sha256(input_string: str):
        h = hashlib.new('sha256')
        h.update(input_string.encode(encoding = 'UTF-8', errors = 'strict'))
        hashed = h.hexdigest()
        return jsonify({
            "name": input_string,
            "hash": hashed,
            "short_hash": hashed[0:5]
        })

    @app.route("/hash/sha3_512/<string:input_string>")
    def generate_hash_sha3_512(input_string: str):
        h = hashlib.new('sha3_512')
        h.update(input_string.encode(encoding = 'UTF-8', errors = 'strict'))
        hashed = h.hexdigest()
        return jsonify({
            "name": input_string,
            "hash": hashed,
            "short_hash": hashed[0:5]
        })

    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)
   
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/blog', endpoint='blog_index')

    from . import url
    app.register_blueprint(url.bp)
    app.add_url_rule('/url', endpoint='url_index')

    return app
