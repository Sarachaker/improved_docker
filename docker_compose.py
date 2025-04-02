version: '3.8'

services:
  qr-service:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - QR_URL=https://github.com/your-new-profile
      - QR_FILENAME=custom_qr.png
      - QR_COLOR=darkgreen
      - QR_BG_COLOR=white
    volumes:
      - qr-storage:/qr_app/output
    restart: on-failure

volumes:
  qr-storage:
