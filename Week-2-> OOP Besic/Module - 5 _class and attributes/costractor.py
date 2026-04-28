class Phone:
    manufacturer = "oppo"

    def __init__(self, owner_name, price, colour, brand):
        self.owner_name = owner_name
        self.price = price
        self.colour = colour
        self.brand =brand

    def send_message(self, phone_number, message):
        text = f"sending message to {phone_number} with content: {message}"
        return text

my_phn = Phone("anower",8000,"nevi_blue","oppo")
print(my_phn.owner_name,my_phn.price,my_phn.colour,my_phn.brand)

her_phn = Phone("Samira",12000," balck", "iphone")
print(her_phn.owner_name,her_phn.price,her_phn.colour,her_phn.brand)

print(her_phn.send_message("1234567890","Hello, how are you?"))

dad_phn = Phone("Anower's dad", 15000, "white", "samsung")
print(dad_phn.owner_name, dad_phn.price, dad_phn.colour, dad_phn.brand)