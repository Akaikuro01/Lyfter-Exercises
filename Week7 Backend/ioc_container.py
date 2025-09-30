from db import db_context
from JWT_Manager import JWT_Manager
from PEM_keys_generator import generate_private_key, generate_puplic_key
from Repositories.user_repository import UserRepository
from Repositories.roles_repository import RoleRepository
from Repositories.products_repository import ProductRepository
from Repositories.invoice_repository import InvoiceRepository

class IocContainter():
    def __init__(self):
        self.db_context = db_context
        self.jwt_manager = JWT_Manager(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtQ+6YtY2FWKm6IrLNKCp
TNxlmWQC6imk9fkuOm6Puar//QoQT6IaqMdzayZmmsRkgXqNvj0+XZ3OOf3SmeKT
G0rpNr7zofdjKBwguehDA9RmdzknijLF84CQd5VOT5Pm/PAZJ7bzjLjbhr3IpCsg
B8XsZm99SdkI0CxAcM+m6o+albr5A09Q0WGAe0Du2Ec/Lfw83YrVFwrgwrFDnl32
IR2e6jub+jGumWjpOvmd9f+f1/Ehv4ElkQJXBQWFUQZgBprCSetxJ/G1npmqNwpN
8u1xqOWz+yi4NaDbHbPfrbbJUqtRH02ljsm0rVKVXOTjdMsH8I27WLvgOD1fyAkO
NwIDAQAB
-----END PUBLIC KEY-----""", 
            """-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC1D7pi1jYVYqbo
iss0oKlM3GWZZALqKaT1+S46bo+5qv/9ChBPohqox3NrJmaaxGSBeo2+PT5dnc45
/dKZ4pMbSuk2vvOh92MoHCC56EMD1GZ3OSeKMsXzgJB3lU5Pk+b88BkntvOMuNuG
vcikKyAHxexmb31J2QjQLEBwz6bqj5qVuvkDT1DRYYB7QO7YRz8t/DzditUXCuDC
sUOeXfYhHZ7qO5v6Ma6ZaOk6+Z31/5/X8SG/gSWRAlcFBYVRBmAGmsJJ63En8bWe
mao3Ck3y7XGo5bP7KLg1oNsds9+ttslSq1EfTaWOybStUpVc5ON0ywfwjbtYu+A4
PV/ICQ43AgMBAAECggEACs0I49t+d3EentGkxJtu7ghZwTg/mkNotUmrkc3FoiBK
zAf9KBr19yqKvpIYXdQoYLb0XKxfm4sN4dS76vUirGagGeVzOC6/SgW/iAeMc96I
TEVrD+nueBOryo5sEQA0L9OM1Jsr1TGz2spYfT6bVwteClBNS4n4Zh61q2Ufwm87
7Dh/+ZORze16C2Y/r/pUNhavSypmRxhCcy83bqIAdD1Thw3SzELVOANlTtydAeL3
31QSjLn2ClNy0ry7aLTxP+e+f6EPnTWWVOv+8jc5nEE6VljUVG0H1My15tKAYT39
IrHHTQOVLRFaambjobRaQvx1vlPxjrUyxN62pvSESQKBgQDYJ4M5U8pm0uLdImEZ
5Ev5umrnammNrytAfCapOhBreQRnFYXDfHuvreajVK8+wKdYdn1zkFawLX/OUud9
YQ9n6NUBzH/dcyHQoO7gH2CJBZxkPlkW5bemBJBDZvYZYl7K+b8EUoJo1P42qoaC
VcF2XYBip2JrlY6+MYMEqL3+3wKBgQDWcCeP4Q2U7w4s5jJuXIWOThYa86hWmQw3
T/W5JS7bm9XJkV9SUFs9Xd1m+85siKvyf0hGLhWu9f4nP0JUt+waJNhKG43flOjO
ugDXPYhzVp8ZsGg6H9zFdVv7Plwg3z4JwwqeRcdUICP92M21jABc7XeVa6IJfaai
qQZpSbbTqQKBgQDXT1yOQSGvFMe4YGN6yAbKBeAxDbWA1Yju3fwgu17Zvx0clbq9
hAUsdLv13AgIKR1IqBbEg3VmXpwdaEWAhasz5SAwf4SqkOGREI2BoJ+nPXiP/e7+
OOqbK5aMHUZs+KjV5LpaUtnmFKv4xhngQA3Kms6k9ni6E6qxV15byL4g3wKBgQCc
RX+PSuMq9kvOTLPT2Xk7C4zwd0DmWwKcDJl2I7LSN+7ExjxBMG5Nemou8rKsRa2J
O1jgTBVhO8PLtj4QnzhglRlKaGor1ckTXlnegek+pJGtlvFd6nppK+2sWvWovwfm
9Ux3q0Jn/EQ+ahD/jNd24VeUfKvJXthhEeyqLh4egQKBgEMy922YyaUJb1QH7+ih
SSUpf8WMrNLWdXMTu9wAXDej2K+wm6lnRVd6ADFzKYv/7YlnCX6xt/mxSJ8U1TfU
zEuG2trFoGW2ygPJPRwMS5ly0QvnsiyGtInQgKXnfgkzecC61alYbaAmL8Qd4RH7
nnbYKPP8UiCwg3SZMfMYIW8L
-----END PRIVATE KEY-----""", 'RS256')
        self.users_repository = UserRepository(self.db_context.engine)
        self.role_repository = RoleRepository(self.db_context.engine)
        self.product_repository = ProductRepository(self.db_context.engine)
        self.invoice_repository = InvoiceRepository(self.db_context.engine)