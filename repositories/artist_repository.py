from models.artist import Artist
from db.run_sql import run_sql

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        name = row["name"]
        id = row["id"]
        artist = Artist(name, id)
        artists.append(artist)
    return artists

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    results = run_sql(sql, (id,))
    row = results[0]
    name = row["name"]
    id = row["id"]
    artist = Artist(name, id)
    return artist

def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
    results = run_sql(sql, (artist.name,))
    id = results[0]["id"]
    artist.id = id
    return artist

def update(artist):
    sql = "UPDATE artists SET (name) = (%s) WHERE id = %s"
    run_sql(sql, (artist.name, artist.id))

def delete(id):
    sql = "DELETE FROM artists WHERE id = %s"
    run_sql(sql, (id,)).count
