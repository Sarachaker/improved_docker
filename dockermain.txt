# Using Alpine for smaller image size
FROM python:3.9-alpine

# Install system dependencies
RUN apk add --no-cache build-base python3-dev libffi-dev openssl-dev

# Create and switch to app directory
WORKDIR /qr_app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY qr_generator.py .

# Set default environment variables
ENV QR_URL=https://github.com/Sarachaker
ENV QR_OUTPUT=/qr_app/output
ENV QR_FILENAME=my_qr.png
ENV QR_COLOR=navy
ENV QR_BG_COLOR=white
ENV QR_SIZE=10
ENV QR_BORDER=4

# Create volume mount point
VOLUME /qr_app/output

# Run the application
CMD ["python", "qr_generator.py"]
