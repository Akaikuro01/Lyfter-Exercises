import jwt

class JWT_Manager:
    def __init__(self, public_key, private_key, algorithm):
        self.private_key = private_key
        self.public_key = public_key
        self.algorithm = algorithm

    def encode(self, data):
        try:
            encoded = jwt.encode(data, self.private_key, algorithm=self.algorithm)
            return encoded
        except:
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
            return decoded
        except Exception as e:
            print(e)
            return None