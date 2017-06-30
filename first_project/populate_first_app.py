import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE","first_project.settings")

import django
django.setup()

import random
from first_app.models import AccessRecord,WebPage,Topic
from faker import Faker

fakegen = Faker()
topics =["Search", "Social", "MarketPlace", "Sports", "News"]

def addTopic():
    t=Topic.objects.get_or_create(top_name =random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top = addTopic()

        fake_url = fakegen.url()
        fake_name = fakegen.company()
        fake_date = fakegen.date()

        webpg = WebPage.objects.get_or_create(topic = top, url =fake_url, name = fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__== '__main__':
    print("Populating")
    populate(10)
    print("Done")
