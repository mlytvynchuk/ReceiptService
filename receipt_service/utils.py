from mindee import Client
from django.conf import settings


def get_json_data_from_receipt(image_path) -> dict:
    client = Client(settings.MINDEE_TOKEN)
    receipt = client.parse_receipt(image_path).receipt
    data = {
        'total': receipt.total_incl.value,
        'category': receipt.category.value,
        'merchant_name': receipt.merchant_name.value,
        'date': receipt.date.value,
        'tax': receipt.total_tax.value,
    }
    return data


if __name__ == '__main__':
    image_path = '/Users/maksimlitvincuk/Desktop/learning/receipt_service/media/images/receipt.png'
    data = get_json_data_from_receipt(image_path)
    print(data)
