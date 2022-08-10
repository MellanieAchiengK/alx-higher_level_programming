-- lists all shows contained in hbtn_0d_tvshows 
-- return NULL if no genre
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows as tv_shows
	LEFT JOIN tv_show_genres as tv_show_genres 
	    ON tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
