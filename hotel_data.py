import pandas as pd
import numpy as np
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine
from numpy.random import default_rng
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg
from datetime import date, timedelta


fake = Faker()
employee_1 = defaultdict(list)

for i in range(1000):
    rng = gen(pcg(seed = 365)) 
    employee_1["employee_id"].append(rng.choice(1000, size=1000, replace=False)[i]) 
    employee_1["first_name"].append( fake.first_name() )
    employee_1["last_name"].append( fake.last_name() )
    employee_1["ssn"].append( fake.ssn() )
    employee_1["birth_date"].append( fake.date_of_birth() )
    employee_1["mobile_number"].append( fake.phone_number() )
    employee_1["email"].append( fake.email() )
    employee_1["job_type"].append( np.random.choice(["Guest Services Associate","Guest Services Supervisor","Hotel Clerk","Hotel Receptionist","Reservationist","Reservations Agent","Events Manager","Executive Conference Manager","Executive Meeting Manager","Meeting and Convention Planner","Meeting Coordinator","Meeting Manager","Meeting Planner","Meeting Specialist","Special Events Manager","Wedding Coordinator","Baggage Porter","Director of Housekeeping","Director of Maintenance","Director of Operations","Executive Housekeeper","Housekeeper","Housekeeping Aide","Housekeeping Supervisor","Lead Housekeeper","Maid","Maintenance Supervisor","Maintenance Worker","Director of Hotel Sales","Director of Marketing and Sales","Group Sales Manager","Hotel Manager","Lodging Manager","Sales and Marketing Manager","Shift Leader","Shift Manager","Spa Manager","Wedding Sales Manager","Service","Administration","Security"],
    p=[0.0307692307692308,0.0133333333333333,0.0307692307692308,0.0307692307692308,0.0307692307692308,0.0307692307692308,0.0133333333333333,0.0133333333333333,0.0133333333333333,0.0307692307692308,0.0307692307692308,0.0133333333333333,0.0307692307692308,0.0307692307692308,0.0133333333333333,0.0307692307692308,0.0307692307692308,0.0307692307692308,0.0307692307692308,0.0307692307692308,0.0307692307692308,0.0307692307692308,0.0307692307692308,0.0133333333333333,0.0307692307692308,0.0307692307692308,0.0133333333333333,0.0307692307692308,0.0307692307692308,0.0307692307692308,0.0133333333333333,0.0133333333333333,0.0133333333333333,0.0133333333333333,0.0307692307692308,0.0133333333333333,0.0133333333333333,0.0133333333333333,0.0307692307692308,0.0307692307692308,0.0307692307692308]))

employee = pd.DataFrame(employee_1)

print(employee.employee_id.is_unique)

location_1 = defaultdict(list)

for i in range(50):
    rng = gen(pcg(seed = 36)) 
    location_1["location_id"].append(rng.choice(50, size=50, replace=False)[i]) 
    location_1["country"].append( fake.country() )
    location_1["city"].append( fake.city() )
    location_1["street_name"].append( fake.street_name() )
    location_1["building_number"].append( fake.building_number())

hotel_location = pd.DataFrame(location_1)

customer_1 = defaultdict(list)

for i in range(2000):
    rng = gen(pcg(seed = 365)) 
    customer_1["customer_id"].append(rng.choice(2000, size=2000, replace=False)[i]) 
    customer_1["first_name"].append( fake.first_name() )
    customer_1["last_name"].append( fake.last_name() )
    customer_1["ssn"].append( fake.ssn() )
    customer_1["birth_date"].append( fake.date_of_birth() )
    customer_1["mobile_number"].append( fake.phone_number() )
    customer_1["email"].append( fake.email() )
    

customer = pd.DataFrame(customer_1)

payment_ids = [1,2,3,4,5,6]
payment_type = ["Cash", "Checks", "Debit cards", "Credit cards", "Mobile payments", "Electronic bank transfers"]

payment_method = pd.DataFrame(zip(payment_ids,payment_type),columns=["payment_method_id","type"])

rng = gen(pcg(seed = 365)) 
facilities_list = ["Rent-a-car","Airline reservation and confirmation","Babysitter upon request","Tour","Multilingual staff","24-hour currency exchange","24-hour Manager on Duty","Dry cleaning and laundry","Banquet facilities","Bar","Computer facility","Conference and meeting facilities","Disabled room","Fitness room","Health club","Sauna and steam bath","Lounge","Luggage storage","Non-smoking rooms","Parking outside the hotel at an extra charge","Pet friendly at a surcharge","Restaurant","Smoking rooms","Summer terrace","Complimentary Wi-Fi internet throughout the entire hotel","Semi open & outdoor restaurant","Poolside bar","Car parking","Swimming pool/ Jacuzzi","Public computer","24 Hour security","Outside catering service","150 Capacity outdoor terrace","45 Seating conference room","35 Seating private air-conditioning dining room","Water purification system","Sunset boat trip","Gift shop"]

