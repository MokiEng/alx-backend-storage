-- Create a trigger to update the item quantity after adding a new order
DELIMITER //
CREATE TRIGGER decrease_item_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    DECLARE item_quantity INT;
    DECLARE order_quantity INT;

    -- Get the quantity from the items table for the item associated with the new order
    SELECT quantity INTO item_quantity
    FROM items
    WHERE name = NEW.item_name;

    -- Get the quantity from the new order
    SET order_quantity = NEW.number;

    -- Update the item quantity by subtracting the order quantity
    UPDATE items
    SET quantity = item_quantity - order_quantity
    WHERE name = NEW.item_name;
END;
//
DELIMITER ;
