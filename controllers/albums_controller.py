from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.album import Album
import repositories.album_repository as album_repository
from models.artist import Artist
import repositories.artist_repository as artist_repository

albums_blueprint = Blueprint("albums", __name__)

@albums_blueprint.route("/albums")
def albums():
    albums = album_repository.select_all()
    return render_template("albums/index.html", albums = albums)

@albums_blueprint.route("/albums/new", methods=["GET"])
def create_album():
    artists = artist_repository.select_all()
    return render_template("albums/create.html", artists = artists)

@albums_blueprint.route("/albums", methods=["POST"])
def new_album():
    artist_id = request.form["artist_id"]
    artist = artist_repository.select(artist_id)
    title = request.form["title"]
    quantity = request.form["quantity"]
    id = request.form["id"]
    album = Album(title, artist, quantity, id)
    album_repository.save(album)
    return redirect("/albums")

@albums_blueprint.route("/albums/<id>", methods=["GET"])
def show_album(id):
    album = album_repository.select(id)
    return render_template("albums/show.html", album = album)

@albums_blueprint.route("/albums/<id>/edit", methods=["GET"])
def edit_album(id):
    album = album_repository.select(id)
    artists = artist_repository.select_all()
    return render_template("albums/edit.html", album = album, artists = artists)

@albums_blueprint.route("/albums/<id>", methods=["POST"])
def update_album(id):
    artist = artist_repository.select(request.form.artist_id)
    request.form["artist"] = artist
    title = request.form["title"]
    quantity = request.form["quantity"]
    id = request.form["id"]
    album = Album(title, artist, quantity, id)
    album_repository.update(album)
    return redirect("/albums")

@albums_blueprint.route("/albums/<id>/delete", methods=["POST"])
def delete_album(id):
    album_repository.delete(id)
    return redirect("/albums")
