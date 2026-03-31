import qrcode
import io
import base64
from flask import Flask, render_template, request, jsonify
from urllib.parse import urlparse
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# Map of font names to Windows font filenames
FONTS = {
    "Arial": "arial.ttf",
    "Arial Bold": "arialbd.ttf",
    "Georgia": "georgia.ttf",
    "Georgia Bold": "georgiab.ttf",
    "Verdana": "verdana.ttf",
    "Verdana Bold": "verdanab.ttf",
    "Courier New": "cour.ttf",
    "Trebuchet MS": "trebuc.ttf",
    "Comic Sans": "comic.ttf",
    "Impact": "impact.ttf",
}

def is_valid_url(url):
    try:
        result = urlparse(url)
        return result.scheme in ("http", "https") and bool(result.netloc)
    except Exception:
        return False

def load_font(font_name, size):
    filename = FONTS.get(font_name, "arial.ttf")
    try:
        return ImageFont.truetype(filename, size)
    except:
        try:
            return ImageFont.truetype("arial.ttf", size)
        except:
            return ImageFont.load_default()

@app.route("/")
def index():
    font_names = list(FONTS.keys())
    return render_template("index.html", fonts=font_names)

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()

    url = data.get("url", "").strip()
    fg_color = data.get("fg_color", "#000000").strip() or "#000000"
    bg_color = data.get("bg_color", "#ffffff").strip() or "#ffffff"
    label = data.get("label", "").strip()
    font_name = data.get("font", "Arial")

    if not url:
        return jsonify({"error": "Please enter a URL."}), 400

    if not is_valid_url(url):
        return jsonify({"error": "Please enter a valid URL starting with http:// or https://"}), 400

    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=fg_color, back_color=bg_color).convert("RGB")

    # If label provided, add it below the QR code
    if label:
        qr_width, qr_height = qr_img.size
        padding = 20
        font_size = 48

        font = load_font(font_name, font_size)

        dummy = ImageDraw.Draw(Image.new("RGB", (1, 1)))
        bbox = dummy.textbbox((0, 0), label, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        label_area_height = text_height + padding * 2

        new_img = Image.new("RGB", (qr_width, qr_height + label_area_height), bg_color)
        new_img.paste(qr_img, (0, 0))

        draw = ImageDraw.Draw(new_img)
        text_x = (qr_width - text_width) // 2
        text_y = qr_height + padding
        draw.text((text_x, text_y), label, fill=fg_color, font=font)

        final_img = new_img
    else:
        final_img = qr_img

    buffer = io.BytesIO()
    final_img.save(buffer, format="PNG")
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    return jsonify({"image": img_base64, "url": url})

if __name__ == "__main__":
    app.run(debug=True)
