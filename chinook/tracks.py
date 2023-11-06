from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from chinook.db import get_db

bp = Blueprint('track', __name__, url_prefix="/track")

@bp.route('/')
def index():
    db = get_db()
    tracks = db.execute(
       """SELECT name
            FROM tracks
         ORDER BY name ASC"""
    ).fetchall()
    return render_template('track/index.html', tracks=tracks)

