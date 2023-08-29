from datetime import date
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask_ckeditor import CKEditor
from flask_gravatar import Gravatar
from flask_login import UserMixin, login_user, LoginManager, current_user, logout_user, login_required
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

import os
import smtplib

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


if __name__ == "__main__":
    app.run("0.0.0.0", port=8080, debug=True)