import requests
from bs4 import BeautifulSoup as bs
from bin.core import delete_last_file, delete_specific_folder, get_request_from_link
from bin.helper import printAll


def star_tech_website_parser(data, link, folder_parent_path, identifier):
    highest_page = -1

    req = requests.get(link).text
    soup = bs(req, 'html.parser')
    pagination_lists = soup.find(name = 'ul', class_ = 'pagination')

    for li in pagination_lists:
        if li.text.isdigit() and int(li.text) > highest_page:
            highest_page = int(li.text)

    for page in range(highest_page + 1):
        if page == 0: continue
        req = get_request_from_link(folder_parent_path, str(page), link, identifier, '&page=')

        soup = bs(req, 'html.parser')
        div_tags = soup.find_all(name = 'div', class_ = 'p-item-details')

        for div in div_tags:
            data['from'].append( )
            # get the product titles
            data['headers'].append(div.h4.text)
            # get the single product links
            data['header_links'].append(div.h4.a['href'])
            uls = div.div.ul # has many (4) li tags, each is one description contained by ul
            description_text = ''
            # loop through the descriptions (li) in the ul
            for li in uls:
                # string contatenation after removing '\n'
                description_text += li.text.replace('\n', ', ')
            data['header_descriptions'].append(description_text)
            spans = div.div.findNext('div').children # can contain two spans, one for old price and one for new
            prices = 0
            old_prices = 0
            # loop through new and old prices in the span
            for span in spans:
                if len(span.text) > 1:
                    # print(span.has_attr('class'), span.get('class')['0'])
                    if span.has_attr('class') and span.get('class')[0] == 'price-old': 
                        old_prices = span.text.replace('৳', '')
                    elif not span.has_attr('class'): old_prices = None
                    prices = span.text.replace('৳', '')

            data['present_prices'].append(prices)
            data['old_prices'].append(old_prices)

    return data

def ryan_computer_website_parser(data, link, folder_parent_path, identifier):
    highest_page = -1

    req = requests.get(link).text
    soup = bs(req, 'html.parser')
    pagination_lists = soup.find(name = 'ol', class_ = '') # or pagination_lists = soup.find(name = 'ol', class_ = '').children
    for li in pagination_lists:
        if li.text.isdigit() and int(li.text) > highest_page:
            highest_page = int(li.text)

    for page in range(highest_page + 1):
        if page == 0: continue
        req = get_request_from_link(folder_parent_path, str(page), link, identifier, '&page=')

        soup = bs(req, 'html.parser')
        a_tags = soup.find_all(name = 'a', class_ = 'product-title-grid')
        for a_tag in a_tags:
            data['from'].append(identifier)
            # as headers are coming in partial maybe go inside the link and bring out the real header next
            data['headers'].append(a_tag.text)
            data['header_links'].append(a_tag['href'])
            data['header_descriptions'].append(None)

        old_prices = soup.find_all(name='span', class_='old-price')
        present_prices = soup.find_all(name='span', class_='price')

        for price in old_prices:
            data['old_prices'].append(price.text.strip())
        for price in present_prices:
            data['present_prices'].append(price.text.strip())

    return data


def global_brand_parser(data, link, folder_parent_path, identifier):
    page_num = 1
    while True:
        req = get_request_from_link(folder_parent_path, str(page_num), link, identifier, '&page=')
        soup = bs(req, 'html.parser')
        main_products_wrapper = soup.find(name='div', class_='main-products-wrapper')

        # break out from the loop and delete the last file stored
        if len(main_products_wrapper) <= 0:
            delete_last_file(identifier, str(page_num))
            break

        page_num += 1

        title_divs = soup.find_all(name='div', class_='name')

        for div in title_divs:
            data['from'].append(identifier)
            data['headers'].append(div.text)
            data['header_links'].append(div.a['href'])

        desc_divs = soup.find_all(name='div', class_='shortinfo')

        for div in desc_divs:
            # only take the first ul 
            description_text = ''
            for li in div.ul:
                description_text += li.text.strip() + ' '
            
            data['header_descriptions'].append(description_text)

        price_divs = soup.find_all(name='span', class_='price-normal')

        for price in price_divs:
            price = price.text.replace('৳', '')
            if price == '0':
                data['present_prices'].append(None)
            else:
                data['present_prices'].append(price.strip())
            data['old_prices'].append(None)

    # delete_specific_folder(identifier)
    return data

def computer_mania_parser(data, link, folder_parent_path, identifier):
    page_num = 1
    while True:
        req = get_request_from_link(folder_parent_path, str(page_num), link, identifier, '/page/')
        soup = bs(req, 'html.parser')

        results = soup.find_all(name='h3', class_='woocommerce-loop-product__title')

        # break out from the loop and delete the last file stored
        if len(results) <= 0:
            delete_last_file(identifier, str(page_num))
            break

        page_num += 1

        for h3 in results:
            data['from'].append(identifier)
            data['headers'].append(h3.a.text)
            data['header_links'].append(h3.a['href'])
            data['header_descriptions'].append(None)


            # findNext finds the next to itself specifying class and name like find_all, find and soup.select
            span = h3.findNext(name='span', class_='price')

            if span:
                # basically contents has length 3 even though there are two tags (weird but true)
                # probably there is a hidden tag
                contents = span.contents
                # In case of 3 tags
                if len(contents) > 1:
                    data['old_prices'].append(contents[0].span.bdi.text.replace('৳', ''))
                    data['present_prices'].append(contents[2].span.bdi.text.replace('৳', ''))
                # in case of 1 tag
                elif len(contents) == 1:
                    # the text is found at a different nested tag
                    if len(contents[0].text):
                        data['present_prices'].append(contents[0].text.replace('৳', ''))
                    else: 
                        data['present_prices'].append(None)
                    data['old_prices'].append(None)
                # edge case handled (might not be needed but just in case)
                else:
                    data['present_prices'].append(None)
                    data['old_prices'].append(None)
            else:
                data['present_prices'].append(None)
                data['old_prices'].append(None)

    return data

        