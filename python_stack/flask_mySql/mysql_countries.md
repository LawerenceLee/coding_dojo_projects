# Queries

1. What query would you run to get all the countries that speak Slovene? Your query should return the name of the country, language and language percentage. Your query should arrange the result by language percentage in descending order. (1)

    ```sql
    SELECT countries.name, languages.language, languages.percentage FROM countries
    JOIN languages ON countries.code = languages.country_code
    WHERE languages.language = 'slovene'
    ORDER BY languages.percentage DESC;
    ```

2. What query would you run to display the total number of cities for each country? Your query should return the name of the country and the total number of cities. Your query should arrange the result by the number of cities in descending order. (3)

    ```sql
    SELECT countries.name, count(cities.name) as city_count FROM countries
    JOIN cities ON countries.code = cities.country_code
    GROUP BY countries.name ORDER BY city_count DESC;
    ```

3. What query would you run to get all the cities in Mexico with a population of greater than 500,000? Your query should arrange the result by population in descending order. (1)

    ```sql
    SELECT cities.name, cities.population FROM countries
    JOIN cities ON countries.code = cities.country_code
    WHERE cities.population > 500000 && countries.name = "Mexico"
    ORDER BY cities.population DESC;
    ```

4. What query would you run to get all languages in each country with a percentage greater than 89%? Your query should arrange the result by percentage in descending order. (1)

    ```sql
    SELECT countries.name, languages.language, languages.percentage FROM countries
    JOIN languages ON countries.code = languages.country_code
    WHERE languages.percentage > 89.00
    ORDER BY languages.percentage DESC;
    ```

5. What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)

    ```sql
    SELECT name,  surface_area,  population FROM countries
    WHERE surface_area < 501 && population > 100000;
    ```

6. What query would you run to get countries with only Constitutional Monarchy with a capital greater than 200 and a life expectancy greater than 75 years? (1)

    ```sql
    SELECT name, government_form, life_expectancy, capital FROM countries
    WHERE government_form = "Constitutional Monarchy" && capital > 200 && life_expectancy > 75;
    ```

7. What query would you run to get all the cities of Argentina inside the Buenos Aires district and have the population greater than 500, 000? The query should return the Country Name, City Name, District and Population. (2)

    ```sql
    SELECT countries.name, cities.name, cities.district, cities.population FROM countries
    JOIN cities ON countries.code = cities.country_code
    WHERE countries.name = "Argentina" && cities.district = "Buenos Aires" && cities.population > 500000;
    ```

8. What query would you run to summarize the number of countries in each region? The query should display the name of the region and the number of countries. Also, the query should arrange the result by the number of countries in descending order. (2)

    ```sql
    SELECT region, count(name) as country_count FROM countries
    GROUP BY region
    ORDER BY country_count DESC;
    ```