from faker import Faker
fake = Faker()
import random
from .models import *

def seed_db(n=10)->None:
    for i in range(0,n):

        department_objs = Department.objects.all()
        random_index = random.randint(0,len(department_objs))
        department = department_objs[random_index]
        student_id = f'STU-0{random.randint(100,999)}'
        student_name = fake.name()
        student_email = fake.email()
        student_age = random.randint(20,30)
        student_address = fake.address()