fac_ids = rng.choice(50, size=len(facilities_list), replace=False)
facilities = pd.DataFrame(zip(fac_ids,facilities_list),columns=["facility_id","name"])


hotel_1 = defaultdict(list)

for i in range(20):
    rng = gen(pcg(seed = 365)) 
    hotel_1["hotel_id"].append(rng.choice(20, size=20, replace=False)[i]) 
    hotel_1["name"].append(np.random.choice([ "Radisson Blu Hotel","Grand Hotel", "Golden Palace Hotel", "Ani Grand Hotel"],
    p = [0.3,0.25,0.2,0.25]))
    hotel_1["phone_number"].append( fake.phone_number() )
    hotel_1["stars"].append(5)
    hotel_1["location_id"].append(np.random.choice(hotel_location.location_id))

hotel = pd.DataFrame(hotel_1)

hotel = hotel.drop_duplicates(
  subset = ['name', 'location_id'],
  keep = 'last').reset_index(drop = True)

room_1 = defaultdict(list)

for i in range(500):
    rng = gen(pcg(seed = 365)) 
    room_1["room_id"].append(rng.choice(500, size=500, replace=False)[i]) 
    room_1["floor"].append(rng.choice(10, size=500, replace=True)[i])
    room_1["num_of_bedroom"].append(rng.choice(5, size=500, replace=True)[i])
    room_1["balcony"].append(np.random.choice([True, False],p = [0.5,0.5]))
    room_1["hotel_id"].append(np.random.choice(hotel.hotel_id))

room = pd.DataFrame(room_1)

shop_1 = defaultdict(list)
shop_name = ['Art Cross','IrinExArt Souvenir','Gifts','Arev souvenirs','Colors of Armenia']

for i in range(5):
    rng = gen(pcg(seed = 365)) 
    shop_1["shop_id"].append(rng.choice(5, size=5, replace=False)[i]) 
    shop_1["name"].append(shop_name[i])
    shop_1["phone_number"].append( fake.phone_number() )

shop = pd.DataFrame(shop_1)

restaurant_1 = defaultdict(list)
restaurant_name = ["Sherep","Dargett Craft Beer","Tapastan","Yasaman","Mayrig","Tavern Yerevan","Lavash"]

for i in range(7):
    rng = gen(pcg(seed = 35)) 
    restaurant_1["restaurant_id"].append(rng.choice(7, size=7, replace=False)[i]) 
    restaurant_1["name"].append(restaurant_name[i])
    restaurant_1["phone_number"].append( fake.phone_number() )

restaurant = pd.DataFrame(restaurant_1)

cafe_1 = defaultdict(list)
cafe_name = ['Blueberry','vienna cafe yerevan','Rooby','Malocco Cafe','Coffeeshop','Tiziano','Impresso']

for i in range(7):
    rng = gen(pcg(seed = 35)) 
    cafe_1["cafe_id"].append(rng.choice(7, size=7, replace=False)[i]) 
    cafe_1["name"].append(cafe_name[i])
    cafe_1["phone_number"].append( fake.phone_number() )


cafe = pd.DataFrame(cafe_1)

hotel_shop_1 = defaultdict(list)

for i in range(50):
    rng = gen(pcg(seed = 365)) 
    hotel_shop_1["hotel_shop_id"].append(rng.choice(50, size=50, replace=False)[i]) 
    hotel_shop_1["shop_id"].append(np.random.choice(shop.shop_id))
    hotel_shop_1["hotel_id"].append(np.random.choice(hotel.hotel_id))

hotel_shop = pd.DataFrame(hotel_shop_1)

hotel_shop = hotel_shop.drop_duplicates(
  subset = ['shop_id', 'hotel_id'],
  keep = 'last').reset_index(drop = True)

hotel_restaurant_1 = defaultdict(list)


for i in range(70):
    rng = gen(pcg(seed = 365)) 
    hotel_restaurant_1["hotel_rest_id"].append(rng.choice(70, size=70, replace=False)[i]) 
    hotel_restaurant_1["restaurant_id"].append(np.random.choice(restaurant.restaurant_id))
    hotel_restaurant_1["hotel_id"].append(np.random.choice(hotel.hotel_id))

