-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
--  that computes and store the average weighted score for a student.
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(5, 2);
    DECLARE total_weight DECIMAL(5, 2);

    SELECT SUM(score * weight) INTO total_score, SUM(weight) INTO total_weight
    FROM corrections
    WHERE user_id = user_id;

    IF total_weight IS NOT NULL THEN
        SET total_score = total_score / total_weight;
    ELSE
        SET total_score = 0;
    END IF;

    UPDATE users
    SET average_weighted_score = total_score
    WHERE id = user_id;
END $$

DELIMITER ;
