-- removes all records with a score less than or equal to 5
-- from the table second_table of the database hbtn_0c_0 in your MySQL server
-- The database name will be passed as an argument of the mysql command

DELETE FROM 
    second_table 
WHERE 
    score <= 5;