hotel_restaurant = pd.DataFrame(hotel_restaurant_1)

hotel_restaurant = hotel_restaurant.drop_duplicates(
  subset = ['restaurant_id', 'hotel_id'],
  keep = 'last').reset_index(drop = True)

hotel_cafe_1 = defaultdict(list)

for i in range(60):
    rng = gen(pcg(seed = 365)) 
    hotel_cafe_1["hotel_cafe_id"].append(rng.choice(60, size=60, replace=False)[i]) 
    hotel_cafe_1["cafe_id"].append(np.random.choice(cafe.cafe_id))
    hotel_cafe_1["hotel_id"].append(np.random.choice(hotel.hotel_id))

hotel_cafe = pd.DataFrame(hotel_cafe_1)

hotel_cafe = hotel_cafe.drop_duplicates(
  subset = ['cafe_id', 'hotel_id'],
  keep = 'last').reset_index(drop = True)

hotel_emp = defaultdict(list)
salary = list(range(80000,200000,5000))

for i in range(5000):
    rng = gen(pcg(seed = 365)) 
    hotel_emp["hotel_e_id"].append(rng.choice(5000, size=5000, replace=False)[i]) 
    hotel_emp["employee_id"].append(np.random.choice(employee.employee_id))
    hotel_emp["hotel_id"].append(np.random.choice(hotel.hotel_id))
    hotel_emp["salary"].append(np.random.choice(salary))

hotel_employee = pd.DataFrame(hotel_emp)

hotel_employee = hotel_employee.drop_duplicates(
  subset = ['employee_id', 'hotel_id'],
  keep = 'last').reset_index(drop = True)

hotel_facility_1 = defaultdict(list)

for i in range(3000):
    rng = gen(pcg(seed = 359)) 
    hotel_facility_1["hotel_facility_id"].append(rng.choice(3000, size=3000, replace=False)[i]) 
    hotel_facility_1["facility_id"].append(np.random.choice(facilities.facility_id))
    hotel_facility_1["hotel_id"].append(np.random.choice(hotel.hotel_id))

hotel_facility = pd.DataFrame(hotel_facility_1)

hotel_facility = hotel_facility.drop_duplicates(
  subset = ['facility_id', 'hotel_id'],
  keep = 'last').reset_index(drop = True)


start = list(range(1,1000))
end = list(range(1,31))
working_1 = defaultdict(list)

for i in range(3000):
    rng = gen(pcg(seed = 359)) 
    working_1["employee_id"].append(np.random.choice(employee.employee_id))
    working_1["room_id"].append(np.random.choice(room.room_id))
    working_1["working_date"].append( date.today() - timedelta(days = int(np.random.choice(start))) )
    
working = pd.DataFrame(working_1)


working = working.drop_duplicates(
  subset = None,
  keep = 'last').reset_index(drop = True)


stay_1 = defaultdict(list)

for i in range(500):
    rng = gen(pcg(seed = 359)) 
    stay_1["customer_id"].append(np.random.choice(customer.customer_id))
    stay_1["room_id"].append(np.random.choice(room.room_id))
    stay_1["check_in"].append( date.today() - timedelta(days = int(np.random.choice(start))) )
    stay_1["check_out"].append( stay_1["check_in"][i] + timedelta(days = int(np.random.choice(end))) )
    stay_1["num_of_people"].append(np.random.choice(list(range(1,6))) )

stay = pd.DataFrame(stay_1)

stay = stay.drop_duplicates(
  subset = ['room_id'],
  keep = 'last').reset_index(drop = True)

print(stay.room_id.is_unique)

bill_1 = defaultdict(list)
amount = list(range(30000,100000,5000))

for i in range(300):
    rng = gen(pcg(seed = 359)) 
    bill_1["transaction_date"].append( stay["check_in"][i] - timedelta(days = int(np.random.choice(list(range(1,5))))))
    bill_1["amount"].append(np.random.choice(amount))
    bill_1["payment_method_id"].append(np.random.choice(payment_method.payment_method_id))
    bill_1["facility_id"].append(np.random.choice(facilities.facility_id))
    bill_1["customer_id"].append(stay["customer_id"][i])

bill = pd.DataFrame(bill_1)

bill = bill.drop_duplicates(
  subset = ['customer_id'],
  keep = 'last').reset_index(drop = True)


print("Done Data")