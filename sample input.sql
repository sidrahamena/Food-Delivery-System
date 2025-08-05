#SAMPLE USERS-

#user info
INSERT INTO Users VALUES (1, 'Aanya', 9876543210);
INSERT INTO Users VALUES (2, 'Rahul', 9123456780);

#menu to order from
INSERT INTO Menu VALUES (1, 'Burger', 120.00);
INSERT INTO Menu VALUES (2, 'Pizza', 250.00);
INSERT INTO Menu VALUES (3, 'Pasta', 180.00);
INSERT INTO Menu VALUES (4, 'Fries', 80.00);

#orders places
INSERT INTO Orders VALUES (1, 1, 2, 1); -- Aanya ordered 1 Pizza
INSERT INTO Orders VALUES (2, 2, 4, 2); -- Rahul ordered 2 Fries