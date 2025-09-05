import mysql.connector
from faker import Faker
import pymysql
import random

connection = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'RIVERHOME',
    db = 'classicmodels',
    charset = 'utf8mb4',
    cursorclass = pymysql.cursors.DictCursor)

faker = Faker() 

# 초급: 1번 고객 테이블에 1명 데이터 넣기
try: 
    customername = faker.user_name()
    contactlastname = faker.last_name()
    contactfirstname = faker.first_name()
    phone = faker.phone_number()

    with connection.cursor() as cursor:
        # %s는 자리표시자. 파이썬 데이터베이스 라이브러리에서 값을 안전하게 전달하기 위함임. %s를 써서 값이 들어갈 자리 지정
        # 실제 값은 cursor.execte(sql,())에서 별도로 넣어 줌. 
        # 직접 넣으면 SQL 인젝션 위험성이 높음. 보안상 이 방법이 더 안전함. 
        sql = "INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone) VALUES (1001, %s, %s, %s, %s)"
        cursor.execute(sql, (customername, contactlastname, contactfirstname, phone))

        connection.commit()

finally: 
    connection.close()

# 초급: 제품 테이블에 새로운 제품 1개 넣기
try: 
    productname = faker.random_company_product()
    productdescription = faker.english_text()
    productvendor = faker.company()
    with connection.cursor() as cursor:
        sql = "insert into products (productName, productDescription, productVendor) values(%s, %s, %s)"
        cursor.execute(sql, (productname, productdescription, productvendor))

    connection.commit()

finally: 
    connection.close()

# 초급: 직원 테이블에 새로운 직원 1명 넣기. 
try: 
    lastname = faker.last_name()
    firstname = faker.first_name()
    email = faker.email()

    with connection.cursor() as cursor:
        sql = "insert into employees (lastName, firstName, email) values(%s, %s, %s)"
        cursor.execute(sql,(lastname, firstname, email))

    connection.commit()

finally:
    connection.close()


# 중급: 고객 테이블에 고객 10명 한번에 넣기 
    # 루프에서 변수의 값을 사용하지 않을 때 _ 사용 
    # 반복문에서 변수가 꼭 필요 없을 경우, 의미없는 변수라는 뜻에서 _ 사용. 
    # 각 반복에서 실제 순번이나 인덱스가 의미가 없기 때문에 변수 이름을_로 설정.
    # 반복 횟수 또는 인덱스 값이 필요하다면, i, n, idx 등을 씀. 
    # 여기서는 고객 번호를 생성해야 값이 들어가서 고객 번호를 생성할 수 있도록 i 사용. 
try:
    data_list = []

    for i in range(10):
        customernumber = i + 1002
        customername = faker.user_name()
        contactlastname = faker.last_name()
        contactfirstname = faker.first_name()
        phone = faker.phone_number()
        data_list.append((customernumber, customername, contactlastname, contactfirstname, phone))

    with connection.cursor() as cursor:
        sql = "INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone) VALUES (%s, %s, %s, %s, %s)"
        cursor.executemany(sql, data_list)

    connection.commit()
finally:
    connection.close()


# 중급: 제품 테이블에 제품 여러개 넣기 

try: 
    data_list = []

    for _ in range(15):
        productname = faker.random_company_product()
        productdescription = faker.text()
        productvendor = faker.company()
        data_list.append((productname, productdescription, productvendor))
    with connection.cursor() as cursor:
        sql = "insert into products (productName, productDescription, productVendor) values(%s, %s, %s)"
        cursor.executemany(sql, data_list)

    connection.commit()

finally: 
    connection.close()    

# 중급: 직원 여러명 넣어보기 

try: 
    data_list = [] 
    for _ in range(20):
        lastname = faker.last_name()
        firstname = faker.first_name()
        email = faker.email()
        data_list.append((lastname, firstname, email))

    with connection.cursor() as cursor:
        sql = "insert into employees (lastName, firstName, email) values(%s, %s, %s)"
        cursor.executemany(sql, data_list)  

    connection.commit()

finally:
    connection.close()


# 고급: 고객 테이블에 새 고객 추가하고 바로 주문 추가 1명 
try:
    # 데이터 생성
    customername = faker.user_name()
    contactlastname = faker.last_name()
    contactfirstname = faker.first_name()
    phone = faker.phone_number()

    orderdate = faker.date()
    requireddate = faker.date()
    status = faker.word()

    quantityordered = faker.random_number()
    priceeach = float(faker.random_number(digits=2)) + random.random()

    with connection.cursor() as cursor:
        sql = "INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone) VALUES (1001, %s, %s, %s, %s)"
        cursor.execute(sql, (customername, contactlastname, contactfirstname, phone))
        customernumber = 1040

        sql2 = "INSERT INTO orders (customerNumber, orderDate, requiredDate, status) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql2, (customernumber, orderdate, requireddate, status))
        ordernumber = cursor.lastrowid

        sql3 = "INSERT INTO orderdetails (orderNumber, quantityOrdered, priceEach) VALUES (%s, %s, %s)"
        cursor.execute(sql3, (ordernumber, quantityordered, priceeach))


    connection.commit()
finally:
    connection.close()
