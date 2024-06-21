# session.py
class UserSession:
    def __init__(self):
        self.user_id = None
        self.username = None
        self.password = None
        self.is_authenticated = False

    def authenticate(self, user_id, username, password):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.is_authenticated = True

    def logout(self):
        self.user_id = None
        self.password = None
        self.username = None
        self.is_authenticated = False


# Global session object
user_session = UserSession()
