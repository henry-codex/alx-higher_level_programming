--  lists all the cities of California that can be found in the database hbtn_0d_usa.
--  table contains only one record where state id 0 cities id
SELECT cities.id, cities.name, states.name FROM cities INNER JOIN states ON  states.id = cities.state_id;
