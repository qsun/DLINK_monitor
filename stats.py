#!/usr/bin/env python

from datetime import datetime
import requests
import mechanize
import cookielib
import sys
from bs4 import BeautifulSoup
import logging

try:
    import code
except Exception:
    pass


def get_stats(ip, username, password):
    logging.debug("GetStats for %s %s[%s]" % (ip, username, password,))
    br = mechanize.Browser()

    cj = cookielib.LWPCookieJar()
    br.set_cookiejar(cj)
    # br.set_debug_redirects(True)
    # br.set_debug_responses(True)
    # br.set_debug_http(True)
    
    br.set_handle_robots(False)
    br.addHeaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36')]
    br.open('http://' + ip + '/login.html')
    logging.debug('open done. Title: ' + br.title())
    logging.debug('select form')
    
    br.select_form(name='frmLogin')
    br['username'] = [username,]
    br['password'] = password
    br['validateCode'] = ''
    response = br.submit()
    
    logging.debug(response.info())
    logging.debug('login done. Title: ' + br.title())
    logging.debug('now redirect to stats')
    
    response = requests.get('http://' + ip + '/statsifcwanber.html')
    logging.debug("Response: " + str(len(response.content)))
    bs = BeautifulSoup(response.content)
    # code.interact(local=locals())
    logging.debug("rate: " + str(bs.select('#statsxDslRate')[0].parent))

    _, att_down, att_up = bs.select('#statsxDslAttenuation')[0].parent.select('td')
    _, rx, tx = bs.select('#statsxDslRate')[0].parent.select('td')

    logging.debug("Rate: %s,%s" % (str(rx.text), str(tx.text),))
    logging.debug("Att: %s,%s" % (str(att_down.text), str(att_up.text),))
    
    return dict(
        att_down=att_down.text,
        att_up=att_up.text,
        rx=rx.text,
        tx=tx.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %H:%M',
    )
    
    stats = get_stats(sys.argv[1], sys.argv[2], sys.argv[3])
    print "%s,%s,%s,%s,%s" % (datetime.now(), 
                              stats['att_down'],
                              stats['att_up'],
                              stats['rx'],
                              stats['tx'],)
                              
    
