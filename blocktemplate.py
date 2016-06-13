__author__ = 'ekudryashova'

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
<h1> MCV object storage speed test results</h1>
{{table}}

</body>
</html>

"""


test_dict = [
    {'attempt': 1, 'node': 'node-13', 'action': 'read', 'speed': '43,5Mb/s'},
    {'attempt': 2, 'node': 'node-13', 'action': 'read', 'speed': '33,6Mb/s'},
    {'attempt': 3, 'node': 'node-13', 'action': 'read', 'speed': '38,3Mb/s'},
    {'attempt': 'average', 'node': 'node-13', 'action': 'read', 'speed': '43,5Mb/s'},

     {'attempt': 1, 'node': 'node-13', 'action': 'write', 'speed': '80,5Mb/s'},
    {'attempt': 2, 'node': 'node-13', 'action': 'write', 'speed': '83,1Mb/s'},

     {'attempt': 3, 'node': 'node-13', 'action': 'write', 'speed': '85,7Mb/s'},
    {'attempt': 'average', 'node': 'node-13', 'action': 'write', 'speed': '82,9Mb/s'},


]



from flask_table import Table, Col
from jinja2 import Template

# Declare your table
class ObjTable(Table):
    attempt = Col('ATTEMPT')
    node = Col('NODE')
    action = Col('ACTION')
    speed = Col('RESULT')





items = test_dict



# Populate the table
table = ObjTable(items)
table_html = table.__html__()
template = Template(erred_temp)
res = template.render(table=table_html)

# Print the html

erred = open('object.html', 'wr')
erred.write(res)
erred.close()