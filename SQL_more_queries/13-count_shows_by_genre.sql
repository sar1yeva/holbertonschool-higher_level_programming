-- count_shows_by_genre
SELECT g.name AS genre, COUNT(sg.show_id) AS number_of_shows
FROM genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
GROUP BY g.name
ORDER BY number_of_shows DESC;
