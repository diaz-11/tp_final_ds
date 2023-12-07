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
        """SELECT name, artistId
        FROM artists 
        ORDER BY Name ASC"""
    ).fetchall()
    return render_template('artists/index.html', artists=artists)


@bp.route('/<int:id>')
def detalle(id):   
    db = get_db()
    artist = db.execute(
       """SELECT ar.Name AS artista 
         FROM artists ar
         WHERE ar.ArtistId = ?""",
         (id,)
    ).fetchone()
    return render_template('artist/detalle.html', artist=artist)

