-- top countries

SELECT
    country,
    COUNT(*) total_cases
FROM journalist_cases
GROUP BY country
ORDER BY total_cases DESC;

-- impunity rate

SELECT
    country,

    COUNT(*) total_cases,

    SUM(
        CASE
            WHEN resolved=0
            THEN 1
            ELSE 0
        END
    ) unresolved_cases

FROM journalist_cases

GROUP BY country;

-- yearly trend

SELECT
    EXTRACT(
        YEAR FROM incident_date
    ) year,

    COUNT(*) total_cases

FROM journalist_cases

GROUP BY year

ORDER BY year;
