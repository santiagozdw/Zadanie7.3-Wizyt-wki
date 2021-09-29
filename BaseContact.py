class BaseContact:
    def __init__(self, name, surname, phone, email) -> None:
        self.name = name 
        self.surname = surname
        self.phone = phone
        self.email = email
        
    def __str__(self) -> str:
        return f'BaseContact (name ={self.name}, surname={self.surname}, email={self.email} phone={self.phone})'
    
    @property
    def label_length(self):
        return len(f"{self.name} {self.surname}".replace(' ', ''))
        # return len(f"{self.name} {self.surname}")

    def contact(self):
        print(f"Wybieram numer +48 {self.phone} i dzwonię do {self.name} {self.surname}")

    

