-- lists all records of the table second_table
-- Dont list rows without a name value
-- Records should be listed by descending score
SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
