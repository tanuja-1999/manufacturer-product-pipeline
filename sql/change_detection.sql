WITH current_data AS
(
    SELECT *
    FROM PRODUCT_PIPELINE_DB.RAW.PRODUCT_SNAPSHOTS
),

previous_data AS
(
    SELECT *
    FROM PRODUCT_PIPELINE_DB.RAW.PRODUCT_SNAPSHOT_HISTORY
)

SELECT
    c.product_name,
    p.price AS old_price,
    c.price AS new_price,
    c.product_url
FROM current_data c
JOIN previous_data p
    ON c.product_url = p.product_url
WHERE c.price <> p.price;