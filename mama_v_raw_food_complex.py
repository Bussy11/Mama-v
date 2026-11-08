import streamlit as st
import streamlit.components.v1 as components
from urllib.parse import quote
from pathlib import Path
import base64
import mimetypes
import html

# ============================================================
# MAMA-V-RAW FOOD COMPLEX
# Streamlit conversion of the supplied HTML/CSS/JavaScript site
# ============================================================

st.set_page_config(
    page_title="MAMA-V-RAW FOOD COMPLEX",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- BUSINESS SETTINGS: EDIT THESE VALUES ----------
BUSINESS_NAME = "MAMA-V-RAW FOOD COMPLEX"
TAGLINE = "Quality & Farm-Fresh Raw Foodstuffs"
CEO_NAME = "Adeyemi Mary Owoeye"

# IMPORTANT: Replace this with the business WhatsApp number.
# Use country code, without +, spaces, or leading zero.
# Example for a Nigerian number: 2348012345678
VENDOR_WHATSAPP = "2348000000000"

ASSET_DIR = Path(__file__).parent / "assets"

# ---------- PRODUCTS ----------
PRODUCTS = [
    {
        "name": "Stacked Bags of Beans (Honey/Oloyin)",
        "price": 45000,
        "unit": "Bag",
        "image": "beans-stack.jpg",
        "description": "Quality honey beans for homes, retailers and bulk buyers.",
    },
    {
        "name": "50kg Premium Rice Bag",
        "price": 65000,
        "unit": "Bag",
        "image": "rice-bags.jpg",
        "description": "Premium rice for everyday family and business needs.",
    },
    {
        "name": "Semovita (10kg Pack)",
        "price": 12500,
        "unit": "Pack",
        "image": "semovita.jpg",
        "description": "A convenient 10kg pack for your kitchen.",
    },
    {
        "name": "Tin Tomatoes (Carton)",
        "price": 18000,
        "unit": "Carton",
        "image": "tin-tomatoes.jpg",
        "description": "Tomato cartons for household and commercial cooking.",
    },
]

# ---------- STYLING ----------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    .stApp { background: #f4f6f8; color: #2c3e50; }
    [data-testid="stHeader"] { background: rgba(244,246,248,0.95); }
    .block-container { max-width: 1200px; padding-top: 1.4rem; padding-bottom: 3rem; }
    .brand-card {
        background: #fff; border-radius: 18px; padding: 22px 15px;
        text-align: center; box-shadow: 0 8px 24px rgba(0,0,0,.07);
        border-top: 5px solid #2e7d32; margin-bottom: 25px;
    }
    .brand-title { color: #1b5e20; font-size: clamp(1.35rem, 4vw, 2rem);
        font-weight: 800; letter-spacing: 1px; margin: 8px 0 2px; }
    .brand-subtitle { color: #666; font-size: .95rem; }
    .section-heading {
        color: #1b5e20; text-align: center; font-size: 1.55rem;
        font-weight: 700; letter-spacing: .7px; margin: 28px 0 18px;
    }
    .section-heading:after {
        content: ''; display: block; width: 62px; height: 4px;
        background: #fbc02d; margin: 8px auto 0; border-radius: 5px;
    }
    .product-card {
        background: white; padding: 13px; border-radius: 14px;
        box-shadow: 0 8px 24px rgba(0,0,0,.07); height: 100%;
        border: 1px solid #edf0ed;
    }
    .product-card h3 { color: #263238; font-size: 1rem; min-height: 48px; }
    .product-price { color: #2e7d32; font-size: 1.15rem; font-weight: 800; }
    .product-description { color: #6b7280; font-size: .83rem; min-height: 42px; }
    .order-panel {
        background: #fff; padding: 22px; border-radius: 16px;
        box-shadow: 0 8px 24px rgba(0,0,0,.07);
    }
    .small-note { color: #777; font-size: .82rem; }
    div.stButton > button {
        border-radius: 8px; font-weight: 600; min-height: 42px;
    }
    .whatsapp-link {
        display: block; text-align: center; background: #25d366; color: white !important;
        padding: 14px 16px; border-radius: 9px; text-decoration: none !important;
        font-weight: 700; margin-top: 12px;
    }
    .footer {
        text-align: center; color: #777; font-size: .82rem;
        padding: 28px 5px 8px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


def asset_path(filename: str) -> Path:
    """Return the expected path for an image stored in the assets folder."""
    return ASSET_DIR / filename


def show_image(filename: str, caption: str = "", width=None):
    """Display an image, or a helpful placeholder if it has not been uploaded."""
    path = asset_path(filename)
    if path.exists():
        st.image(str(path), caption=caption, use_container_width=(width is None))
    else:
        st.markdown(
            f"""
            <div style="height:180px;display:flex;align-items:center;justify-content:center;
                        background:#eef3ee;border:1px dashed #9bb59d;border-radius:12px;
                        color:#55715a;text-align:center;padding:12px;">
                <div><div style="font-size:2rem;">🖼️</div>
                <b>Image not uploaded</b><br><small>{html.escape(filename)}</small></div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def image_as_data_uri(path: Path):
    """Convert a local image to a data URI for the browser-based carousel."""
    if not path.exists():
        return None
    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"
    encoded = base64.b64encode(path.read_bytes()).decode("utf-8")
    return f"data:{mime};base64,{encoded}"


def show_ceo_carousel():
    slides = [
        ("ceo-photo-1.jpg", CEO_NAME, "CEO & Founder - Mama-V-Raw Food Complex"),
        ("ceo-photo-2.jpg", "Quality Assured", "Inspecting premium raw foodstuffs from trusted farm sources."),
        ("ceo-photo-3.jpg", "Customer First Services", "Bulk and retail food supply with customer-focused service."),
    ]
    available = []
    for filename, title, subtitle in slides:
        data_uri = image_as_data_uri(asset_path(filename))
        if data_uri:
            available.append((data_uri, title, subtitle))

    if not available:
        st.info(
            "CEO showcase photos have not been uploaded yet. Add ceo-photo-1.jpg, "
            "ceo-photo-2.jpg and ceo-photo-3.jpg to the assets folder."
        )
        return

    slide_html = ""
    for index, (src, title, subtitle) in enumerate(available):
        active = "active" if index == 0 else ""
        slide_html += f"""
        <div class="slide {active}">
          <img src="{src}" alt="{html.escape(title)}">
          <div class="caption">
            <h3>{html.escape(title)}</h3>
            <p>{html.escape(subtitle)}</p>
          </div>
        </div>
        """

    carousel_html = f"""
    <!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
      * {{ box-sizing:border-box; }}
      body {{ margin:0; font-family:Arial,sans-serif; }}
      .carousel {{ position:relative; width:100%; height:clamp(240px, 48vw, 420px);
        overflow:hidden; border-radius:14px; background:#e9eee9; }}
      .slide {{ display:none; position:absolute; inset:0; opacity:0; transition:opacity 1s ease; }}
      .slide.active {{ display:block; opacity:1; }}
      .slide img {{ width:100%; height:100%; object-fit:cover; object-position:center; }}
      .caption {{ position:absolute; left:0; right:0; bottom:0; padding:35px 15px 17px;
        color:white; text-align:center; background:linear-gradient(transparent,rgba(0,0,0,.82)); }}
      .caption h3 {{ margin:0 0 4px; font-size:clamp(16px,3vw,21px); }}
      .caption p {{ margin:0; font-size:clamp(11px,2vw,14px); color:#eee; }}
      .progress {{ height:4px; background:#e0e0e0; border-radius:5px; overflow:hidden; margin-top:10px; }}
      .bar {{ height:100%; width:0; background:#2e7d32; animation:load 20s linear forwards; }}
      @keyframes load {{ to {{ width:100%; }} }}
    </style></head><body>
      <div class="carousel">{slide_html}</div>
      <div class="progress"><div class="bar" id="bar"></div></div>
      <script>
        const slides = document.querySelectorAll('.slide');
        let current = 0;
        function nextSlide() {{
          slides[current].classList.remove('active');
          current = (current + 1) % slides.length;
          slides[current].classList.add('active');
          const oldBar = document.getElementById('bar');
          const newBar = oldBar.cloneNode(false);
          oldBar.parentNode.replaceChild(newBar, oldBar);
        }}
        if (slides.length > 1) setInterval(nextSlide, 20000);
      </script>
    </body></html>
    """
    components.html(carousel_html, height=460, scrolling=False)


# ---------- SESSION CART ----------
if "cart" not in st.session_state:
    st.session_state.cart = []


# ---------- HEADER / BRANDING ----------
logo_file = asset_path("watermarked_img_778831935902119491.jpg")
st.markdown('<div class="brand-card">', unsafe_allow_html=True)
if logo_file.exists():
    st.image(str(logo_file), width=145)
else:
    st.markdown("## 🌾")
st.markdown(
    f'<div class="brand-title">{BUSINESS_NAME}</div>'
    f'<div class="brand-subtitle">{TAGLINE}</div></div>',
    unsafe_allow_html=True,
)

# ---------- CEO SHOWCASE ----------
st.markdown('<div class="section-heading">LEADERSHIP &amp; VISION</div>', unsafe_allow_html=True)
show_ceo_carousel()

# ---------- PRODUCT CATALOG ----------
st.markdown('<div class="section-heading">OUR PREMIUM PRODUCTS</div>', unsafe_allow_html=True)
columns = st.columns(4, gap="medium")
for index, product in enumerate(PRODUCTS):
    with columns[index]:
        st.markdown('<div class="product-card">', unsafe_allow_html=True)
        show_image(product["image"])
        st.markdown(f'<h3>{html.escape(product["name"])}</h3>', unsafe_allow_html=True)
        st.markdown(
            f'<div class="product-price">₦{product["price"]:,} / {product["unit"]}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div class="product-description">{html.escape(product["description"])}</div>',
            unsafe_allow_html=True,
        )
        if st.button("➕ Add to Order", key=f"add_{index}", use_container_width=True):
            st.session_state.cart.append(
                {"name": product["name"], "price": product["price"]}
            )
            st.toast(f'{product["name"]} added to your order.')
        st.markdown("</div>", unsafe_allow_html=True)

# ---------- ORDER SUMMARY ----------
st.markdown('<div class="section-heading">COMPLETE YOUR ORDER</div>', unsafe_allow_html=True)
left, right = st.columns([1.05, 1], gap="large")

with left:
    st.markdown('<div class="order-panel">', unsafe_allow_html=True)
    st.subheader("🛒 Selected Items")
    if not st.session_state.cart:
        st.caption('No items added yet. Select "Add to Order" above.')
        total = 0
    else:
        total = 0
        for i, item in enumerate(st.session_state.cart):
            row1, row2 = st.columns([5, 1])
            row1.write(f'{item["name"]} — ₦{item["price"]:,}')
            if row2.button("✕", key=f"remove_{i}", help="Remove this item"):
                st.session_state.cart.pop(i)
                st.rerun()
            total += item["price"]
    st.divider()
    st.markdown(f"### Total estimate: :green[₦{total:,}]")
    if st.button("🗑️ Clear Order", disabled=not st.session_state.cart):
        st.session_state.cart = []
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown('<div class="order-panel">', unsafe_allow_html=True)
    st.subheader("📦 Customer Details")
    with st.form("customer_order_form"):
        customer_name = st.text_input("Full Name *", placeholder="Enter your full name")
        customer_phone = st.text_input("Phone Number *", placeholder="e.g. 08012345678")
        customer_address = st.text_area(
            "Delivery Address *",
            placeholder="Enter full delivery address, area and nearest landmark",
            height=105,
        )
        submitted = st.form_submit_button(
            "Send Order via WhatsApp", type="primary", use_container_width=True
        )

    if submitted:
        if not st.session_state.cart:
            st.error("Please add at least one product to your order.")
        elif not customer_name.strip() or not customer_phone.strip() or not customer_address.strip():
            st.error("Please complete all customer details marked with *.")
        elif not VENDOR_WHATSAPP.isdigit() or len(VENDOR_WHATSAPP) < 10 or VENDOR_WHATSAPP == "2348000000000":
            st.error(
                "The business WhatsApp number has not been configured. "
                "Edit VENDOR_WHATSAPP near the top of the Python file."
            )
        else:
            item_lines = "\n".join(
                f'- {item["name"]}: ₦{item["price"]:,}'
                for item in st.session_state.cart
            )
            order_total = sum(item["price"] for item in st.session_state.cart)
            message = (
                f"*NEW ORDER - {BUSINESS_NAME}*\n\n"
                f"*Customer Details:*\n"
                f"Name: {customer_name.strip()}\n"
                f"Phone: {customer_phone.strip()}\n"
                f"Address: {customer_address.strip()}\n\n"
                f"*Items Ordered:*\n{item_lines}\n\n"
                f"*Total Estimate: ₦{order_total:,}*\n\n"
                "Please confirm product availability and delivery arrangements."
            )
            whatsapp_url = (
                f"https://wa.me/{VENDOR_WHATSAPP}?text={quote(message)}"
            )
            st.success("Your order message is ready. Tap the button below to send it.")
            st.markdown(
                f'<a class="whatsapp-link" href="{whatsapp_url}" target="_blank">'
                '🟢 Open WhatsApp and Send Order</a>',
                unsafe_allow_html=True,
            )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------- FOOTER ----------
st.markdown(
    f'<div class="footer">© 2026 {BUSINESS_NAME}. All Rights Reserved.</div>',
    unsafe_allow_html=True,
)

with st.expander("📁 Required image files and upload names"):
    st.write("Create a folder named **assets** in the same location as this Python file.")
    st.write("Save your images in that folder using these exact filenames:")
    st.code(
        "assets/\n"
        "├── watermarked_img_778831935902119491.jpg  # Business logo\n"
        "├── ceo-photo-1.jpg                         # CEO portrait\n"
        "├── ceo-photo-2.jpg                         # CEO at inspection / farm visit\n"
        "├── ceo-photo-3.jpg                         # CEO with customers / at work\n"
        "├── beans-stack.jpg                         # Beans product photo\n"
        "├── rice-bags.jpg                            # Rice product photo\n"
        "├── semovita.jpg                             # Semovita product photo\n"
        "└── tin-tomatoes.jpg                         # Tin tomatoes product photo"
    )
    st.caption(
        "JPG, JPEG or PNG images are suitable. If you use PNG or a different extension, "
        "update the matching filename in the code. Product prices can be edited in PRODUCTS."
    )
