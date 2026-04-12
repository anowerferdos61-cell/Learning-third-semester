class Phone:
    price = 8000
    colour = "nevi_blue"
    brand = "oppo"

    def call(self):
        print("calling")
    def message(self,phone_number,message):
        text = f"sending message to {phone_number} with content: {message}"
        return text
    

my_phone = Phone()
print(my_phone)
print(my_phone.brand)
my_phone.call()
print(my_phone.message("1234567890","Hello, how are you?"))