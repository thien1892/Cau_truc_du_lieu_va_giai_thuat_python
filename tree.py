class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self):
        return (f'User(username={self.username}, name={self.name}, email={self.email})')
    
    def __str__(self) -> str:
        return self.__repr__()
