# Epic Title: User Account Management

class UserProfile:
    user_id: int
    first_name: str
    last_name: str
    phone_number: str

    def __init__(self, user_id: int, first_name: str, last_name: str, phone_number: str):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
    
    def update_profile(self, first_name: str, last_name: str, phone_number: str):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number