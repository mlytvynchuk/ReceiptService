import re

import cv2
import pytesseract as pytesseract
from pytesseract import Output


def get_json_data_from_receipt(file_path):
    img = cv2.imread('receipt.jpg')
    d = pytesseract.image_to_data(img, output_type=Output.DICT)
    n_boxes = len(d['level'])
    for i in range(n_boxes):
        (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
        img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

    extracted_text = pytesseract.image_to_string(img, lang='en')
    splits = extracted_text.splitlines()
    restaurant_name = splits[0] + '' + splits[1]
    receipt_ocr = {}
    lines_with_chf = []
    date_pattern = r'(0[1-9]|[12][0-9]|3[01])[.](0[1-9]|1[012])[.](19|20)\d\d'
    date = re.search(date_pattern, extracted_text).group()
    receipt_ocr['date'] = date
    receipt_ocr['restaurant_name'] = restaurant_name
    for line in splits:
        if re.search(r'$', line):
            lines_with_chf.append(line)

    items = []
    for line in lines_with_chf:
        print(line)
        if re.search(r'Incl', line):
            continue
        if re.search(r'Total', line):
            total = line
        else:
            items.append(line)

    total = total.split('CHF')[-1]

    # Store the results in the dict
    receipt_ocr['total'] = total

    return receipt_ocr
