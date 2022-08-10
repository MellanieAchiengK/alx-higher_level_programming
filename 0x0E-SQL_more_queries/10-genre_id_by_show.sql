-- lists all shows contained in hbtn_0d_tvshows 
-- have at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows as tv_shows
	INNER JOIN tv_show_genres as tv_show_genres 
	    ON tv_shows.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;
