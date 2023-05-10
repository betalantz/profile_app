from app import app

from models import db, Profile

from faker import Faker
from faker.providers import profile
fake = Faker()
fake.add_provider(profile)

with app.app_context():

    print("Deleting existing profiles")
    Profile.query.delete()

    print("Creating profile objects...")
    profiles = []
    for _ in range(10):
        profile = fake.simple_profile()
        new_profile = Profile(
            name=profile['name'],
            username=profile['username'],
            address=profile['address'],
            email=profile['mail']
        )
        profiles.append(new_profile)

    print("Adding profiles to transaction")
    db.session.add_all(profiles)

    print("committing")
    db.session.commit()

    print("Seeding complete.")
