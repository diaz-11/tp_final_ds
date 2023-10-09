from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from chinook.db import get_db

bp = Blueprint('tracks', __name__, url_prefix="/tracks")

@bp.route('/')
def index():
    db = get_db()
    track = db.execute(
       """SELECT
            FROM JOIN  ON 
         ORDER BY  DESC"""
    ).fetchall()
    return render_template('track/index.html', track=track)

