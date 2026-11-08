import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from urllib.parse import quote
import base64
import html
import mimetypes

# =====================================================
# MAMA-V-RAW FOOD COMPLEX
# PROFESSIONAL BUSINESS WEBSITE
# =====================================================

st.set_page_config(
    page_title="MAMA-V-RAW FOOD COMPLEX",
    page_icon="🌾",
    layout="wide"
)

# =====================================================
# BUSINESS SETTINGS
# =====================================================

BUSINESS_NAME = "MAMA-V-RAW FOOD COMPLEX"
TAGLINE = "Quality & Farm-Fresh Raw Foodstuffs"
CEO_NAME = "Adeyemi Mary Owoeye"

# Replace with actual WhatsApp number
WHATSAPP_NUMBER = "2348000000000"

# Change this password before publishing
ADMIN_PASSWORD = "ChangeMyAdminPassword"

BASE_DIR = Path(__file__).parent
ASSET_FOLDER = BASE_DIR / "assets"
ASSET_FOLDER.mkdir(exist_ok=True)


# =====================================================
# IMAGE FILENAMES
# =====================================================

IMAGES = {
    "Business Logo": "logo.jpg",
    "CEO Portrait": "ceo.jpg",
    "CEO Inspection": "ceo2.jpg",
    "CEO Customer Relations": "ceo3.jpg",
    "Beans": "bean.jpg",
    "Rice": "rice.jpg",
    "Semovita": "semovita.jpg",
    "Tin Tomatoes": "tomato.jpg"
}


# =====================================================
# PRODUCT DATABASE
# =====================================================

PRODUCTS = [
    {
        "name": "Honey/Oloyin Beans",
        "price": 45000,
        "unit": "Bag",
        "image": "bean.jpg"
    },

    {
        "name": "50kg Premium Rice",
        "price": 65000,
        "unit": "Bag",
        "image": "rice.jpg"
    },

    {
        "name": "Semovita (10kg)",
        "price": 12500,
        "unit": "Pack",
        "image": "semovita.jpg"
    },

    {
        "name": "Tin Tomatoes",
        "price": 18000,
        "unit": "Carton",
        "image": "tomato.jpg"
    }
]


# =====================================================
# SESSION MANAGEMENT
# =====================================================

if "cart" not in st.session_state:
    st.session_state.cart = {}

if "admin_login" not in st.session_state:
    st.session_state.admin_login = False


# =====================================================
# CUSTOM WEBSITE DESIGN
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: Poppins, sans-serif;
}

.stApp {
    background: #f4f7f3;
}

.block-container {
    max-width: 1250px;
    padding-top: 1rem;
}

.brand {
    background: white;
    padding: 25px;
    text-align: center;
    border-radius: 15px;
    border-top: 5px solid #2e7d32;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
}

.brand h1 {
    color: #1b5e20;
    font-size: 30px;
    font-weight: 800;
}

.section-title {
    text-align: center;
    color: #1b5e20;
    font-weight: 800;
    margin-top: 35px;
    margin-bottom: 25px;
}

.product-card {
    background: white;
    border-radius: 15px;
    padding: 12px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.07);
    margin-bottom: 20px;
}

.price {
    color: #2e7d32;
    font-size: 21px;
    font-weight: 800;
}

.order-box {
    background: white;
    padding: 22px;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
}

.footer {
    text-align: center;
    padding: 30px;
    color: #777;
}

