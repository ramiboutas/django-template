import random

from huey import crontab
from huey.contrib import djhuey as huey

from .models import HomePage


@huey.db_periodic_task(crontab(hour="2", minute="5"))
def change_homepagehero_sections_daily():
    homepages = HomePage.objects.filter(enable_section_changing=True, hero__is_active=False).distinct()

    for home in homepages:
        active_hero = home.hero_set.filter(is_active=True)
        new_active_hero = random.choice(home.homehero_set.filter(is_active=False))
        active_hero.update(is_active=False)
        new_active_hero.active = True
        new_active_hero.save()


@huey.db_periodic_task(crontab(hour="2", minute="15"))
def auto_adding_articles_to_homepages(self):
    homepages = HomePage.objects.filter(enable_section_changing=True, hero__is_active=False).distinct()
