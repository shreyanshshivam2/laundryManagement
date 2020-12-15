import sqlite3 as sq

conn = sq.connect('customer.db') #creates file
conn.execute('''Create table if not exists payment
        (customer_id VARCHAR (20) not null,
         payment_id VARCHAR (20) not null,
        order_id VARCHAR (20) not null,
        payment_date date not null,
        cost FLOAT ,
        PRIMARY KEY (payment_id));''')

print('Table Created Successfully')
conn.close()