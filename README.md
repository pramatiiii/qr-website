# 🔲 Custom QR Code Generator

A beautifully designed, modern web application that generates highly customizable QR codes. Built with a Python/Flask backend and a responsive, glassmorphism-styled frontend, this app allows users to create, customize, and download QR codes instantly.

## ✨ Features

* **Instant QR Generation:** Convert any valid HTTP/HTTPS URL into a scannable QR code.
* **Extensive Customization:**
    * Choose custom foreground and background colors using interactive color pickers or HEX codes.
    * Add custom text labels below the QR code.
    * Select from multiple font families for the text label.
* **Modern UI/UX:** Features a stunning "glassmorphism" interface with floating, animated gradient background orbs.
* **Session History:** Automatically saves your recently generated QR codes (up to 6) in the current browser session for quick reloading and comparison.
* **One-Click Download:** Download generated QR codes directly as high-quality PNG files.
* **Cloud-Ready:** Pre-configured for deployment on Render.

## 🛠️ Tech Stack

* **Backend:** Python 3, Flask
* **Image Processing:** `qrcode`, `Pillow` (PIL)
* **Frontend:** HTML5, CSS3 (DM Sans & Playfair Display fonts), Vanilla JavaScript
* **Server / Deployment:** Gunicorn, Render

## 📁 Project Structure

```text
├── app.py                 # Main Flask application and image processing logic
├── render.yaml            # Render deployment configuration
├── requirements.txt       # Python dependencies
├── static/
│   └── style.css          # UI styling, animations, and glassmorphism effects
└── templates/
    └── index.html         # Frontend HTML structure and client-side JavaScript
