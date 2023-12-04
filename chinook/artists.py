from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from chinook.db import get_db

bp = Blueprint('artist', __name__,url_prefix='/artist')

@bp.route('/')
def index():
    db = get_db()
    artists = db.execute(
        """SELECT tracks.Name , albums.Title, artists.Name
        FROM tracks 
        JOIN albums 
        ON albums.AlbumId = tracks.AlbumId
        JOIN artists 
        ON albums.ArtistId = artists.ArtistId
        ORDER BY artists.Name ASC"""
    ).fetchall()
    return render_template('artists/index.html', artists=artists)
