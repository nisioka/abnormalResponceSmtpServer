import smtpd
import re
import asyncore

class AbnormalResponseSmtpServer(smtpd.SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        try:
            # メールアドレスの先頭文字をそのまま応答レスポンスとする。
            return re.match('^[0-9]*', mailfrom).group()
        except Exception as e:
            # デフォルトでは 250 Ok を返す。
            return None

server = AbnormalResponseSmtpServer(('127.0.0.1', 25), None)

asyncore.loop()