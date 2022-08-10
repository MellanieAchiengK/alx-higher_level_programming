-- lists all cities contained in hbtn_0d_usa db using join
SELECT cities.id, cities.name, states.name
  FROM cities as cities
       INNER JOIN states AS states ON cities.state_id = states.id
 ORDER BY cities.id;
