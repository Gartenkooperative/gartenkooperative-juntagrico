# Mailer that limits the max number of recipients, as the email servers don't like so many recipients.

MAX_EMAILS = 20
class Mailer:
    def send(msg):
        to = msg.to[:]
        bcc = msg.bcc[:]
        cc = msg.cc[:]
        while len(to) + len(bcc) + len(cc):
            if (len(to) > MAX_EMAILS):
                msg.to = to[:19]
                del to[:19]
            else:
                msg.to = to
                to = []
            if (len(cc) > MAX_EMAILS):
                msg.cc = cc[:19]
                del cc[:19]
            else:
                msg.cc = cc
                cc = []
            if (len(bcc) > MAX_EMAILS):
                msg.bcc = bcc[:19]
                del bcc[:19]
            else:
                msg.bcc = bcc
                bcc = []
            msg.send()
