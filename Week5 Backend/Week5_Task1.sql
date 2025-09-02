CREATE DATABASE RentaCar;

CREATE SCHEMA lyfter_car_rental
    AUTHORIZATION postgres;


CREATE TABLE lyfter_car_rental.users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(100) NOT NULL,
	username VARCHAR(50) NOT NULL,
	email VARCHAR(100) NOT NULL,
	password VARCHAR(30) NOT NULL,
	date_birth DATE NOT NULL,
	account_status VARCHAR(50) NOT NULL
);

-- Inserting 50 users:
INSERT INTO lyfter_car_rental.users (name, username, email, password, date_birth, account_status) VALUES
('Ryan Johnson', 'crivera', 'brandyferguson@gmail.com', '%@*0Agm1Qb9M', '2001-05-06', 'banned'),
('Christopher Barber', 'usheppard', 'juliebowman@jones.com', '@4ZzZP8_Q+4F', '1964-11-11', 'inactive'),
('Mr. Colton Brown', 'richard37', 'singhjoseph@franco.info', '%CV(sGGe95vN', '1962-05-18', 'banned'),
('Deborah Crawford', 'james76', 'tracy51@gmail.com', '$ck3S#MRR#Ob', '1972-09-14', 'active'),
('Kristy Wyatt MD', 'nlewis', 'regina92@hotmail.com', ')YpZGem*44tP', '1960-05-10', 'active'),
('Richard Pruitt', 'schultzmary', 'owilliamson@miller.org', '%70zVYuP$Tye', '2006-03-30', 'pending'),
('Phillip Allen', 'kristinlopez', 'jeremynewton@hotmail.com', '^X%Q@dr(2dbR', '1983-07-01', 'pending'),
('Jesse Myers', 'bryan28', 'icarpenter@thomas.com', '4B__SeJEp#2a', '1971-05-12', 'active'),
('Joseph Harris', 'meagan23', 'baileycain@clarke-fox.com', '_!XMDEr(1UY1', '1995-03-23', 'pending'),
('Jennifer Walker', 'craiganderson', 'jjackson@phillips.info', 'F+Gc9Wg5#Z5W', '1963-12-29', 'inactive'),
('Heather Thomas', 'chadramirez', 'tylergonzales@hotmail.com', 'ppZ2$5sV!H^4', '1970-07-09', 'banned'),
('James Barton', 'nmartinez', 'maryfletcher@adams.org', 'Wc2wP)FeR%jD', '1988-06-11', 'active'),
('Sandra Thompson', 'erica99', 'travis92@morales.com', 'FjZzN@tWy12G', '1999-09-03', 'active'),
('Melissa Lopez', 'timothy22', 'arthur49@perkins.net', 'k1!P3d&QmB$H', '1979-04-26', 'inactive'),
('Catherine Moore', 'bradley64', 'daniel75@yahoo.com', 'Tz4R)jQ9ZqP_', '1967-10-20', 'active'),
('Matthew Smith', 'johnstonkevin', 'phillipthomas@hotmail.com', 'b!Z7Vg$4Hp2U', '2002-02-15', 'pending'),
('Joshua Martinez', 'alicia73', 'lmartin@yahoo.com', 'p*8f4YZmC3!x', '1985-01-05', 'banned'),
('Angela Davis', 'stephanie39', 'matthewbutler@reid.com', 'X#V7!pL0o2cH', '1978-08-08', 'inactive'),
('Donna White', 'andrew20', 'zacharyowens@gmail.com', 'M5$z2R%oB^jN', '1993-04-18', 'active'),
('Paul Green', 'michaelsmith', 'cynthiaortiz@yahoo.com', 'W@3q6Jt#sGp1', '1961-09-23', 'pending'),
('Michelle Miller', 'maryking', 'karenlopez@hotmail.com', 'Zc*0B8hY!t4Q', '1989-03-17', 'active'),
('Kevin Johnson', 'andersonjohn', 'williamsamantha@hotmail.com', 'g#7X0wLpT&jM', '1976-11-05', 'inactive'),
('David Anderson', 'smithheather', 'martinpaul@hotmail.com', 'F!9x2VjL#q8B', '1969-12-19', 'active'),
('Stephanie Robinson', 'emilyjackson', 'jacoballen@rogers.com', 'P@5n8YrL$k2S', '1991-07-13', 'banned'),
('Thomas Hall', 'briangomez', 'rebeccawilliams@garcia.com', 'X^6c3NtQ*o7W', '1982-06-22', 'active'),
('Nancy Hernandez', 'millerfrank', 'andersoneric@yahoo.com', 'M$4v7XgF)q9D', '1975-05-30', 'inactive'),
('George Nelson', 'jessicaadams', 'brownsteven@gmail.com', 'K!2p5LcT#o8R', '1987-01-16', 'pending'),
('Karen Allen', 'johnnyross', 'halltiffany@flores.com', 'S*3w9GvJ!d6K', '1963-08-24', 'active'),
('Robert Young', 'petersusan', 'kathleenmurphy@gmail.com', 'D!8m2XrT^f5Y', '1996-02-28', 'inactive'),
('Patricia Scott', 'rachelthomas', 'joewright@hotmail.com', 'L$7k3NwG)h1C', '1977-12-04', 'banned'),
('Charles King', 'cherylcampbell', 'danielroberts@gmail.com', 'Y%5j6MzB(q2N', '1984-04-07', 'active'),
('Mary Wright', 'larrymoore', 'stephencarter@yahoo.com', 'N!9h4KtP^l7J', '1990-05-19', 'pending'),
('Anthony Mitchell', 'gregorylee', 'barbarajones@hotmail.com', 'R@1x8BqF!d3M', '1966-07-25', 'active'),
('Lisa Perez', 'davidmorris', 'jenniferjohnson@hotmail.com', 'C$4m7XkF)q2P', '1971-09-12', 'inactive'),
('Brian Collins', 'kellyhall', 'richardmartinez@perry.org', 'V*5p9NgL!f6Q', '1980-11-30', 'banned'),
('Sarah Rivera', 'elizabethallen', 'paulhernandez@yahoo.com', 'J!6n2RtV^g7L', '1997-01-11', 'active'),
('Daniel Ward', 'sandrabrown', 'georgethompson@gmail.com', 'T%8j4MwH)k1X', '1974-03-08', 'inactive'),
('Barbara Price', 'christopherjackson', 'michaeldavis@gmail.com', 'Q@7h5LnT*d9B', '1968-10-14', 'pending'),
('Jason Cox', 'patriciawilson', 'margaretmiller@hotmail.com', 'E!2q6BtR^f4K', '1986-09-21', 'active'),
('Elizabeth Rogers', 'markclark', 'dianasmith@yahoo.com', 'U*3k9JmP!h5C', '1962-12-02', 'inactive'),
('Mark Stewart', 'nancygreen', 'kennethlewis@hotmail.com', 'O$1n7VxJ)q8L', '1994-02-26', 'banned'),
('Susan Gray', 'donaldyoung', 'bettywhite@yahoo.com', 'I!4k8GnT^o2M', '1981-05-14', 'active'),
('Steven Brooks', 'josephhill', 'edwardmartin@hughes.com', 'H@9c2YpR!t3B', '1973-11-18', 'inactive'),
('Donna Flores', 'timothybaker', 'phillipwilson@yahoo.com', 'B!5j7QkF^g1N', '1992-08-23', 'pending'),
('Andrew Ward', 'angelarobinson', 'kevinlopez@gmail.com', 'G$6p9MtV)h2K', '1965-10-05', 'active'),
('Karen Murphy', 'jamesallen', 'mariagarcia@hotmail.com', 'Z!2m8KtP^f7D', '1979-09-17', 'inactive'),
('Christopher Long', 'davidwhite', 'robertwilliams@gmail.com', 'P@8x3JqF!d5M', '2000-06-13', 'active'),
('Jessica Jenkins', 'amandawalker', 'nancyharris@hotmail.com', 'C*7p2BnM!h4R', '1983-04-25', 'inactive'),
('Travis Bell', 'victoria46', 'christopherjones@yahoo.com', 'aE(PnMmvB#1x', '1982-10-17', 'active');

-- Table for vehicles
CREATE TABLE lyfter_car_rental.vehicles (
	id SERIAL PRIMARY KEY,
	brand VARCHAR(50) NOT NULL,
	model VARCHAR(50) NOT NULL,
	fabrication_year SMALLINT NOT NULL,
	vehicle_status VARCHAR(50) NOT NULL
);

-- Cross table for users and rents
CREATE TABLE lyfter_car_rental.user_rents (
	id SERIAL PRIMARY KEY,
	user_id BIGINT NOT NULL,
	vehicle_id BIGINT NOT NULL,
	date_rented TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	rent_status VARCHAR(50) NOT NULL
);