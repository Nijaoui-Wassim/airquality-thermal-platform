# SmartEnv Air Quality & Thermal Platform

Live: [https://www.smartenv.ca/](https://www.smartenv.ca/)

---

## Overview

**SmartEnv** is an integrated IoT platform for real-time monitoring and visualization of indoor environmental quality, including particulate matter (PM), air quality metrics, and thermal imaging. The system is designed to connect multiple Raspberry Pi-based sensor devices to a centralized backend for data aggregation, storage, and analysis.

![Website Screenshot](https://github.com/Nijaoui-Wassim/airquality-thermal-platform/blob/main/sampleScreenshot.jpg?raw=true)


Key features include:

- **Real-time Data Ingestion:** Collects PM data, AQ data, images, and thermal images from distributed devices.
- **Room-Based Management:** Devices are grouped into logical “Rooms” for easy monitoring and filtering.
- **Modern Dashboard:** Clean, responsive dashboard for trends, charts, and raw data review.
- **Data Export:** Filter and export measurements by room, device, and date.
- **Device Management:** RESTful endpoints for secure device data uploads.
- **Admin Panel:** Full Django admin support for managing rooms, devices, and measurements.

---

## Technologies Used

- **Backend:** Django (Python), Gunicorn
- **Frontend:** Django templates (Bootstrap 5)
- **Database:** SQLite (default, easily replaceable with PostgreSQL or MySQL)
- **Deployment:** AWS EC2 (Amazon Linux), Nginx reverse proxy, Certbot/Let’s Encrypt for HTTPS
- **Domain:** [https://www.smartenv.ca/](https://www.smartenv.ca/)

![Website Screenshot](https://github.com/Nijaoui-Wassim/airquality-thermal-platform/blob/main/simplifiedArch.jpg?raw=true)

---

## Quick Start

1. Clone this repo:
   ```bash
   git clone https://github.com/Nijaoui-Wassim/airquality-thermal-platform.git
   ```
2. Set up your virtual environment and install requirements:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Apply migrations and create a superuser:
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
4. Collect static files:
   ```bash
   python manage.py collectstatic
   ```
5. Run the server:
   ```bash
   gunicorn --bind 127.0.0.1:8000 mybackend.wsgi:application
   ```

---

## Live Demo

The site is hosted at [https://www.smartenv.ca/](https://www.smartenv.ca/)

---

## License

This project is licensed under the MIT License.

---

## Author

Wassim Nijaoui\
Contact: [wassimnijaoui@gmail.com](mailto\:wassimnijaoui@gmail.com)

---

## Acknowledgements

- [Django Project](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Gunicorn](https://gunicorn.org/)
- [Nginx](https://nginx.org/)
- [Certbot](https://certbot.eff.org/)

