import odoolib


connection = odoolib.get_connection(hostname ="otrusa.odoo.com",
    database = "otrusa-otrusa-331982",
    login = "torfun@otrusa.com",
    password ="Otrusa@11201",
    port = 443,
    protocol = "jsonrpcs"
)

odoo_model_data = connection.get_model('product.template')

# odoo_records = odoo_model_data.search_read(['&',('create_uid', '=',65),('list_price','>',1200)], ['id','name','list_price','create_uid'])

# Find Average List Price

odoo_records = odoo_model_data.search_read(['&',('create_uid', '=',65),('list_price','>',1200)], ['id','name','list_price'])
print(odoo_records)

list_price = []

for i in odoo_records:
    value = i.get('list_price')
    list_price.append(value)


print(list_price)

total = sum(list_price)
length = len(list_price)
average = total/length
print(average)



