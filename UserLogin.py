from Permission_level import PermissionLevel


class UserLogin:
    def print(self):
        print(f"""id={self.__user.id} username={self.__user.username} permission_level={self.__user.permission_level}""")

    def fromDB(self, user_id, get_user):
        self.__user = get_user(user_id)
        return self
    
    def create(self, user):
        self.__user = user
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
    def is_admin(self):
        return self.__user.permission_level == PermissionLevel.ADMIN

    def get_id(self):
        return self.__user.id