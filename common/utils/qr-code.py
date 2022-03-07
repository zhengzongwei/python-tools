
import cv2
import qrcode


def make_qrcode(msg: str, path: str) -> bool:
    ret = True
    try:
        img = qrcode.make(msg)
        img.save(path)
    except Exception as e:
        ret = False
        print(e)

    return ret


def parse_qrcode(path: str) -> bool:
    ret = True
    try:
        img = cv2.imread(path)
        det = cv2.QRCodeDetector()
        value, bbox, straight_qrcode = det.detectAndDecode(img)
        print(value)
    except Exception as e:
        ret = False
        print(e)
    return ret


if __name__ == "__main__":
    # make_qrcode("hello world", "./qrcode.png")
    parse_qrcode("./qrcode.png")