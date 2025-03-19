/* Prompt used for all AI engines: Create a table in MySQL names dealershipInventory with columns: vehicle type, car brand, model, year, horsepower, miles per gallon, and price. Populate this table with sample data.*/

/*ChatGPT*/
CREATE TABLE dealershipInventory (
    vehicle_type VARCHAR(50),
    car_brand VARCHAR(50),
    model VARCHAR(50),
    year INT,
    horsepower INT,
    mpg FLOAT,
    price DECIMAL(10,2)
);

INSERT INTO dealershipInventory (vehicle_type, car_brand, model, year, horsepower, mpg, price) VALUES
('Sedan', 'Toyota', 'Camry', 2022, 203, 32.0, 28000.00),
('SUV', 'Honda', 'CR-V', 2023, 190, 28.5, 32000.00),
('Truck', 'Ford', 'F-150', 2021, 400, 24.0, 45000.00),
('Sports Car', 'Chevrolet', 'Corvette', 2023, 495, 19.0, 70000.00),
('Electric', 'Tesla', 'Model 3', 2024, 283, 130.0, 42000.00),
('Sedan', 'Hyundai', 'Elantra', 2023, 147, 33.5, 22000.00),
('SUV', 'BMW', 'X5', 2022, 335, 26.0, 62000.00);


/*Gemini*/
-- Create the dealershipInventory table
CREATE TABLE dealershipInventory (
    vehicle_type VARCHAR(50),
    car_brand VARCHAR(50),
    model VARCHAR(50),
    year INT,
    horsepower INT,
    miles_per_gallon DECIMAL(4, 1),
    price DECIMAL(10, 2)
);

-- Insert sample data into the table
INSERT INTO dealershipInventory (vehicle_type, car_brand, model, year, horsepower, miles_per_gallon, price) VALUES
('Sedan', 'Toyota', 'Camry', 2023, 203, 33.0, 26970.00),
('SUV', 'Honda', 'CR-V', 2024, 190, 30.0, 29510.00),
('Truck', 'Ford', 'F-150', 2023, 400, 20.0, 40850.00),
('Sedan', 'Honda', 'Civic', 2024, 158, 36.0, 23950.00),
('SUV', 'Toyota', 'RAV4', 2023, 203, 30.0, 27975.00),
('Sports Car', 'Chevrolet', 'Corvette', 2024, 495, 18.0, 65500.00),
('Truck', 'Chevrolet', 'Silverado', 2024, 310, 22.0, 38500.00),
('Sedan', 'Nissan', 'Altima', 2023, 188, 32.0, 25600.00),
('SUV', 'Jeep', 'Grand Cherokee', 2024, 293, 21.0, 39000.00),
('Hatchback', 'Mazda', 'Mazda3', 2024, 191, 31.0, 23350.00);

-- You can now query the table to see the data
SELECT * FROM dealershipInventory;


/*Grok3*/
-- Create the table
CREATE TABLE dealershipInventory (
    vehicle_type VARCHAR(50),
    car_brand VARCHAR(50),
    model VARCHAR(50),
    year INT,
    horsepower INT,
    miles_per_gallon INT,
    price DECIMAL(10,2)
);

-- Insert sample data
INSERT INTO dealershipInventory (vehicle_type, car_brand, model, year, horsepower, miles_per_gallon, price) VALUES
('Sedan', 'Toyota', 'Camry', 2023, 203, 32, 27995.00),
('SUV', 'Honda', 'CR-V', 2022, 190, 28, 31950.00),
('Truck', 'Ford', 'F-150', 2023, 290, 20, 41995.00),
('Coupe', 'BMW', '4 Series', 2023, 255, 29, 45900.00),
('Hatchback', 'Volkswagen', 'Golf', 2022, 147, 33, 23995.00),
('Sedan', 'Tesla', 'Model 3', 2023, 283, 131, 43990.00),
('SUV', 'Jeep', 'Grand Cherokee', 2022, 293, 22, 38995.00),
('Minivan', 'Chrysler', 'Pacifica', 2023, 287, 22, 37995.00);

/*Claude*/
-- Create the dealershipInventory table
CREATE TABLE dealershipInventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    vehicleType VARCHAR(50) NOT NULL,
    carBrand VARCHAR(50) NOT NULL,
    model VARCHAR(100) NOT NULL,
    year INT NOT NULL,
    horsepower INT,
    milesPerGallon DECIMAL(4,1),
    price DECIMAL(10,2) NOT NULL
);

-- Insert sample data
INSERT INTO dealershipInventory (vehicleType, carBrand, model, year, horsepower, milesPerGallon, price) VALUES
('Sedan', 'Toyota', 'Camry', 2023, 203, 32.2, 28500.00),
('SUV', 'Honda', 'CR-V', 2022, 190, 30.5, 31200.00),
('Truck', 'Ford', 'F-150', 2024, 325, 22.0, 45750.00),
('Sedan', 'Tesla', 'Model 3', 2023, 283, 131.0, 46990.00),
('SUV', 'Jeep', 'Grand Cherokee', 2022, 293, 21.5, 39995.00),
('Hatchback', 'Volkswagen', 'Golf', 2023, 147, 34.0, 25000.00),
('Coupe', 'Chevrolet', 'Corvette', 2024, 495, 19.5, 65995.00),
('SUV', 'Subaru', 'Outback', 2023, 182, 29.5, 33995.00),
('Sedan', 'BMW', '3 Series', 2022, 255, 28.0, 47500.00),
('Minivan', 'Chrysler', 'Pacifica', 2023, 287, 24.5, 42000.00),
('SUV', 'Audi', 'Q5', 2024, 261, 26.3, 51990.00),
('Sedan', 'Hyundai', 'Elantra', 2022, 147, 37.0, 22500.00),
('Truck', 'Chevrolet', 'Silverado', 2023, 355, 21.0, 41995.00),
('SUV', 'Mazda', 'CX-5', 2024, 187, 28.5, 32500.00),
('Hatchback', 'Kia', 'Soul', 2023, 147, 31.0, 23590.00);

-- Verify the data
SELECT * FROM dealershipInventory;

/*Perplexity*/
-- Create the dealershipInventory table
CREATE TABLE dealershipInventory (
    vehicle_type VARCHAR(50),
    car_brand VARCHAR(50),
    model VARCHAR(50),
    year INT,
    horsepower INT,
    miles_per_gallon DECIMAL(5, 2),
    price DECIMAL(10, 2)
);

-- Insert sample data into the dealershipInventory table
INSERT INTO dealershipInventory (vehicle_type, car_brand, model, year, horsepower, miles_per_gallon, price)
VALUES
    ('Sedan', 'Toyota', 'Camry', 2023, 203, 32.5, 28000.00),
    ('SUV', 'Honda', 'CR-V', 2022, 190, 28.0, 32000.00),
    ('Truck', 'Ford', 'F-150', 2024, 400, 20.0, 45000.00),
    ('Coupe', 'Chevrolet', 'Camaro', 2021, 275, 25.0, 35000.00),
    ('Hatchback', 'Volkswagen', 'Golf', 2020, 147, 35.0, 22000.00),
    ('Electric', 'Tesla', 'Model S', 2025, 670, NULL, 79999.99),
    ('Hybrid', 'Toyota', 'Prius', 2023, 121, 56.0, 27000.00);
