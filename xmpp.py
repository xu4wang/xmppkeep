#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import sleekxmpp
from sleekxmpp.componentxmpp import ComponentXMPP
import assistant

if sys.version_info < (3, 0):
    from sleekxmpp.util.misc_ops import setdefaultencoding
    setdefaultencoding('utf8')
else:
    raw_input = input

class EchoComponent(ComponentXMPP):
    def __init__(self, jid, secret, server, port):
        ComponentXMPP.__init__(self, jid, secret, server, port)
        self.add_event_handler("message", self.message)

    def message(self, msg):
        r = assistant.process_message_with_path(msg.get_from().bare,msg.get_to().user, msg["body"])
        msg.reply(r).send()

if __name__ == '__main__':
    xmpp = EchoComponent("wd.wx.alixpay.com", "alixpay", "127.0.0.1", "8888")
    xmpp.registerPlugin('xep_0030') # Service Discovery
    xmpp.registerPlugin('xep_0004') # Data Forms
    xmpp.registerPlugin('xep_0060') # PubSub
    xmpp.registerPlugin('xep_0199') # XMPP Ping

    # Connect to the XMPP server and start processing XMPP stanzas.
    if xmpp.connect():
        xmpp.process(block=True)
        print("Done")
    else:
        print("Unable to connect.")
