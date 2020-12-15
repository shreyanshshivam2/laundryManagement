import sqlite3 as sq

conn = sq.connect('employee.db')  # creates file
conn.execute('''Create table if not exists orders
        (laundaryman_staff_id VARCHAR(20) not null PRIMARY KEY ,
        name VARCHAR(20) not null,
        email VARCHAR(20) not null,
        contact_no VARCHAR(20) not null,
        address VARCHAR(20) not null,
        gender VARCHAR(20) not null,
        salary VARCHAR(20) not null,
        age INT not null,
        store_id VARCHAR(20) not null);''')

print('Table Created Succes')