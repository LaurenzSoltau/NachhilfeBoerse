import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from App.db import get_db

# create blueprint named auth and the urls prefix auth
bp = Blueprint("auth", __name__, url_prefix="/auth")
