-- Create a trigger to reset valid_email when email is changed
DELIMITER //
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users -- Replace "your_table" with the actual table name
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0; -- Set valid_email to 0 when email changes
    END IF;
END;
//
DELIMITER ;
