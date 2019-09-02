import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"SecProj.settings")

import django
django.setup()

# FAKE POP SCRIPT
import random
from second_app.models import User
from faker import Faker
fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        # create fake data
        fake_name = fakegen.name()
        fake_email = fakegen.email()

        # split name into first and last
        name = fake_name
        first,last = name.split()

        # populate User model
        usr = User.objects.get_or_create(first_name=first,last_name=last,email=fake_email)[0]

if __name__ == '__main__':
    print('Populating Script!')
    populate(20)
    print('Population Complete!')
