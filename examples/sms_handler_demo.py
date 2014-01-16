#!/usr/bin/env python

"""\
Demo: handle incoming SMS messages by replying to them

Simple demo app that listens for incoming SMS messages, displays the sender's number
and the messages, then replies to the SMS by saying "thank you"
"""

from __future__ import print_function

import logging

PORT = '/dev/ttyUSB1'
BAUDRATE = 9600
PIN = None # SIM card PIN (if any)

from gsmmodem.modem import GsmModem
i =0
def handleSms(sms):
    print(u'== SMS message received ==\nFrom: {0}\nTime: {1}\nMessage: {2}\n'.format(sms.number, sms.time, sms.text))
    
def main():
    print('Initializing modem...')
    # Uncomment the following line to see what the modem is doing:
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    modem = GsmModem(PORT, BAUDRATE, smsReceivedCallbackFunc=handleSms)
    modem.smsTextMode = True 
    modem.connect(PIN)
    print('Waiting for SMS message...')    
    try:    
        modem.rxThread.join(2**31) # Specify a (huge) timeout so that it essentially blocks indefinitely, but still receives CTRL+C interrupt signal
    finally:
        modem.close();

if __name__ == '__main__':
    main()
