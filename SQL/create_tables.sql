CREATE TABLE journalist_cases(

    id INT PRIMARY KEY,

    country VARCHAR(20),

    incident_date DATE,

    gender VARCHAR(20),

    age INT,

    media VARCHAR(50),

    conflict_zone BOOLEAN,

    enquiry_status VARCHAR(50),

    resolution_date DATE,

    resolved INT,

    impunity INT,

    resolution_days INT

);