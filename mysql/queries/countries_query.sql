-- 1) slovenian speaking countries
SELECT countries.name AS 'country_name', languages.language, languages.percentage FROM languages
JOIN countries ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

-- 2) total cities per country
SELECT countries.name AS country_name, COUNT(*) AS city_count FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY COUNT(*) DESC;

-- 3) countries in Mexico with population > 500,000
SELECT countries.name AS 'country', cities.name AS 'city', cities.population FROM cities
JOIN countries ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC;

-- 4) all languages in each country greater than 89%
SELECT countries.name as country_name, languages.language, languages.percentage FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;


-- 5) countries with surfac area < 501 and population > 100,000
SELECT name AS 'country_name', surface_area, population FROM countries
WHERE surface_area < 501 AND population > 100000;

-- 6) countries with constitution monarchy, capital > 200, life expectancy > 75
SELECT name AS 'country_name', government_form, capital, life_expectancy FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;

-- 7) cities in argentina inside the buenos aires district
SELECT countries.name AS 'country_name', cities.name AS 'city_name', cities.district, cities.population FROM countries 
JOIN cities ON cities.country_id = countries.id
WHERE countries.name = 'Argentina' AND cities.district = 'Buenos Aires' AND cities.population > 500000;

-- 8) total countries in each region
SELECT countries.region, COUNT(*) AS country_count FROM countries
GROUP BY countries.region
ORDER BY COUNT(*) DESC;