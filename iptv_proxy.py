from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request as urllib2
import logging
import re
import gzip

logging.basicConfig()
logger = logging.getLogger(__name__)

class ProxyHandler(BaseHTTPRequestHandler):
    def match(self, url):
        address = 'http://' + str(self.server.server_address[0]) + ":" + str(self.server.server_address[1]) + '/'
        m = re.match(r'(https?:\/\/)([a-z0-9\.\:]+)(.+\.php)', url)
        if m:
            return url.replace(m.group(0), address + m.group(0))
        else:
            return url
    def proxy(self):
        print('请求:', self.path)
        print('请求头:', self.headers)
        print('请求方法:', self.command)
        if self.command == 'POST':
            req = self.rfile.read(int(self.headers['content-length']))
            print('请求体:', req.decode('utf-8'))
        else:
            req = None
        if self.path.endswith('.m3u'):
            request = urllib2.Request(url='https://mirror.ghproxy.com/https://raw.githubusercontent.com/Kimentanm/aptv/master/m3u/iptv.m3u', method=self.command, data=req)
            with urllib2.urlopen(request) as f:
                print(f.status, f.headers)
                self.send_response(f.status)
                for (key, value) in f.headers.items():
                    if key == 'Content-Type':
                        self.send_header(key, value)
                self.end_headers()
                data = f.read()
                if f.headers['Content-Encoding'] == 'gzip':
                    data = gzip.decompress(data)
                data = data.decode('utf-8')
                data = '\n'.join([self.match(x) for x in data.split('\n')])
                # data = data.decode('utf-8').replace('http://live.aptvapp.com', 'http://192.168.3.32:6666')
                self.wfile.write(data.encode('utf-8'))
        elif self.path.startswith('/http'):
            header = {}
            header['User-Agent'] = 'AptvPlayer/1.1.4'
            request = urllib2.Request(self.path[1:], headers=header, method=self.command, data=req)
            with urllib2.urlopen(request) as f:
                print(f.status, f.headers)
                self.send_response(f.status)
                for (key, value) in f.headers.items():
                    if key == 'Content-Type':
                        self.send_header(key, value)
                self.end_headers()
                data = f.read()
                if f.headers['Content-Encoding'] == 'gzip':
                    data = gzip.decompress(data)
                print(data.decode('utf-8'))
                self.wfile.write(data)

    def do_GET(self):
        self.proxy()


    def do_POST(self):
        self.proxy()


def run():
    server_address = ('127.0.0.1', 6666)
    httpd = HTTPServer(server_address, ProxyHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    run()
