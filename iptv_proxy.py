import requests
import httpx
import re
import base64
from sanic import Sanic
import sanic.log
from sanic.log import logger
from sanic.request import Request
from sanic.response import json, text

config = sanic.log.LOGGING_CONFIG_DEFAULTS
config['handlers']['file'] = {
    "class" : "logging.handlers.RotatingFileHandler",
    "formatter": "generic",
    "filename": "iptv.log",
    "maxBytes": 1024000,
    "backupCount": 10
}
config['handlers']['file_access'] = {
    "class" : "logging.handlers.RotatingFileHandler",
    "formatter": "access",
    "filename": "iptv.log",
    "maxBytes": 1024000,
    "backupCount": 10
}
config['loggers']['sanic.root']['handlers'].append('file')
config['loggers']['sanic.access']['handlers'].append('file_access')
config['loggers']['sanic.error']['handlers'].append('file')
config['loggers']['sanic.server']['handlers'].append('file')
app = Sanic("iptv", log_config=config)
client = httpx.AsyncClient(timeout = httpx.Timeout(5.0, connect=2.0))

def match(url):
    address = 'http://192.168.3.37:6666/proxy/'
    m = re.match(r'(https?:\/\/)([a-z0-9\.\:]+)(.+\.php)', url)
    if m:
        return address + base64.urlsafe_b64encode(url.encode()).decode() + ".m3u8"
    else:
        return url

@app.get(r'/<m3u:[a-z]+.m3u>')
async def iptv(request, m3u):
    if m3u == "iptv.m3u":
        r = await client.get('https://mirror.ghproxy.com/https://raw.githubusercontent.com/Kimentanm/aptv/master/m3u/iptv.m3u')
        html = r.text
        html = '\n'.join([match(x) for x in html.split('\n')])
        return text(html)
    return text("")

@app.get('/proxy/<url>')
async def proxy(request: Request, url):
    logger.info('proxy: ' + url)
    if url:
        headers={"User-Agent": "AptvPlayer/1.1.4"}
        r = await client.get(base64.urlsafe_b64decode(url.replace(".m3u8","")).decode(), headers=headers)
        html = r.text
        logger.info('return: ' + html)
        return text(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6666, access_log=True)
