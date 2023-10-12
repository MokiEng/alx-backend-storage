-- a SQL script that creates a stored procedure ComputeAverageScoreForUser
--that computes and store the average score for a student
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_corrections INT;
    DECLARE avg FLOAT;

    -- Calculate the total score and total number of corrections for the user
    SELECT SUM(score), COUNT(*) INTO total_score, total_corrections
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the average score, or set to 0 if there are no corrections
    IF total_corrections > 0 THEN
        SET avg = total_score / total_corrections;
    ELSE
        SET avg = 0;
    END IF;

    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = avg
    WHERE id = user_id;
END;
//
DELIMITER ;
