import mysql.connector

create = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="936700"
)

create_cursor = create.cursor()

create_cursor.execute("CREATE DATABASE IF NOT EXISTS DB")

create_cursor.execute("SHOW DATABASES")

for db in create_cursor:
    print(db)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="936700",
    database="DB"
)

db_cursor = db.cursor()

db_cursor.execute("""
                CREATE TABLE IF NOT EXISTS list (
                id INT, 
                name VARCHAR(100), 
                type VARCHAR(100), 
                sector VARCHAR(100), 
                resources TEXT,
                indiv VARCHAR(100),
                email VARCHAR(100),
                phone VARCHAR(100),
                address VARCHAR(100),
                date DATE
                )
                """)

db_cursor.execute("""
                INSERT INTO list (id, name, type, sector, resources, indiv, email, phone, address, date)
                VALUES
                (1, 'ABC Tech Solutions', 'Business', 'Technology', 'IT consulting, mentorship', 'John Doe', 'john.doe@abctech.com', '123-456-7890', '123 Main St', '2023-01-01'),
                (2, 'Community Health Clinic', 'Community', 'Healthcare', 'Health education programs', 'Jane Smith', 'jane.smith@healthclinic.org', '987-654-3210', '456 Oak Ave', '2023-02-15'),
                (3, 'Green Energy Co-op', 'Business', 'Energy', 'Renewable energy resources', 'Sam Green', 'sam.green@greenenergycoop.com', '555-123-4567', '789 Pine Rd', '2023-03-20'),
                (4, 'Local Arts Foundation', 'Community', 'Arts', 'Art exhibitions, workshops', 'Alex Turner', 'alex.turner@artsfoundation.org', '111-222-3333', '321 Elm St', '2023-04-10'),
                (5, 'XYZ Manufacturing', 'Business', 'Manufacturing', 'Internship programs, factory tours', 'Maria Rodriguez', 'maria.rodriguez@xyzmanufacturing.com', '777-888-9999', '987 Steel Blvd', '2023-05-05'),
                (6, 'Youth Mentorship Alliance', 'Community', 'Education', 'Mentorship programs for students', 'Carlos Gonzalez', 'carlos.gonzalez@youthalliance.org', '333-444-5555', '654 Maple Ln', '2023-06-18'),
                (7, 'Financial Literacy Institute', 'Business', 'Finance', 'Financial education workshops', 'Emily Johnson', 'emily.johnson@financeliteracy.org', '222-111-0000', '876 Oak Ridge', '2023-07-12'),
                (8, 'Local Environmental Group', 'Community', 'Environment', 'Environmental cleanup events', 'Chris Anderson', 'chris.anderson@envirogroup.net', '444-555-6666', '543 Pine Ave', '2023-08-25'),
                (9, 'Global Food Bank', 'Business', 'Non-profit', 'Food donations, volunteer opportunities', 'Sophia Lee', 'sophia.lee@globalfoodbank.org', '666-777-8888', '234 Walnut St', '2023-09-30'),
                (10, 'Small Business Network', 'Community', 'Entrepreneurship', 'Business development workshops', 'Michael Brown', 'michael.brown@smallbiznetwork.com', '999-000-1111', '789 Birch Rd', '2023-10-05');
                """)
db.commit()