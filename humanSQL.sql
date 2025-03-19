CREATE TABLE dealershipInventory (
  vehicleType VARCHAR (65) NOT NULL,
  carBrand VARCHAR(65) NOT NULL,
  model VARCHAR(65) NOT NULL,
  year INT NOT NULL,
  horsepower INT NOT NULL,
  milesPerGallon DECIMAL (10,2) NOT NULL,
  price INT NOT NULL

)

INSERT INTO dealershipInventory(vehicleType,carBrand,model,year,horsepower,milesPerGallon,price)
VALUES 
('sedan','Toyota','Corolla SE',2015,169,35.5,13500),
('SUV','Land Rover','Range Rover Sport',2024,395,25,180300),
('sedan','Honda','Accord',2019,192,38,19200),
('convertible','Porsche','911 Carrera',2025,388,25,120100),
('SUV','Honda','CR-V Hybrid',2023,190,34,43200),
('coupe','Aston Martin','DBS Superleggera',2023,715,18,319420),
('sedan','Hyundai','Sonata',2020,189,32,24600),
('coupe','Mercedes Benz','C 63 S Coupe',2022,509,24,43500),
('sedan','Toyota','Camry',2022,202,34,25300);