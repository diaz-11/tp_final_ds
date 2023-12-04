from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from chinook.db import get_db

bp = Blueprint('album', __name__,url_prefix='/album')

@bp.route('/')
def index():
    db = get_db()
    albums = db.execute(
        """SELECT tracks.Name , albums.Title
        FROM tracks 
        JOIN albums 
        ON albums.AlbumId = tracks.AlbumId
        ORDER BY albums.Title DESC"""
    ).fetchall()
    return render_template('albums/index.html', albums=albums)

