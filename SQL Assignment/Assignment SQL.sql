create database market_co;
use market_co;

CREATE TABLE Company (
    CompanyID INT PRIMARY KEY,
    CompanyName VARCHAR(45),
    Street VARCHAR(45),
    City VARCHAR(45),
    State VARCHAR(2),
    Zip VARCHAR(10)
);

-- 1) Statement to create the Contact table
CREATE TABLE Contact (
    ContactID INT PRIMARY KEY,
    CompanyID INT,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    Street VARCHAR(45),
    City VARCHAR(45),
    State VARCHAR(2),
    Zip VARCHAR(10),
    IsMain BOOLEAN,
    Phone VARCHAR(12),
    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
);


-- 2) Statement to create the Employee table 

CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY,
    FirstName VARCHAR(45),
    LastName VARCHAR(45),
    HireDate DATE,
    JobTitle VARCHAR(25),
    Email VARCHAR(45),
    Phone VARCHAR(12)
);

-- Statement to create the ContactEmployee table

CREATE TABLE ContactEmployee (
    ContactEmployeeID INT PRIMARY KEY,
    ContactID INT,
    EmployeeID INT,
    ContactDate DATE,
    Description VARCHAR(100),
    FOREIGN KEY (ContactID) REFERENCES Contact(ContactID),
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID)
);

-- Insert Data into Company Table

insert into Company (CompanyID, CompanyName, Street, City, State, Zip) values
(1, 'Urban Outfitters, Inc.', '123 Fashion St', 'New York', 'NY', '10001'),
(2, 'Toll Brothers', '456 Luxury Rd', 'Philadelphia', 'PA', '19103');

-- Insert Data into Contact Table

insert into Contact (ContactID, CompanyID, FirstName, LastName, Street, City, State, Zip, Initial, Phone) values
(1, 1, 'John', 'Doe', '789 Market St', 'San Francisco', 'CA', '94103', TRUE, '415-555-1234'),
(2, 2, 'Jane', 'Smith', '987 Broad St', 'Philadelphia', 'PA', '19110', FALSE, '215-555-5678');

-- Insert Data into Employee Table

insert into Employee (EmployeeID, FirstName, LastName, Salary, JobTitle, Email, Phone) values
(1, 'Lesley', 'Bland', 50000.00, 'Manager', 'lesley.bland@marketco.com', '123-456-7890'),
(2, 'Jack', 'Lee', 45000.00, 'Sales Associate', 'jack.lee@marketco.com', '987-654-3210');

-- Insert Data into ContactEmployee Table

insert into ContactEmployee (ContactEmployeeID, ContactID, EmployeeID, ContactDate, Description) values
(1, 1, 1, '2024-03-12', 'Discussed marketing strategies'),
(2, 2, 2, '2024-03-15', 'Negotiated contract terms');

-- Update Lesley Bland’s Phone Number

set SQL_SAFE_UPDATES = 0;

update Employee
set Phone = '215-555-8800'
where FirstName = 'Lesley' and LastName = 'Bland';

set SQL_SAFE_UPDATES = 1;

-- Change Company Name
set SQL_SAFE_UPDATES = 0;
update Company
set CompanyName = 'Urban Outfitters'
where CompanyName = 'Urban Outfitters, Inc. ';
set SQL_SAFE_UPDATES = 1;

-- Remove Dianne Connor’s Contact with Jack Lee

delete from ContactEmployee
where ContactEmployeeID = 2;

-- Retrieve Employees Who Contacted Toll Brothers

select Employee.FirstName, Employee.LastName
from Employee
join ContactEmployee on Employee.EmployeeID = ContactEmployee.EmployeeID
join Contact on Contact.ContactID = ContactEmployee.ContactID
join Company on Contact.CompanyID = Company.CompanyID
where Company.CompanyName = 'Toll Brothers';

-- Significance of % and _ in LIKE

select * from Employee where FirstName like 'J%';  -- Finds names starting with 'J'
select * from Employee where FirstName like '_a_'; -- Finds names with 'a' as second letter

-- Normalization in Databases
-- ANSWER :- Normalization is the process of organizing data in a database to reduce redundancy and improve integrity.
-- First Normal Form (1NF): Ensure all columns contain atomic values.
-- Second Normal Form (2NF): Remove partial dependencies.
-- Third Normal Form (3NF): Remove transitive dependencies.

-- What is a JOIN in MySQL?

-- ANSWER:- A JOIN combines records from two or more tables based on a related column.
-- Common Types of Joins:
-- INNER JOIN: Only matching rows.
-- LEFT JOIN: All rows from the left table, plus matches from the right.
-- RIGHT JOIN: All rows from the right table, plus matches from the left.
-- FULL JOIN: All rows from both tables (not supported in MySQL directly).

-- What do you understand about DDL, DCL, and DML in MySQL? 

-- ANSWER:- DDL (Data Definition Language) – Defines structure
			-- CREATE, ALTER, DROP, TRUNCATE
-- DML (Data Manipulation Language) – Modifies data
	-- INSERT, UPDATE, DELETE, SELECT
-- DCL (Data Control Language) – Controls access
	-- GRANT, REVOKE
    
-- What is the role of the MySQL JOIN clause in a query, and what are some common types of joins?    

-- ANSWER:- Used to combine records from multiple tables.

-- INNER JOIN – Returns matching records.
-- LEFT JOIN – All left table records + matching right ones.
-- RIGHT JOIN – All right table records + matching left ones.
-- FULL JOIN (Not in MySQL, use UNION).
-- CROSS JOIN – Cartesian product (all possible combinations).

