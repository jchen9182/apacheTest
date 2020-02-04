#!/usr/bin/python3
import sys

sys.path.insert(0,"/var/www/apacheTest/")
sys.path.insert(0,"/var/www/apacheTest/apacheTest/")

import logging
logging.basicConfig(stream=sys.stderr)

from apacheTest import app as application
