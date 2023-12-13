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
        """SELECT a.ArtistId, a.Name AS artista 
        FROM artists a
        ORDER BY a.Name DESC;"""
    ).fetchall()
    return render_template('artists/index.html', artists=artists)


@bp.route('/<int:id>')
def detalle(id):    
    db = get_db()
    artist = db.execute(
       """SELECT a.Name AS artista
         FROM artists a
         WHERE a.ArtistId = ?""",
         (id,)
    ).fetchone()

    discos = db.execute(
       """SELECT a.Title AS disco FROM albums a
         WHERE a.ArtistId = ?""",
         (id,)
    ).fetchall()
    return render_template('artists/detalle.html', artist=artist, discos=discos)