import bs4


def processInventory():
    the_file = open('inventory.txt', 'r')
    inventory = the_file.read()
    num_dict = {}
    soup = bs4.BeautifulSoup(inventory, 'html.parser')
    str_soup = str(soup)
    list_soup = str_soup.split('<br/>')
    new_list = [each.strip().split(maxsplit=1) for each in list_soup if '<' not in each]
    for num, name in new_list:
        num_dict[name] = int(num)
    return num_dict


def processPrices():
    the_file = open('standard.txt', 'r')
    standard_gold = the_file.read()
    the_file_2 = open('modern_one.txt', 'r')
    modern_one = the_file_2.read()
    the_file_3 = open('modern_two.txt', 'r')
    modern_two = the_file_3.read()
    price_dict = {}
    stn_soup = bs4.BeautifulSoup(standard_gold, 'html.parser')
    mod1_soup = bs4.BeautifulSoup(modern_one, 'html.parser')
    mod2_soup = bs4.BeautifulSoup(modern_two, 'html.parser')
    stn_dts = stn_soup.select('dt')
    mod1_dts = mod1_soup.select('dt')
    mod2_dts = mod2_soup.select('dt')
    stn_dds = stn_soup.select('dd')
    mod1_dds = mod1_soup.select('dd')
    mod2_dds = mod2_soup.select('dd')
    stn_count = len(stn_dts)
    mod1_count = len(mod1_soup.select('dt'))
    mod2_count = len(mod2_soup.select('dt'))
    for i in range(stn_count):
        price_dict[stn_dts[i].text] = float(stn_dds[i].text)
    for i in range(mod1_count):
        price_dict[mod1_dts[i].text] = float(mod1_dds[i].text)
    for i in range(mod2_count):
        price_dict[mod2_dts[i].text] = float(mod2_dds[i].text)

    return price_dict

if __name__ == '__main__':
    the_file = open('december7.txt', 'w')
    inventory = processInventory()
    prices = processPrices()
    str_to_join = [each + ' ' + str(prices[each]) for each in prices if each in inventory]
    str_to_join = sorted(str_to_join)
    the_file.write('\n'.join(str_to_join))