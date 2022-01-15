import hotel_data


hotel_tables = (
    """
    CREATE TABLE IF NOT EXISTS employee (
        employee_id  SERIAL,    
        first_name VARCHAR(200) NOT NULL,
        last_name VARCHAR(200) NOT NULL,
        ssn VARCHAR(200) NOT NULL,
        birth_date DATE,
        mobile_number VARCHAR(200) NOT NULL,
        email VARCHAR(200),
        job_type VARCHAR(200),
        PRIMARY KEY (employee_id)
    )
    """, 
    """
    CREATE TABLE IF NOT EXISTS hotel_location (
        location_id  SERIAL,
        country VARCHAR(200) NOT NULL,
        city VARCHAR(200) NOT NULL,
        street_name VARCHAR(200) NOT NULL,
        building_number INTEGER,
        PRIMARY KEY (location_id)
    )
    """,
     """
    CREATE TABLE IF NOT EXISTS customer (
        customer_id  SERIAL,
        first_name VARCHAR(200) NOT NULL,
        last_name VARCHAR(200) NOT NULL,
        ssn VARCHAR(200) NOT NULL,
        birth_date DATE,
        mobile_number VARCHAR(200) NOT NULL,
        email VARCHAR(200),
        PRIMARY KEY (customer_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS payment_method (
        payment_method_id  SERIAL,
        type VARCHAR(200) NOT NULL,
        PRIMARY KEY (payment_method_id)
    )
    """,
     """
    CREATE TABLE IF NOT EXISTS facilities (
        facility_id  SERIAL,
        name VARCHAR(200) NOT NULL,
        PRIMARY KEY (facility_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS hotel (
        hotel_id  SERIAL,
        name VARCHAR(200) NOT NULL,
        phone_number VARCHAR(200) NOT NULL,
        stars INTEGER,
        location_id INTEGER,
        PRIMARY KEY (hotel_id),
        FOREIGN KEY (location_id) REFERENCES hotel_location(location_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS room (
        room_id  SERIAL,
        floor INTEGER NOT NULL,
        num_of_bedroom INTEGER NOT NULL,
        balcony BOOL,
        hotel_id INTEGER,
        PRIMARY KEY (room_id),
        FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS shop (
        shop_id  SERIAL,
        name VARCHAR(200) NOT NULL,
        phone_number VARCHAR(200)  NOT NULL,
        PRIMARY KEY (shop_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS restaurant (
        restaurant_id  SERIAL,
        name VARCHAR(200) NOT NULL,
        phone_number VARCHAR(200) NOT NULL,
        PRIMARY KEY (restaurant_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS cafe (
        cafe_id  SERIAL,
        name VARCHAR(200) NOT NULL,
        phone_number VARCHAR(200) NOT NULL,
        PRIMARY KEY (cafe_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS hotel_shop (
        hotel_shop_id  SERIAL,
        shop_id INTEGER,
        hotel_id INTEGER,
        PRIMARY KEY (hotel_shop_id),
        FOREIGN KEY (shop_id) REFERENCES shop(shop_id),
        FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
    )
    """,
      """
    CREATE TABLE IF NOT EXISTS hotel_restaurant (
        hotel_rest_id  SERIAL,
        restaurant_id INTEGER,
        hotel_id INTEGER,
        PRIMARY KEY (hotel_rest_id),
        FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id),
        FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
    )
    """,
      """
    CREATE TABLE IF NOT EXISTS hotel_cafe (
        hotel_cafe_id  SERIAL,
        cafe_id INTEGER,
        hotel_id INTEGER,
        PRIMARY KEY (hotel_cafe_id),
        FOREIGN KEY (cafe_id) REFERENCES cafe(cafe_id),
        FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS hotel_employee (
        hotel_e_id  SERIAL,
        employee_id INTEGER,
        hotel_id INTEGER, 
        salary INTEGER NOT NULL,
        PRIMARY KEY (hotel_e_id),
        FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
        FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS hotel_facility (
        hotel_facility_id  SERIAL,
        facility_id INTEGER, 
        hotel_id INTEGER,
        PRIMARY KEY (hotel_facility_id),
        FOREIGN KEY (facility_id) REFERENCES facilities(facility_id),
        FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS working (
        working_id  SERIAL,
        employee_id INTEGER, 
        room_id INTEGER, 
        working_date TIMESTAMP NOT NULL,
        PRIMARY KEY (working_id),
        FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
        FOREIGN KEY (room_id) REFERENCES room(room_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS stay (
        stay_id  SERIAL,
        customer_id INTEGER, 
        room_id INTEGER,
        check_in DATE NOT NULL,
        check_out DATE,
        num_of_people INTEGER,
        PRIMARY KEY (stay_id),
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
        FOREIGN KEY (room_id) REFERENCES room(room_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS bill (
        bill_id  SERIAL,
        transaction_date TIMESTAMP NOT NULL,
        amount INTEGER NOT NULL,
        payment_method_id INTEGER,
        facility_id INTEGER,
        customer_id INTEGER,
        PRIMARY KEY (bill_id),
        FOREIGN KEY (payment_method_id) REFERENCES payment_method(payment_method_id),
        FOREIGN KEY (facility_id) REFERENCES facilities(facility_id),
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
    )
    """
    )


