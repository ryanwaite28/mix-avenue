# --- Modules/Functions --- #

import os , sys , cgi , re, hmac, hashlib, smtplib, requests, datetime
import logging, dateutil, urllib, sqlite3, httplib2
import json, psycopg2, random, string
from datetime import timedelta
from dateutil import parser

from flask import Flask, make_response, g, request, url_for, send_from_directory
from flask import render_template, url_for, redirect, flash, jsonify
from flask import session as login_session
from sqlalchemy import cast, Column, ForeignKey, Integer, String, DateTime, exc, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, desc, or_
from sqlalchemy.sql import func
from sqlalchemy.exc import InvalidRequestError, ArgumentError, StatementError, OperationalError, InternalError
from functools import wraps
from jinja2.ext import do
from werkzeug.utils import secure_filename
from threading import Timer

# --- Setup --- #

current_dir = os.path.dirname(os.path.abspath(__file__))
ALLOWED_EXTENSION = set(['zip'])

app = Flask(__name__)
app.secret_key = '98vny569kt245cyt9785jctwkrthg9w385h78y5j078tj'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSION

# ---

def sendMSG(email, subject, msg):
    # Set Headers

    FROM = "status@travellrs.com"
    TO = [email] # must be a list
    SUBJECT = subject
    TEXT = msg

    # Prepare actual message

    message = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)

    try:
        server = smtplib.SMTP('mail.travellrs.com:25')
        server.starttls()
        server.login('status@travellrs.com', 'RMW@nasa2015')
        server.sendmail(FROM, TO, message)
        server.quit()

        return 'successful'

    except Exception:
        return 'unsuccessful'

# ---


# --- Routes --- #
# --- Routes --- #
# --- Routes --- #

@app.route('/', methods=['GET'])
def home():
    if request.method == 'GET':
        return render_template('welcome.html')
# ---



@app.route('/get_firebase_info', methods=['POST'])
def get_firebase_info():
    return jsonify(msg = "firebase", status = 200, data = {})
# ---


if __name__ == '__main__':
    app.debug = True
    app.run( host = '0.0.0.0' , port = 8000 )
# ---
