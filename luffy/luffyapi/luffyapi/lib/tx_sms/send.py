from qcloudsms_py import SmsSingleSender
from luffyapi.lib.tx_sms import settings
from luffyapi.utils.logger import log


def get_code():
    import random
    s_code = ''
    for i in range(4):
        s_code += str(random.randint(0, 9))
    return s_code


def send_message(phone, code):
    sender = SmsSingleSender(settings.appid, settings.appkey)
    params = [code, "3"]
    try:
        result = sender.send_with_param(86, phone, settings.template_id,
                                        params, sign=settings.sms_sign, extend="", ext="")
        if result.get('result') == 0:
            pass
    except Exception as e:
        log.error(f'手机号: {phone},短信发送失败')
