#! /usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/ubuntu/FlaskApps/MnistClassifierApp/")
sys.path.insert(1,"/home/ubuntu/.local/lib/python2.7/site-packages")
# home points to the home.py file
from home import app as application
#application.secret_key = "somesecretsessionkey"
