import json

from django.shortcuts import render
import uuid
import os
from images.models import UploadImage
from receipt_service.utils import get_json_data_from_receipt


def receipt_upload_view(request):
    context = {}
    if request.method == 'POST':
        receipt_file = request.FILES['receipt_file']
        uploaded_image = UploadImage.objects.create(title=str(uuid.uuid4()), image=receipt_file)

        image_path = uploaded_image.image.path
        json_data = get_json_data_from_receipt(image_path)
        context = {
            'json_data': json.dumps(json_data, indent=4)
        }

        # Remove image
        uploaded_image.delete()
        os.remove(image_path)

    return render(request, 'receipt_upload.html', context=context)
