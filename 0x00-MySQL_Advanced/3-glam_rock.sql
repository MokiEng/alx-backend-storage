-- List bands with Glam rock as their main style, ranked by longevity
SELECT
    band_name,
    2022 - YEAR(formed) AS lifespan
FROM
    bands
WHERE
    split LIKE '%Glam rock%'
ORDER BY
    lifespan;
