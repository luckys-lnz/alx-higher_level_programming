-- script that lists all shows contained in the database hbtn_0d_tvshows
-- SELECT tv_shows.title IFNULL(tv_shows_genres.genre_id, 'NULL') AS genre_id
-- FROM tv_shows
-- LEFT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
-- ORDER BY tv_shows.title ASC, genre_id ASC

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id;