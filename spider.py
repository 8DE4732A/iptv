from bs4 import BeautifulSoup
import requests
import sys
import time

def parse_list():
    cookies = {
        '_ga': 'GA1.1.1182438.1714223248',
        'HstCfa4853344': '1714223251554',
        'HstCmu4853344': '1714223251554',
        'HstCnv4853344': '1',
        'REFERER': '14203174',
        'ckip1': '113.118.45.27%7C113.118.45.220%7C120.7.86.32%7C221.205.20.224%7C221.234.25.122%7C110.7.130.140%7C121.24.99.40%7C218.24.193.146',
        'ckip2': '117.32.85.181%7C117.32.85.254%7C223.10.12.188%7C220.191.39.87%7C27.11.255.229%7C183.191.233.139%7Cmail.long365.net%7C183.191.209.209',
        'HstCla4853344': '1714227994606',
        'HstPn4853344': '17',
        'HstPt4853344': '17',
        'HstCns4853344': '3',
        '_ga_JNMLRB3QLF': 'GS1.1.1714223247.1.1.1714227995.0.0.0',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga=GA1.1.1182438.1714223248; HstCfa4853344=1714223251554; HstCmu4853344=1714223251554; HstCnv4853344=1; REFERER=14203174; ckip1=113.118.45.27%7C113.118.45.220%7C120.7.86.32%7C221.205.20.224%7C221.234.25.122%7C110.7.130.140%7C121.24.99.40%7C218.24.193.146; ckip2=117.32.85.181%7C117.32.85.254%7C223.10.12.188%7C220.191.39.87%7C27.11.255.229%7C183.191.233.139%7Cmail.long365.net%7C183.191.209.209; HstCla4853344=1714227994606; HstPn4853344=17; HstPt4853344=17; HstCns4853344=3; _ga_JNMLRB3QLF=GS1.1.1714223247.1.1.1714227995.0.0.0',
        'Referer': 'http://tonkiang.us/hotellist.html?s=223.10.16.11:8085',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }
    r = requests.get('http://tonkiang.us/', cookies=cookies, headers=headers, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    parse_result = {}
    for box in soup.select('div.box'):
        box_name = box.find('div').string.strip()
        items = [x.string for x in box.select('span > a')]
        parse_result[box_name] = items
    print(parse_result)
    return parse_result

def search_ip(ip: str):
    cookies = {
        '_ga': 'GA1.1.1182438.1714223248',
        'HstCfa4853344': '1714223251554',
        'HstCmu4853344': '1714223251554',
        'HstCnv4853344': '1',
        'REFERER': '14203174',
        'HstCns4853344': '3',
        '_ga_JNMLRB3QLF': 'GS1.1.1714223247.1.1.1714228008.0.0.0',
        'HstCla4853344': '1714228008223',
        'HstPn4853344': '18',
        'HstPt4853344': '18',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga=GA1.1.1182438.1714223248; HstCfa4853344=1714223251554; HstCmu4853344=1714223251554; HstCnv4853344=1; REFERER=14203174; HstCns4853344=3; _ga_JNMLRB3QLF=GS1.1.1714223247.1.1.1714228008.0.0.0; HstCla4853344=1714228008223; HstPn4853344=18; HstPt4853344=18',
        'Referer': 'http://tonkiang.us/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
    }

    params = {
        's': ip,
    }
    r = requests.get('http://tonkiang.us/hoteliptv.php', params=params, cookies=cookies, headers=headers, verify=False)
    soup = BeautifulSoup(r.text, 'html.parser')
    for b in soup.select('div.channel > a > b'):
        b.img.extract()
        return b.string.strip()
    return None

def parse(address: str):
    cookies = {
        '_ga': 'GA1.1.1182438.1714223248',
        'HstCfa4853344': '1714223251554',
        'HstCmu4853344': '1714223251554',
        'HstCnv4853344': '1',
        'HstCns4853344': '2',
        'REFERER2': 'NzTbMrzaMbzcAO0O0O',
        'REFERER1': 'NzTbkryaMbTcIO0O0O',
        'HstCla4853344': '1714224959059',
        'HstPn4853344': '15',
        'HstPt4853344': '15',
        '_ga_JNMLRB3QLF': 'GS1.1.1714223247.1.1.1714225315.0.0.0',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en,zh-CN;q=0.9,zh;q=0.8',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': '_ga=GA1.1.1182438.1714223248; HstCfa4853344=1714223251554; HstCmu4853344=1714223251554; HstCnv4853344=1; HstCns4853344=2; REFERER2=NzTbMrzaMbzcAO0O0O; REFERER1=NzTbkryaMbTcIO0O0O; HstCla4853344=1714224959059; HstPn4853344=15; HstPt4853344=15; _ga_JNMLRB3QLF=GS1.1.1714223247.1.1.1714225315.0.0.0',
        'Referer': 'http://tonkiang.us/hotellist.html?s=223.10.16.11:8085',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    }

    r = requests.get(f'http://tonkiang.us/alllist.php?s={address}&c=false', cookies=cookies, headers=headers, verify=False)
    parse_result = []
    soup = BeautifulSoup(r.text, 'html.parser')
    for result in soup.select('div.result'):
        name_div = result.find('div', style="float: left;")
        m3u8_div = result.find('td', style="padding-left: 6px;")
        if name_div and m3u8_div:
            parse_result.append({
                "name": name_div.string,
                "m3u": m3u8_div.string.strip()
            })
    return parse_result
    
def gen_m3u(group):
    with open(sys.path[0] + "/public/iptv.m3u", "w+", encoding='utf-8') as f:
        f.write('#EXTM3U\n')
        f.write(f'#EXT-X-VERSION {int(time.time())}\n')
        f.write('\n')
        index = 1
        for (group_name, parse_result) in group.items():
            for one in parse_result:
                f.write(f'''#EXTINF:-1,tvg-id="{index}-{one['name']}" tvg-name="{index}-{one['name']}" group-title="{group_name}",{one['name']}\n''')
                f.write(one['m3u'])
                f.write('\n')
            index = index + 1


if __name__ == "__main__":
    result = {}
    ps = []
    parse_list = parse_list()
    for (group_name, items) in parse_list.items():
        if group_name == 'Multicast IP':
            ps.extend([search_ip(ip) for ip in items])
    for (group_name, items) in parse_list.items():
        if group_name == 'Hotel IPTV':
            ps.extend([search_ip(ip) for ip in items])
    print('ips', ps)
    for x in [x for x in ps if x is not None]:
        try:
            result[x] = parse(x)
        except Exception as e:
            print(e)
    gen_m3u(result)
