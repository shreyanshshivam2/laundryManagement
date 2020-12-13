import sqlite3 as sq

conn = sq.connect('employee.db')  # creates file
conn.execute('''Create table if not exists orders
        (store_id VARCHAR(20) not null,
        office_no VARCHAR(20) not null,
        address VARCHAR(20) not null,
        order_id VARCHAR(20) not null,
        PRIMARY KEY (store_id));''')

print('Table Created Successfully')
conn.close()