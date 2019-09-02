import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',"CourseProj.settings")

import django
django.setup()

# FAKE POP SCRIPT

import random
from proj_app.models import AccessRecord,Topic,WebPage
from faker import Faker

fakegen = Faker()
topics =['Search','Social','Marketplace','News','Games']

def add_topic():
    t =Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        # Get the topic or the entry
        top = add_topic()
        # create fake data
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # create new webpage entry

        webpg = WebPage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create fake access record for that WebPage

        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print('Populating Script!')
    populate(20)
    print('Population Complete!')
