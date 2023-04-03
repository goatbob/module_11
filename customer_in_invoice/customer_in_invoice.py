"""
program: customer_in_invoice.py
author: kyle godwin
last date modified: 02 april 2023

Invoice class adds items to a library and
outputs and inventory listing all items, tax,
and total.
"""


class Invoice:

    def __init__(self, inv, cust, items={}):
        self.invoice = inv
        self.customer_info = cust
        self.items_with_price = items

    def __str__(self):
        return f"{self.invoice}; {self.customer_info}; {self.items_with_price}"

    def __repr__(self):
        return f"{self.invoice}, {self.customer_info}, {self.items_with_price}"

    def add_item(self, key_value):
        self.items_with_price.update(key_value)

    def create_invoice(self):
        tax = 0.06
        item_total = 0
        print(self.customer_info)
        for item in self.items_with_price:
            print(f"{item}: ${self.items_with_price[item]:.2f}")
            item_total = item_total + self.items_with_price[item]
        tax = item_total * tax
        invoice_total = item_total + tax
        print(f"Tax: ${tax:.2f}")
        print(f"Total: ${invoice_total:.2f}")


class Customer:

    def __init__(self, cust_id, l_name, f_name, ph_num, addr):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        phone_number_characters = set("1234567890-()")
        if not (name_characters.issuperset(l_name) and name_characters.issuperset(f_name)):
            raise ValueError
        if not phone_number_characters.issuperset(ph_num):
            raise ValueError
        if not isinstance(cust_id, int):
            raise ValueError
        self.customer_id = cust_id
        self.last_name = l_name
        self.first_name = f_name
        self.phone_number = ph_num
        self.address = addr

    def __str__(self):
        return (f"Customer #{self.customer_id}: {self.last_name}, {self.first_name} \n"
                f" {self.phone_number} \n {self.address}")

    def __repr__(self):
        return f"{self.customer_id} {self.last_name} {self.first_name} {self.phone_number} {self.address}"

    def display(self):
        return f"{self.customer_id} {self.last_name} {self.first_name} {self.phone_number} {self.address}"


if __name__ == "__main__":
    captain_mal = Customer(1, 'Reynolds', 'Mal', '123-456-7890', 'Firefly, somewhere in the verse')
    invoice = Invoice(1, captain_mal)
    invoice.add_item({'iPad': 799.99})
    invoice.add_item({'Surface': 999.99})
    invoice.create_invoice()
