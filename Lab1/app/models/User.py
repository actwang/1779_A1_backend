class User:
    def __init__(self, name, authentication_token, images):
        self.name = name
        self.authentication_token = authentication_token
        self.images = images

    def to_json(self):
        return {
            "name": self.name,
            "authenticationToken": self.authentication_token,
            "images": self.images
        }