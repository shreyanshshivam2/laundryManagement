import sqlite3 as sq

conn = sq.connect('customer.db') #creates file
conn.execute('''Create table if not exists payment
        (customer_id char(20) not null PRIMARY KEY,
        name char(20) not null,
        address char(30) not null,
        orderid char(20) not null,
        gender char(6) not null,
        mobile number(10) not null,
        email char(25) not null,
        password varchar(25) not null,
       );''')

print('Table Created Successfully')
conn.close()