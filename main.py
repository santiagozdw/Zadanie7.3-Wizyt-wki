from BaseContact import BaseContact
from BuissnesContact import BuissnesContact
from faker import Faker


contact_one = BaseContact (name="Andrzej", surname="Duda", phone=636366363, email="kancelaria@gmial.com")
bcontact_one = BuissnesContact (name="Andrzej", surname="Duda", phone=636366363, email="kancelaria@gmial.com", position="prezydent", firm_name="Polska", firm_phone="626262626")
print(contact_one.label_length)
print(bcontact_one.label_length)
contact_one.contact()

fake = Faker()
def create_contacts(type ,count):
    contacts= []
    for i in range(count):
        contact = None
        full_name =fake.name().split (' ')
        if (type == 'base'):
            contact = BaseContact(name=' '.join(full_name[:-1]), surname=full_name[-1], phone=fake.phone_number(), email=fake.email())
        if (type == 'buissnes'):
            full_name =fake.name().split (' ')
            contact = BuissnesContact(name=' '.join(full_name[:-1]), surname=full_name[-1], phone=fake.phone_number(), email=fake.email(), position=fake.job(), firm_name=fake.company(), firm_phone=fake.phone_number())
        contacts.append(contact)
    return contacts

for contact in create_contacts ('buissnes', 2):
    print(contact)

