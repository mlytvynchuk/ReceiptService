import json

from django.shortcuts import render

from receipt_service.utils import get_json_data_from_receipt


def receipt_upload_view(request):
    context = {}
    if request.method == 'POST':
        receipt_file = request.FILES['receipt_file']
        json_data = get_json_data_from_receipt(receipt_file)
        context = {
            'json_data': json.dumps(json_data, indent=4)
        }
    return render(request, 'receipt_upload.html', context=context)
