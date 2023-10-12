-- a SQL script that creates a stored procedure ComputeAverageWeightedScoreForUser
--  that computes and store the average weighted score for a student.
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(5, 2);
    DECLARE total_weight DECIMAL(5, 2);

    SELECT SUM(c.score * p.weight) INTO total_score
    FROM corrections AS c
    JOIN projects AS p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    SELECT SUM(p.weight) INTO total_weight
    FROM corrections AS c
    JOIN projects AS p ON c.project_id = p.id
    WHERE c.user_id = user_id;

    IF total_weight IS NOT NULL THEN
        SET total_score = total_score / total_weight;
    ELSE
        SET total_score = 0;
    END IF;

    UPDATE users
    SET average_score = total_score
    WHERE id = user_id;
END $$

DELIMITER ;
