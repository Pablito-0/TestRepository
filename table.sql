SELECT *
FROM mybooks
INNER JOIN impression ON mybooks.book_id = impression.fk_id  