div.stButton > button {
    background: #2e7d32;
    color: white;
    border-radius: 8px;
    font-weight: bold;
    width: 100%;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# IMAGE DISPLAY FUNCTION
# =====================================================

def image_path(filename):
    return ASSET_FOLDER / filename


def display_image(filename, height=200):

    path = image_path(filename)

    if path.is_file():

        st.image(
            str(path),
            use_container_width=True
        )

    else:

        st.markdown(f"""
        <div style="
            height:{height}px;
            background:#e8f5e9;
            border:1px dashed #2e7d32;
            border-radius:12px;
            display:flex;
            align-items:center;
            justify-content:center;
            text-align:center;
            color:#1b5e20;
        ">
            <div>
                <h2>🖼️</h2>
                <b>Image unavailable</b><br>
                {html.escape(filename)}
            </div>
        </div>
        """, unsafe_allow_html=True)


# =====================================================
# IMAGE CONVERSION FOR CEO SLIDESHOW
# =====================================================

def image_data(filename):

    path = image_path(filename)

    if not path.exists():
        return None

    mime = mimetypes.guess_type(path.name)[0] or "image/jpeg"

    encoded = base64.b64encode(
        path.read_bytes()
    ).decode()

    return f"data:{mime};base64,{encoded}"


# =====================================================
# CEO AUTOMATIC SLIDESHOW
# =====================================================

def ceo_slideshow():

    slide_details = [
        ("ceo.jpg", CEO_NAME, "CEO & Founder"),
        ("ceo2.jpg", "Quality Assurance", "Inspecting quality food products"),
        ("ceo3.jpg", "Customer Relations", "Serving customers with excellence")
    ]

    slides = []

    for filename, title, subtitle in slide_details:

        img = image_data(filename)

        if img:
            slides.append((img, title, subtitle))

    if not slides:

        st.info("Upload CEO pictures using the Admin Dashboard.")

        return

    slide_html = ""

    for i, (img, title, subtitle) in enumerate(slides):

        active = "active" if i == 0 else ""

        slide_html += f"""
        <div class="slide {active}">
            <img src="{img}">
            <div class="caption">
                <h3>{html.escape(title)}</h3>
                <p>{html.escape(subtitle)}</p>
            </div>
        </div>
        """

    page = f"""
    <html>
    <head>
    <style>

    body {{
        margin:0;
        font-family:Arial;
    }}

    .carousel {{
        position:relative;
        height:400px;
        overflow:hidden;
        border-radius:15px;
    }}

    .slide {{
        display:none;
        position:absolute;
        width:100%;
        height:100%;
    }}

    .slide.active {{
        display:block;
    }}

    .slide img {{
        width:100%;
        height:100%;
        object-fit:cover;
    }}

    .caption {{
        position:absolute;
        bottom:0;
        width:100%;
        background:linear-gradient(transparent,black);
        color:white;
        text-align:center;
        padding:30px 10px 15px;
    }}

    </style>
    </head>

    <body>

    <div class="carousel">
        {slide_html}
    </div>

    <script>

    let slides = document.querySelectorAll(".slide");

    let current = 0;

    function nextSlide() {{

        slides[current].classList.remove("active");

        current = (current + 1) % slides.length;

        slides[current].classList.add("active");

    }}

    if (slides.length > 1) {{
        setInterval(nextSlide, 20000);
    }}

    </script>

    </body>
    </html>
    """

    components.html(page, height=420)


# =====================================================
# WEBSITE HEADER
# =====================================================

st.markdown('<div class="brand">', unsafe_allow_html=True)

display_image("logo.jpg", 140)

st.markdown(f"""
<h1>{BUSINESS_NAME}</h1>

<p>{TAGLINE}</p>

<b>Welcome! Quality foodstuffs at affordable prices.</b>

</div>
""", unsafe_allow_html=True)


# =====================================================
# LEADERSHIP SECTION
# =====================================================

st.markdown(
    '<h2 class="section-title">LEADERSHIP & VISION</h2>',
    unsafe_allow_html=True
)

ceo_slideshow()


# =====================================================
# PRODUCT CATALOGUE
# =====================================================

st.markdown(
    '<h2 class="section-title">OUR PREMIUM PRODUCTS</h2>',
    unsafe_allow_html=True
)

columns = st.columns(4)

for index, product in enumerate(PRODUCTS):

    with columns[index]:

        st.markdown('<div class="product-card">', unsafe_allow_html=True)

        display_image(product["image"])

        st.subheader(product["name"])

        st.markdown(
            f'<div class="price">₦{product["price"]:,}</div>',
            unsafe_allow_html=True
        )

        st.caption(f'Price per {product["unit"]}')

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            max_value=100,
            value=1,
            key=f"quantity_{index}"
        )

        if st.button("ADD TO ORDER", key=f"add_{index}"):

            name = product["name"]

            if name in st.session_state.cart:

                st.session_state.cart[name]["quantity"] += quantity

            else:

                st.session_state.cart[name] = {
                    "price": product["price"],
                    "quantity": quantity
                }

            st.success("Product added to cart.")

            st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# SHOPPING CART
# =====================================================

st.markdown(
    '<h2 class="section-title">YOUR SHOPPING CART</h2>',
    unsafe_allow_html=True
)

st.markdown('<div class="order-box">', unsafe_allow_html=True)

total = 0

