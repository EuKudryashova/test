from jinja2 import Template

erred_temp = """
<!DOCTYPE html>
<html>
<head>
<style>
table{
    border: 2px solid black;
    border-collapse: collapse;
    width: 90%

}
th, td {
    padding: 15px;
    border: 1px solid black;
}
</style>
</head>
<body>
<h1> MCV error resource statistic</h1>
{{table}}
<h5>*** if table is empty it means that no resources with error state was found</h5>
</body>
</html>

"""


test_dict = [{'type': 'server', 'id': '565431-352343434-2132132', 'name': 'ek_vm1', 'status': 'ERROR', 'other': ''},
                    {'type': 'server', 'name': 'ek_vm2',  'id': '565431-35234dsg434-2132132', 'status': 'ERROR', 'other': ''},
                    {'type': 'server', 'name': 'ek_vm3', 'id': 'ddasfsdf-35234dsg434-2132132', 'status': 'ERROR', 'other': ''},
          {'type': 'image', 'id': 'sdafasfsafasfasfasf', 'name': 'test', 'status': 'ERROR', 'other': 'updated at 05.06.2016'},
                    {'type': 'image', 'id': 'sdaf2131231asfasf', 'name': 'test2', 'status': 'ERROR', 'other': 'updated at 07.06.2016'},
                    {'type': 'image', 'id': 'sdafa2134123asfasf', 'name': 'test3', 'status': 'ERROR', 'other': 'updated at 08.06.2016'},
          {'type': 'volume', 'id': '4234223rtet23e5t32e5', 'name': 'qq', 'status': 'ERROR', 'other': 'is bootable False'},
                    {'type': 'volume', 'id': '42342234545645t32e5', 'name': 'qq', 'status': 'ERROR', 'other': 'is bootable False'},
                    {'type': 'port', 'id': '4234223rtet23e5t32e5', 'name': 'qq', 'status': 'ERROR', 'other': 'Fixed IPs 172.16.0.2'}]



from flask_table import Table, Col
from jinja2 import Template

# Declare your table
class ErredTable(Table):
    type = Col('TYPE')
    name = Col('NAME')
    id = Col('ID')
    status = Col('STATUS')
    other = Col('OTHER')


# Get some objects
class Item(object):
    def __init__(self, type, resource):
        self.name = resource['name']
        self.type = type
        self.id = resource['id']
        self.status = resource['status']
        self.other = resource['other']



items = test_dict



# Populate the table
table = ErredTable(items)
table_html = table.__html__()
template = Template(erred_temp)
res = template.render(table=table_html)

# Print the html
erred = open('erred.html', 'wr')
erred.write(res)
erred.close()