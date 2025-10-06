-- Script to inser a new user
INSERT INTO lyfter_car_rental.users (name, username, email, password, date_birth, account_status) VALUES
('Hillary Clinton', 'hclint', 'hila1908@gmail.com', '!@Iop984mnd', '2000-05-22', 'banned');

-- Script to add a new vehicle
INSERT INTO lyfter_car_rental.vehicles (brand, model, fabrication_year, vehicle_status)
VALUES ('Honda', 'Civic Si', 2017, 'available');

-- Script to change the status of a user
UPDATE lyfter_car_rental.users
SET account_status = 'active'
WHERE id = 1
-- Validating the change
SELECT * FROM lyfter_car_rental.users WHERE id = 1

-- Script to change the status of a vehicle
UPDATE lyfter_car_rental.vehicles
SET vehicle_status = 'rented'
WHERE id = 1
-- Validating the change
SELECT * FROM lyfter_car_rental.vehicles
WHERE id =1

-- Script to generate a new rental with changes to the user and vehicle
-- Inserting a new vehicle for the rent and make it availavble
INSERT INTO lyfter_car_rental.vehicles (brand, model, fabrication_year, vehicle_status)
VALUES ('Toyota', 'Corolla', 2020, 'available');
-- Generating the rent and setting the rent to 'ongoing'
INSERT INTO lyfter_car_rental.user_rents (user_id, vehicle_id, rent_status) 
VALUES (5, 2, 'ongoing');
-- Updating the status of the vehicle to be 'rented'
UPDATE lyfter_car_rental.vehicles
SET vehicle_status = 'rented'
WHERE id = 2;
-- Validating changes
SELECT * FROM lyfter_car_rental.user_rents;
SELECT * FROM lyfter_car_rental.vehicles
WHERE id =2;

-- Script to confirm the devolution of a vehicle, making the car available and completing the stays of the rent
-- Setting the rent status as completed
UPDATE lyfter_car_rental.user_rents
SET rent_status = 'completed'
WHERE id = 1;
-- Setting the car as available
UPDATE lyfter_car_rental.vehicles
SET vehicle_status = 'available'
WHERE id = 2;

-- Validating changes
SELECT * FROM lyfter_car_rental.user_rents;
SELECT * FROM lyfter_car_rental.vehicles
WHERE id =2;

-- Script to disable a vehicle from rent
UPDATE lyfter_car_rental.vehicles
SET vehicle_status = 'unavailable'
WHERE id = 2;
-- Validating changes
SELECT * FROM lyfter_car_rental.vehicles
WHERE id =2;

-- Script to get all the vehicles rented and another one to get all that are available
SELECT * FROM lyfter_car_rental.vehicles
WHERE vehicle_status = 'rented';

SELECT * FROM lyfter_car_rental.vehicles
WHERE vehicle_status = 'available';

SELECT * FROM lyfter_car_rental.vehicles
WHERE id = '1';


SELECT id, user_id, vehicle_id, date_rented, rent_status FROM lyfter_car_rental.user_rents;

SELECT id, name, username, email, password, date_birth, account_status FROM lyfter_car_rental.users WHERE id = '1' AND name = 'Ryan Johnson';

SELECT * FROM lyfter_car_rental.users
where account_status = 'active'

DELETE FROM lyfter_car_rental.users
WHERE id = 52

SELECT * FROM lyfter_car_rental.vehicles

UPDATE lyfter_car_rental.vehicles
SET vehicle_Status = 'Available'