if st.session_state.cart:

    for name, item in list(st.session_state.cart.items()):

        amount = item["price"] * item["quantity"]

        total += amount

        col1, col2, col3 = st.columns([4, 2, 1])

        col1.write(name)

        col2.write(
            f'{item["quantity"]} unit(s) - ₦{amount:,}'
        )

        if col3.button("❌", key=f"remove_{name}"):

            del st.session_state.cart[name]

            st.rerun()

    st.divider()

    st.markdown(f"## TOTAL: :green[₦{total:,}]")

else:

    st.info("Your shopping cart is empty.")

if st.button("CLEAR SHOPPING CART"):

    st.session_state.cart = {}

    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# CUSTOMER ORDER FORM
# =====================================================

st.markdown(
    '<h2 class="section-title">CUSTOMER DELIVERY INFORMATION</h2>',
    unsafe_allow_html=True
)

st.markdown('<div class="order-box">', unsafe_allow_html=True)

with st.form("customer_form"):

    name = st.text_input("Full Name *")

    phone = st.text_input("Phone Number *")

    address = st.text_area("Delivery Address *")

    notes = st.text_area("Additional Instructions (Optional)")

    submit = st.form_submit_button(
        "PREPARE WHATSAPP ORDER"
    )


if submit:

    if not st.session_state.cart:

        st.error("Please add products to your cart.")

    elif not name.strip() or not phone.strip() or not address.strip():

        st.error("Please complete all required information.")

    elif WHATSAPP_NUMBER == "2348000000000":

        st.error("Please enter the actual business WhatsApp number in the code.")

    else:

        order_details = ""

        final_total = 0

        for product_name, item in st.session_state.cart.items():

            amount = item["price"] * item["quantity"]

            final_total += amount

            order_details += (
                f"\n{product_name}: {item['quantity']} unit(s)"
                f" - ₦{amount:,}"
            )

        message = f"""
NEW ORDER - {BUSINESS_NAME}

CUSTOMER DETAILS

Name: {name}

Phone: {phone}

Address: {address}

ORDER DETAILS

{order_details}

TOTAL AMOUNT: ₦{final_total:,}

Additional Instructions: {notes}

Please confirm availability and delivery arrangements.
"""

        whatsapp_url = (
            f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(message)}"
        )

        st.success("Your order is ready.")

        st.link_button(
            "🟢 OPEN WHATSAPP TO SEND ORDER",
            whatsapp_url,
            use_container_width=True
        )

st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# ADMINISTRATOR DASHBOARD
# UPLOAD OR CHANGE BUSINESS IMAGES
# =====================================================

st.markdown(
    '<h2 class="section-title">ADMINISTRATOR DASHBOARD</h2>',
    unsafe_allow_html=True
)

with st.expander("🔐 ADMIN LOGIN AND IMAGE MANAGEMENT"):

    if not st.session_state.admin_login:

        password = st.text_input(
            "Administrator Password",
            type="password"
        )

        if st.button("LOGIN AS ADMIN"):

            if password == ADMIN_PASSWORD:

                st.session_state.admin_login = True

                st.success("Administrator access granted.")

                st.rerun()

            else:

                st.error("Incorrect administrator password.")

    if st.session_state.admin_login:

        st.success("Welcome to the administrator dashboard.")

        st.subheader("Upload or Replace Business Images")

        selected = st.selectbox(
            "Select image category",
            list(IMAGES.keys())
        )

        filename = IMAGES[selected]

        uploaded = st.file_uploader(
            f"Upload {selected}",
            type=["jpg", "jpeg", "png", "webp"]
        )

        if uploaded:

            st.image(
                uploaded,
                caption="Image preview",
                use_container_width=True
            )

            if st.button("SAVE IMAGE"):

                destination = ASSET_FOLDER / filename

                destination.write_bytes(
                    uploaded.getvalue()
                )

                st.success(
                    f"Image successfully saved as {filename}"
                )

                st.rerun()

        st.divider()

        st.subheader("Image Upload Status")

        for label, filename in IMAGES.items():

            if (ASSET_FOLDER / filename).exists():

                st.success(f"{label}: {filename} - Uploaded")

            else:

                st.warning(f"{label}: {filename} - Missing")

        if st.button("LOGOUT ADMIN"):

            st.session_state.admin_login = False

            st.rerun()


# =====================================================
# FOOTER
# =====================================================

st.markdown(f"""
<div class="footer">

<h3>{BUSINESS_NAME}</h3>

<p>{TAGLINE}</p>

<p>© 2026 All Rights Reserved.</p>

</div>
""", unsafe_allow_html=True)
