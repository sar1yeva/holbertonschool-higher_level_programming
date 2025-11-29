-- my_genres
SELECT g.name
FROM genres g
JOIN tv_show_genres sg ON g.id = sg.genre_id
JOIN tv_shows s ON sg.show_id = s.id
WHERE s.title = 'Dexter'
ORDER BY g.name ASC;
