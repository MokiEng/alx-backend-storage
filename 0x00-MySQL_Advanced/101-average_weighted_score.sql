-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUsers
-- that computes and store the average weighted score for all students.
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE user_id INT;

    -- Declare a cursor for selecting distinct user IDs
    DECLARE cur CURSOR FOR SELECT DISTINCT user_id FROM corrections;

    -- Declare variables to store the computed values
    DECLARE total_score DECIMAL(5, 2);
    DECLARE total_weight DECIMAL(5, 2);

    -- Create a temporary table to store the results
    CREATE TEMPORARY TABLE IF NOT EXISTS temp_average_weighted_score (user_id INT, average_score DECIMAL(5, 2));

    -- Open the cursor
    OPEN cur;

    -- Start processing rows
    read_loop: LOOP
        FETCH cur INTO user_id;

        IF done THEN
            LEAVE read_loop;
        END IF;

        -- Calculate the total weighted score
        SELECT SUM(c.score * p.weight) INTO total_score
        FROM corrections AS c
        JOIN projects AS p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Calculate the total weight
        SELECT SUM(p.weight) INTO total_weight
        FROM corrections AS c
        JOIN projects AS p ON c.project_id = p.id
        WHERE c.user_id = user_id;

        -- Calculate the average weighted score
        IF total_weight IS NOT NULL THEN
            SET total_score = total_score / total_weight;
        ELSE
            SET total_score = 0;
        END IF;

        -- Insert the computed result into the temporary table
        INSERT INTO temp_average_weighted_score (user_id, average_score) VALUES (user_id, total_score);

    END LOOP;

    -- Close the cursor
    CLOSE cur;

    -- Update the users table with the computed average scores
    UPDATE users
    JOIN temp_average_weighted_score AS t ON users.id = t.user_id
    SET users.average_score = t.average_score;

    -- Drop the temporary table
    DROP TEMPORARY TABLE IF EXISTS temp_average_weighted_score;
END $$

DELIMITER ;
