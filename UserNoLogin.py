class UserNoLogin:
    def is_authenticated(self):
        return False
    
    def is_active(self):
        return False
    
    def is_anonymous(self):
        return True

    def get_id(self):
        return None
    
    def is_admin(self):
        return False