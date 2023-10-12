-- List bands with Glam rock as their main style, ranked by longevity
SELECT
    band_name,
    IFNULL(2022 - formed, 0) AS lifespan
FROM
    bands
WHERE
    style = 'Glam rock'
ORDER BY
    lifespan DESC;
