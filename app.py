import qrcode
import os
from PIL import Image
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("qr_generation.log"),  # Save logs to file
        logging.StreamHandler()  # Also print to console
    ]
)
logger = logging.getLogger(__name__)

# Environment variables with defaults
QR_DATA_URL = os.getenv("QR_DATA_URL", "https://github.com/sarachaker")
QR_CODE_DIR = os.getenv("QR_CODE_DIR", "qr_codes")
QR_CODE_FILENAME = os.getenv("QR_CODE_FILENAME", "github_qr.png")
FILL_COLOR = os.getenv("FILL_COLOR", "blue")
BACK_COLOR = os.getenv("BACK_COLOR", "yellow")

def generate_qr_code():
    try:
        # Ensure output directory exists
        os.makedirs(QR_CODE_DIR, exist_ok=True)
        logger.info(f"Output directory ensured: {QR_CODE_DIR}")

        # Configure QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(QR_DATA_URL)
        qr.make(fit=True)

        # Generate QR code image
        img = qr.make_image(fill_color=FILL_COLOR, back_color=BACK_COLOR)

        # Save QR code
        output_path = os.path.join(QR_CODE_DIR, QR_CODE_FILENAME)
        img.save(output_path)
        logger.info(f"QR code generated successfully at {output_path}")

        # Display QR code (for online compilers like Colab/Replit)
        try:
            img.show()  # May not work in all online environments
        except Exception as e:
            logger.warning(f"Could not display QR code: {e}. File saved at {output_path}")

    except Exception as e:
        logger.error(f"Error generating QR code: {e}")
        raise

if __name__ == "__main__":
    logger.info("Starting QR code generation")
    generate_qr_code()
    logger.info("QR code generation completed")
