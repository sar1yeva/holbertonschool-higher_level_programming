-- comedy_only
SELECT s.title
FROM tv_shows s
JOIN tv_show_genres sg ON s.id = sg.show_id
JOIN genres g ON sg.genre_id = g.id
WHERE g.name = 'Comedy'
ORDER BY s.title ASC;