table_names = {
    'employee' : hotel_data.employee,
    'hotel_location' : hotel_data.hotel_location,
    'customer' : hotel_data.customer,
    'payment_method': hotel_data.payment_method,
    'facilities' : hotel_data.facilities,
    'hotel': hotel_data.hotel,
    'room': hotel_data.room,
    'shop': hotel_data.shop,
    'restaurant': hotel_data.restaurant,
    'cafe': hotel_data.cafe,
    'hotel_shop': hotel_data.hotel_shop,
    'hotel_restaurant': hotel_data.hotel_restaurant,
    'hotel_cafe': hotel_data.hotel_cafe,
    'hotel_employee': hotel_data.hotel_employee,
    'hotel_facility': hotel_data.hotel_facility,
    'working': hotel_data.working,
    'stay': hotel_data.stay,
    'bill': hotel_data.bill
}


hotel_tables_dw = (
    """
    CREATE TABLE IF NOT EXISTS employee (
        employee_id  BIGINT,    
        first_name VARCHAR(200) NOT NULL,
        last_name VARCHAR(200) NOT NULL,
        ssn VARCHAR(200) NOT NULL,
        birth_date DATE,
        mobile_number VARCHAR(200) NOT NULL,
        email VARCHAR(200),
        job_type VARCHAR(200),
        PRIMARY KEY (employee_id)
    )
    """, 
    """
    CREATE TABLE IF NOT EXISTS hotel_location (
        location_id  BIGINT,
        country VARCHAR(200) NOT NULL,
        city VARCHAR(200) NOT NULL,
        street_name VARCHAR(200) NOT NULL,
        building_number BIGINT,
        PRIMARY KEY (location_id)
    )
    """,
     """
    CREATE TABLE IF NOT EXISTS customer (
        customer_id  BIGINT,
        first_name VARCHAR(200) NOT NULL,
        last_name VARCHAR(200) NOT NULL,
        ssn VARCHAR(200) NOT NULL,
        birth_date DATE,
        mobile_number VARCHAR(200) NOT NULL,
        email VARCHAR(200),
        PRIMARY KEY (customer_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS payment_method (
        payment_method_id  BIGINT,
        type VARCHAR(200) NOT NULL,
        PRIMARY KEY (payment_method_id)
    )
    """,
     """
    CREATE TABLE IF NOT EXISTS facilities (
        facility_id  BIGINT,
        name VARCHAR(200) NOT NULL,
        PRIMARY KEY (facility_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS hotel (
        hotel_id  BIGINT,
        name VARCHAR(200) NOT NULL,
        phone_number VARCHAR(200) NOT NULL,
        stars BIGINT,
        location_id BIGINT,
        PRIMARY KEY (hotel_id),
        FOREIGN KEY (location_id) REFERENCES hotel_location(location_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS room (
        room_id  BIGINT,
        floor BIGINT NOT NULL,
        num_of_bedroom BIGINT NOT NULL,
        balcony BOOL,
        hotel_id BIGINT,
        PRIMARY KEY (room_id),
        FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS shop (
        shop_id  BIGINT,
        name VARCHAR(200) NOT NULL,
        phone_number VARCHAR(200)  NOT NULL,
        PRIMARY KEY (shop_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS restaurant (
        restaurant_id  BIGINT,
        name VARCHAR(200) NOT NULL,
        phone_number VARCHAR(200) NOT NULL,
        PRIMARY KEY (restaurant_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS cafe (
        cafe_id  BIGINT,
        name VARCHAR(200) NOT NULL,
        phone_number VARCHAR(200) NOT NULL,
        PRIMARY KEY (cafe_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS hotel_shop (
        hotel_shop_id  BIGINT,
        shop_id BIGINT,
        hotel_id BIGINT,
        PRIMARY KEY (hotel_shop_id),
        FOREIGN KEY (shop_id) REFERENCES shop(shop_id),
        FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
    )
    """,
      """
    CREATE TABLE IF NOT EXISTS hotel_restaurant (
        hotel_rest_id  BIGINT,
        restaurant_id BIGINT,
        hotel_id BIGINT,
        PRIMARY KEY (hotel_rest_id),
        FOREIGN KEY (restaurant_id) REFERENCES restaurant(restaurant_id),
        FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
    )
    """,
      """
    CREATE TABLE IF NOT EXISTS hotel_cafe (
        hotel_cafe_id  BIGINT,
        cafe_id BIGINT,
        hotel_id BIGINT,
        PRIMARY KEY (hotel_cafe_id),
        FOREIGN KEY (cafe_id) REFERENCES cafe(cafe_id),
        FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS hotel_employee (
        hotel_e_id  BIGINT,
        employee_id BIGINT,
        hotel_id BIGINT, 
        salary BIGINT NOT NULL,
        PRIMARY KEY (hotel_e_id),
        FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
        FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS hotel_facility (
        hotel_facility_id  BIGINT,
        facility_id BIGINT, 
        hotel_id BIGINT,
        PRIMARY KEY (hotel_facility_id),
        FOREIGN KEY (facility_id) REFERENCES facilities(facility_id),
        FOREIGN KEY (hotel_id) REFERENCES hotel(hotel_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS working (
        working_id  BIGINT,
        employee_id BIGINT, 
        room_id BIGINT, 
        working_date TIMESTAMP NOT NULL,
        PRIMARY KEY (working_id),
        FOREIGN KEY (employee_id) REFERENCES employee(employee_id),
        FOREIGN KEY (room_id) REFERENCES room(room_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS stay (
        stay_id  BIGINT,
        customer_id BIGINT, 
        room_id BIGINT,
        check_in DATE NOT NULL,
        check_out DATE,
        num_of_people BIGINT,
        PRIMARY KEY (stay_id),
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id),
        FOREIGN KEY (room_id) REFERENCES room(room_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS bill (
        bill_id  BIGINT,
        transaction_date TIMESTAMP NOT NULL,
        amount BIGINT NOT NULL,
        payment_method_id BIGINT,
        facility_id BIGINT,
        customer_id BIGINT,
        PRIMARY KEY (bill_id),
        FOREIGN KEY (payment_method_id) REFERENCES payment_method(payment_method_id),
        FOREIGN KEY (facility_id) REFERENCES facilities(facility_id),
        FOREIGN KEY (customer_id) REFERENCES customer(customer_id)
    )
    """
    )
