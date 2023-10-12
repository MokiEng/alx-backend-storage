-- a SQL script that lists all bands with Glam rock as
-- their main style, ranked by their longevity.
SELECT
  name AS band_name,
  2022 - CAST(SUBSTRING_INDEX(formed, '-', 1) AS SIGNED) AS lifespan
FROM
  metal_bands
WHERE
  style LIKE '%Glam rock%'
ORDER BY
  lifespan DESC;
