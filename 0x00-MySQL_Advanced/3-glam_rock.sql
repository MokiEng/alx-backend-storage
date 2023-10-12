-- List bands with Glam rock as their main style, ranked by longevity
SELECT band_name, (IFNULL(split, '2020') - formed) AS lifespan
FROM
    bands
WHERE
    split LIKE '%Glam rock%'
ORDER BY
    lifespan DESC;
