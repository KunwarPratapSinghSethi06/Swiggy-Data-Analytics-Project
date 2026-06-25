CREATE DATABASE swiggy_project;
USE swiggy_project;
CREATE TABLE swiggy (
    restaurant_name TEXT,
    cuisine TEXT,
    rating FLOAT,
    number_of_ratings INT,
    average_price INT,
    number_of_offers INT,
    offer_name TEXT,
    area TEXT,
    pure_veg TEXT,
    location TEXT,
    price_category TEXT,
    rating_category TEXT
);
SELECT * FROM swiggy LIMIT 10;
SELECT restaurant_name, location, rating
FROM swiggy
ORDER BY rating DESC
LIMIT 10;
SELECT cuisine, COUNT(*) AS total
FROM swiggy
GROUP BY cuisine
ORDER BY total DESC;
SELECT location, COUNT(*) AS total
FROM swiggy
GROUP BY location
ORDER BY total DESC;
SELECT price_category, ROUND(AVG(rating),2) AS avg_rating
FROM swiggy
GROUP BY price_category;
SELECT pure_veg, COUNT(*) AS total
FROM swiggy
GROUP BY pure_veg;
SELECT restaurant_name, rating, average_price
FROM swiggy
WHERE rating > 4.2 AND average_price < 300
ORDER BY rating DESC;
SELECT number_of_offers, AVG(rating) AS avg_rating
FROM swiggy
GROUP BY number_of_offers
ORDER BY number_of_offers;

