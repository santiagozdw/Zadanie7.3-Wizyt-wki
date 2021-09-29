from BaseContact import BaseContact
class BuissnesContact(BaseContact):
    def __init__(self, position, firm_name, firm_phone, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.position = position
        self.firm_name = firm_name
        self.firm_phone = firm_phone
    def __str__(self) -> str:
        return f'BuissnesContact (name ={self.name}, surname={self.surname}, email={self.email} phone={self.phone}, position ={self.position}, firm_name={self.firm_name}, firm_phone={self.firm_phone})'
