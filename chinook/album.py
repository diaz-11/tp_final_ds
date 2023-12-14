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
        """SELECT AlbumId AS id, Title AS album 
         FROM albums
         ORDER BY Title DESC"""
    ).fetchall()
    return render_template('albums/index.html', albums=albums)

@bp.route('/<int:id>')
def detalle(id):
    db = get_db()
    albums = db.execute(
       """SELECT AlbumId AS id, Title AS album 
         FROM albums""",
         (id,)
          ).fetchone()


    track = db.execute(
        """SELECT t.Name AS nombre, g.Name AS genero, t.Milliseconds AS duracion
            FROM tracks t 
            JOIN genres g ON t.GenreId = g.GenreId
            JOIN albums a ON t.AlbumId = a.AlbumId
            WHERE t.AlbumId = ?;""",
        (id,)
    ).fetchall()

    return render_template('albums/detalle.html', albums=albums, track = track)

    

