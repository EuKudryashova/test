gen_dict = {
    'flavors': None,
    'active_flavors': 'Flavour m1.tiny: RAM 512 disc 1,<br> Flavour m1.micro: RAM 64 disc ,<br> Flavour m1.medium: RAM 4096 disc 40,<br>Flavour m1.small: RAM 2048 disc 20',
    'most_used_flavors': 'm1.medium - 50%<br>m1.small - 50%',
    'volumes': """
        5 - <10Gb,<br>
        2 - <50Gb,<br>
        1 - <100Gb',

    """,
    'most_used_volumes': 0,
    'unattached': None,
    'images': """
        5 - <10Gb,<br>
        1 - <50Gb,
    """,
    'most_used_images': '100% < 10Gb',
    'unused': 0,
    'networks': 2,
    'routers': 5,
    'subnets': 0,
    'unassociated_ips': 0,
    'unattached_ips': 0
}


general_temp = """
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
<h1> MCV general resource statistic</h1>

<table>
 <th>METRIC</th>
  <th>VALUE</th>
         {% for key, value in result.iteritems() %}

            <tr>
               <td> {{ key }} </td>
               <td> {{ value }} </td>
            </tr>

         {% endfor %}
</table>
</body>
</html>

"""


from flask_table import Table, Col
from jinja2 import Template


# Declare your table
class GeneralTable(Table):
    metric = Col('METRIC')
    value = Col('VALUE')


# Get some objects
class Item(object):
    def __init__(self, metric, value):
        self.metric = metric
        self.value = value

items = gen_dict


template = Template(general_temp)
res = template.render(result=gen_dict)

# Print the html
erred = open('general.html', 'wr')
erred.write(res)
erred.close()