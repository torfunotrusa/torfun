import odoolib
print(odoo_records)

connection = odoolib.get_connection(hostname ="otrusa.odoo.com",
    database = "otrusa-otrusa-331982",
    login = "torfun@otrusa.com",
    password ="Otrusa@11201",
    port = 443,
    odoo_protocol = "jsonrpcs"
)

odoo_model_data = connection.get_model('product.template')

odoo_records = odoo_model_data.search_read([('id', '=',41452)], {'fields':['id','name','list_price']})

