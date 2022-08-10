-- lists all shows in hbtn_0d_tvshows DB
SELECT shows.title
FROM tv_shows AS shows
	INNER JOIN tv_show_genres AS show_genres 
	    ON shows.id = show_genres.show_id
	    INNER JOIN tv_genres AS tv_genres
	    ON tv_genres.id = show_genres.genre_id
	    WHERE tv_genres.name = 'Comedy'
ORDER BY shows.title;
