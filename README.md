# 🔳 Custom QR Code Generator

A modern, visually refined web application for generating highly customizable QR codes in real time. This project combines a lightweight Python/Flask backend with a polished, glassmorphism-inspired frontend to deliver both functionality and aesthetic appeal.

It is designed not just as a utility tool, but as a clean example of full-stack development, integrating image processing, UI design, and deployable infrastructure into a cohesive system.

---

## 🚀 Overview

The **Custom QR Code Generator** enables users to transform any valid URL into a fully customizable QR code with control over styling, labeling, and output format.

Unlike basic QR generators, this application focuses on:

* **Design flexibility**
* **User experience**
* **Session-based usability**
* **Deployment readiness**

---

## ✨ Key Features

### ⚡ Instant QR Code Generation

* Converts any valid `http` or `https` URL into a scannable QR code
* Real-time generation with minimal latency
* Error handling for invalid or malformed inputs

---

### 🎨 Advanced Customization

#### 🎯 Color Control

* Custom foreground and background colors
* Interactive color picker + HEX input support
* Ensures contrast for scannability (important practical constraint)

#### 🏷️ Text Labeling

* Add optional text below the QR code
* Useful for branding, instructions, or identification

#### 🔤 Typography Options

* Multiple font families supported
* Clean integration with modern web fonts (DM Sans, Playfair Display)

---

### 🧊 Modern UI (Glassmorphism Design)

* Frosted glass effect interface
* Smooth gradients and animated floating orbs
* Responsive layout for different screen sizes
* Focus on clarity + visual hierarchy

---

### 🕘 Session History

* Stores up to **6 recently generated QR codes**
* Enables quick comparison and reuse
* Implemented using browser session storage (not server-side persistence)

---

### ⬇️ One-Click Download

* Export QR codes as high-quality PNG files
* Maintains visual fidelity and resolution
* No additional processing required

---

### ☁️ Cloud Deployment Ready

* Configured for deployment on **Render**
* Uses **Gunicorn** as the production WSGI server
* Includes deployment configuration (`render.yaml`)

---

## 🛠️ Tech Stack

### Backend

* **Python 3**
* **Flask**

  * Handles routing, request processing, and response delivery

### Image Processing

* **qrcode**

  * Generates QR matrix data
* **Pillow (PIL)**

  * Handles image customization (colors, text rendering)

### Frontend

* **HTML5**
* **CSS3**

  * Glassmorphism effects
  * Animations and gradients
* **Vanilla JavaScript**

  * Handles interactivity and session storage

### Deployment

* **Gunicorn** (WSGI server)
* **Render** (cloud hosting platform)

---

## 📁 Project Structure

```
├── app.py                 # Core Flask app and QR generation logic
├── render.yaml            # Deployment configuration for Render
├── requirements.txt       # Python dependencies
├── static/
│   └── style.css          # Styling, animations, UI effects
└── templates/
    └── index.html         # Frontend layout + client-side JS
```

---

## ⚙️ How It Works (Conceptual Flow)

1. User inputs a URL and customization options
2. Frontend sends data to Flask backend
3. Backend:

   * Generates QR matrix using `qrcode`
   * Applies styling using `Pillow`
   * Adds optional text label
4. Image is returned to frontend
5. Frontend:

   * Displays QR code
   * Stores it in session history
   * Allows download

---

## 🧪 Local Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd custom-qr-generator
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
python app.py
```

### 5. Open in Browser

```
http://127.0.0.1:5000/
```

---

## 🌍 Deployment (Render)

1. Push project to GitHub
2. Connect repository to Render
3. Ensure:

   * `render.yaml` is configured
   * Start command uses Gunicorn
4. Deploy

---

## ⚠️ Design Considerations & Limitations

* **Contrast matters:** Low contrast color combinations may produce unreadable QR codes
* **Text overlay positioning:** Large labels may affect scan reliability if not spaced properly
* **Session storage limitation:** History is not persistent across devices or browser restarts
* **URL validation:** Only basic validation is implemented (can be extended)

---

## 🔮 Possible Improvements

* QR code logo embedding (center image)
* SVG download support (vector format)
* Dark mode toggle
* User accounts + cloud history
* Analytics (scan tracking)
* API endpoint for programmatic use

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👩‍💻 Author

**Pramati Gupta**
B.Tech CSE Student
Focused on building clean, functional, and visually engaging web applications.

---

## 💡 Final Note

This project is a strong example of combining:

* Backend logic
* Image processing
* UI/UX design
* Deployment practices

If extended thoughtfully, it can evolve from a simple utility into a production-grade tool.

---
