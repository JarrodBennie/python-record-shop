from flask import Flask, render_template, request, redirect
from flask import Blueprint

from models.artist import Artist
import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artists_blueprint = Blueprint("artists", __name__)

@artists_blueprint.route("/artists")
def artists():
    artists = artist_repository.select_all()
    return render_template("artists/index.html", artists = artists)

@artists_blueprint.route("/artists/new", methods=["GET"])
def create_artist():
    return render_template("artists/create.html")

@artists_blueprint.route("/artists", methods=["POST"])
def new_artist():
    name = request.form["name"]
    artist = Artist(name)
    artist_repository.save(artist)
    return redirect("/artists")

@artists_blueprint.route("/artists/<id>", methods=["GET"])
def show_artist(id):
    artist = artist_repository.select(id)
    albums = album_repository.select_for_artist(id)
    return render_template("artists/show.html", artist=artist, albums=albums)

@artists_blueprint.route("/artists/<id>/edit", methods=["GET"])
def edit_artist(id):
    artist = artist_repository.select(id)
    return render_template("artists/edit.html", artist=artist)

@artists_blueprint.route("/artists/<id>", methods=["POST"])
def update_artist(id):
    name = request.form["name"]
    artist = Artist(name, id)
    artist_repository.update(artist)
    return redirect("/artists")

@artists_blueprint.route("/artists/<id>/delete", methods=["POST"])
def delete_artist(id):
    artist_repository.delete(id)
    return redirect("/artists")
