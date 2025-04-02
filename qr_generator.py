import os
import sys
import qrcode
from datetime import datetime

class QRGenerator:
    def __init__(self):
        self.config = {
            'url': os.getenv('QR_URL', 'https://github.com/Sarachaker'),
            'output_path': os.getenv('QR_OUTPUT', 'output_qr'),
            'filename': os.getenv('QR_FILENAME', f'qr_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'),
            'color': os.getenv('QR_COLOR', 'darkblue'),
            'bg_color': os.getenv('QR_BG_COLOR', 'lightgray'),
            'size': int(os.getenv('QR_SIZE', '12')),
            'border': int(os.getenv('QR_BORDER', '2'))
        }

    def validate_url(self, url):
        return url.startswith(('http://', 'https://'))

    def generate(self):
        if not self.validate_url(self.config['url']):
            print("Error: Invalid URL format. Must start with http:// or https://")
            sys.exit(1)

        os.makedirs(self.config['output_path'], exist_ok=True)

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=self.config['size'],
            border=self.config['border'],
        )
        
        qr.add_data(self.config['url'])
        qr.make(fit=True)
        
        img = qr.make_image(
            fill_color=self.config['color'],
            back_color=self.config['bg_color']
        )
        
        full_path = os.path.join(self.config['output_path'], self.config['filename'])
        img.save(full_path)
        
        print(f"Success! QR code saved to: {full_path}")
        print(f"Config used: {self.config}")

if __name__ == "__main__":
    generator = QRGenerator()
    generator.generate()
