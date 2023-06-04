from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ScannedImage
import pytesseract
from PIL import Image

class ImageConverterView(APIView):
    def post(self, request):
        image_file = request.FILES['image']
        scanned_image = ScannedImage.objects.create(image=image_file)

        # Open the uploaded image using PIL
        image = Image.open(image_file)

        # Convert the image to grayscale for better OCR accuracy
        image = image.convert('L')

        # Apply OCR using Tesseract
        converted_data = pytesseract.image_to_string(image)

        response_data = {
            'message': 'Image scanned and converted successfully.',
            'converted_data': converted_data.strip()
        }

        return Response(response_data)
