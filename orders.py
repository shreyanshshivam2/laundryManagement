import sqlite3 as sq

conn = sq.connect('customers.db') #creates file
conn.execute('''Create table if not exists orders
        (order_id VARCHAR(20) not null,
        shirts INT not null,
        pants INT not null,
        store_id VARCHAR(20) not null,
        payment_id VARCHAR(20) not null,
        customer_id VARCHAR(20) not null,
        cost FLOAT not null,
        PRIMARY KEY (order_id));''')

print('Table Created Successfully')
conn.close()