from models.album import Album
import repositories.artist_repository as artist_repository
from db.run_sql import run_sql

def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist_id = row["artist_id"]
        artist = artist_repository.select(artist_id)
        title = row["title"]
        quantity = row["quantity"]
        id = row["id"]
        album = Album(title, artist, quantity, id)
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    results = run_sql(sql, (id,))
    row = results[0]
    artist = artist_repository.select(row["artist_id"])
    title = row["title"]
    quantity = row["quantity"]
    id = row["id"]
    album = Album(title, artist, quantity, id)
    return album

def select_for_artist(artist_id):
    artist = artist_repository.select(artist_id)
    albums = []
    sql = "SELECT * FROM albums where artist_id = %s"
    results = run_sql(sql, (artist_id,))
    for row in results:
        title = row["title"]
        quantity = row["quantity"]
        id = row["id"]
        album = Album(title, artist, quantity, id)
        albums.append(album)
    return albums

def save(album):
    sql = "INSERT INTO albums (title, artist_id, quantity) VALUES (%s, %s, %s) RETURNING id"
    results = run_sql(sql, (album.title, album.artist.id, album.quantity))
    id = results[0]["id"]
    album.id = id
    return album

def update(album):
    sql = "UPDATE albums SET (title, artist_id, quantity) = (%s, %s, %s) WHERE id = %s"
    run_sql(sql, (album.title, album.artist.id, album.quantity, album.id))

def delete(id):
    sql = "DELETE FROM albums WHERE id = %s"
    run_sql(sql, (id,)).count
