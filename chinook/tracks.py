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
       """SELECT name, trackId
            FROM tracks
         ORDER BY name ASC"""
    ).fetchall()
    return render_template('track/index.html', tracks=tracks)

@bp.route('/<int:id>')
def detalle(id):
    db  = get_db()
    track = db.execute(
       """SELECT g.Name AS genero, a.Title AS album,ar.Name AS artista,t.Milliseconds,t.Bytes, t.UnitPrice
            FROM tracks t 
            JOIN genres g ON t.GenreId = g.GenreId
            JOIN albums a ON t.AlbumId = a.AlbumId
            JOIN artists ar ON a.ArtistId = ar.ArtistId
            WHERE t.TrackId = ?""",
         (id,)
    ).fetchone()
    return render_template('track/detalle.html', track=track)

