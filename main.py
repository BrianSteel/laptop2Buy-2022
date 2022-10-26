import pandas as pd
from pathlib import Path
from bin.core import should_make_new_link_req


from bin.helper import printAll
from bin.parsers import computer_mania_parser, global_brand_parser, ryan_computer_website_parser, star_tech_website_parser


data = {
    'header_links': [],
    'headers': [],
    'header_descriptions': [],
    'present_prices': [],
    'old_prices': [],
    'from': []
}
folder_parent_path = Path("main.py").parent.absolute()

# fix old price, add loop for links and add if links already visited do not call them again
# computer village
# global brands
# one more
# loop through the array and group all the same computers and then give them all one name and compare their prices


inputs = {
    # startech
    0: {
        'link': 'https://www.startech.com.bd/laptop-notebook/laptop?limit=',
        'limit': '90',
        'identifier': 'StarTech-'
    },
    # ryans
    1: {
        'link': 'https://www.ryanscomputers.com/category/laptop-all-laptop?limit=',
        'limit': '108',
        'identifier': 'Ryans-'
    },
    # global
    2: {
        'link': 'https://globalbrand.com.bd/all-laptop?limit=',
        'limit': '100',
        'identifier': 'Global-' 
    },
    # computer mania
    3: {
        'link': 'https://computermania.com.bd/product-category/laptop',
        'identifier': 'ComputerMania-' 
    }
}

# # even if you dont return variable data will be modified for all functions and will have all the data
# data = star_tech_website_parser(data, inputs[0]['link'] + inputs[0]['limit'], folder_parent_path, inputs[0]['identifier'])
# data = ryan_computer_website_parser(data, inputs[1]['link'] + inputs[1]['limit'], folder_parent_path, inputs[1]['identifier'])
# data = global_brand_parser(data, inputs[2]['link'] + inputs[2]['limit'], folder_parent_path, inputs[2]['identifier'])
# data = computer_mania_parser(data, inputs[3]['link'], folder_parent_path, inputs[3]['identifier'])




# # set display of column width of pd to full length
# pd.set_option('display.max_colwidth', 22) # None
# pd.set_option('display.max_columns', 10) 
# pd.set_option('display.max_rows', 1000) 
# data = pd.DataFrame({'Title': data['headers'], 'Links': data['header_links'], 'Description': data['header_descriptions'],'Present Prices': data['present_prices'], 'Old Price': data['old_prices'], 'From': data['from']})

# data.to_csv('results.csv')

print(should_make_new_link_req())



