DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;

CREATE TABLE artists ( 
  id SERIAL8 PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE albums (
  id SERIAL8 PRIMARY KEY,
  artist_id INT8 REFERENCES artists(id),
  title VARCHAR(255),
  quantity INT8
);

INSERT INTO artists (name)
     VALUES ('AC/DC');

INSERT INTO albums (artist_id, title, quantity)
     VALUES (1, 'Back in Black', 10);
