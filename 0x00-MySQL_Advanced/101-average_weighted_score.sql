-- To create a stored procedure named ComputeAverageWeightedScoreForUsers
-- that calculates and stores the average weighted score for all students
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    DECLARE total_weighted_score FLOAT;
    DECLARE total_weight FLOAT;

    -- Initialize variables
    SET total_weighted_score = 0;
    SET total_weight = 0;

    -- Calculate the weighted score for each student
    UPDATE users
    SET average_score = (
        SELECT SUM(score * weight) / SUM(weight)
        FROM corrections
        JOIN projects ON corrections.project_id = projects.id
        WHERE corrections.user_id = users.id
    );

    -- Calculate the total weighted score for all students
    SELECT SUM(average_score * weight) INTO total_weighted_score
    FROM users
    JOIN corrections ON users.id = corrections.user_id
    JOIN projects ON corrections.project_id = projects.id;

    -- Calculate the total weight for all students
    SELECT SUM(weight) INTO total_weight
    FROM projects;

    -- Update the average_score for all students
    UPDATE users
    SET average_score = total_weighted_score / total_weight;
END //
DELIMITER ;
