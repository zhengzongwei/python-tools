import cv2
import qrcode

"""
手机自动连接 Wi-Fi 二维码生成格式
WIFI:T:WPA;S:MM;P:123456;H:true;  （H:为隐藏SSID，可选)

WIFI:S:MM;T:nopass;P:123456;
----------------------------------------------
{WIFI:T:WPA;S:mynetwork;P:mypass;;}

相关参数说明:

参数  例子  说明
T   WPA 认证类型： WEP 或WPA, ‘nopass’ 代表无需认证
S   network 无线网络的 SSID. (例如 “ABCD”)
P   mypass  无线网络的密码，如果无需认证则忽略此项 (例如 “pass”)
H   true    可选。针对隐藏了SSID的网络

"""


class QRCode(object):
    def __init__(self):
        pass

    @staticmethod
    def generate_qrcode(data, file_name='qrcode.png'):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        img.save(file_name)
        print(f"QR code saved as {file_name}")

    @staticmethod
    def read_qrcode(file='qrcode.png'):
        img = cv2.imread(file)
        qr_detector = cv2.QRCodeDetector()
        retval, points, straight_qrcode = qr_detector.detectAndDecode(img)
        if retval:
            print("Decoded message: ", retval)
        else:
            print("QR Code not detected")

        return retval


# def make_qrcode(msg: str, path: str) -> bool:
#     ret = True
#     try:
#         img = qrcode.make(msg)
#         img.save(path)
#     except Exception as e:
#         ret = False
#         print(e)
#
#     return ret
#
#
# def parse_qrcode(path: str) -> bool:
#     ret = True
#     try:
#         img = cv2.imread(path)
#         det = cv2.QRCodeDetector()
#         value, bbox, straight_qrcode = det.detectAndDecode(img)
#         print(value)
#     except Exception as e:
#         ret = False
#         print(e)
#     return ret
#
#
# if __name__ == "__main__":
#     # make_qrcode("hello world", "./qrcode.png")
#     parse_qrcode("./qrcode.png")


if __name__ == '__main__':
    # QRCode().generate_qrcode("hello,world")
    QRCode().read_qrcode("qrcode.png")
