import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from urllib.parse import quote
import base64

# =====================================================
# MAMA-V-RAW FOOD COMPLEX
# PROFESSIONAL FOOD BUSINESS WEBSITE
# =====================================================

st.set_page_config(
    page_title="MAMA-V-RAW FOOD COMPLEX",
    page_icon="🌾",
    layout="wide"
)

# =====================================================
# BUSINESS INFORMATION
# =====================================================

BUSINESS_NAME = "MAMA-V-RAW FOOD COMPLEX"

TAGLINE = "Quality & Farm-Fresh Raw Foodstuffs"

CEO_NAME = "Adeyemi Mary Owoeye"

WHATSAPP_NUMBER = "2348000000000"

BUSINESS_ADDRESS = "Nigeria"

ASSET_FOLDER = Path(__file__).parent / "assets"


# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp {
    background-color: #f4f7f3;
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
    border-bottom: 5px solid #2e7d32;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
}

.brand h1 {
    color: #1b5e20;
    font-size: 30px;
    font-weight: 800;
}

.brand p {
    color: #666;
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
    font-size: 22px;
    font-weight: 800;
}

.order-box {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 5px 20px rgba(0,0,0,0.08);
}

.footer {
    text-align: center;
    padding: 30px;
    color: #777;
}

div.stButton > button {
    background-color: #2e7d32;
    color: white;
    border-radius: 8px;
    font-weight: bold;
    border: none;
    width: 100%;
}

div.stButton > button:hover {
    background-color: #1b5e20;
    color: white;
}

</style>
""", unsafe_allow_html=True)


# =====================================================
# IMAGE FUNCTION
# =====================================================

def display_image(filename, height=200):

    image_path = ASSET_FOLDER / filename

    if image_path.exists():

        st.image(
            str(image_path),
            use_container_width=True
        )

    else:

        st.markdown(
            f"""
            <div style="
                height:{height}px;
                background:#e8f5e9;
                border:1px dashed #2e7d32;
                border-radius:12px;
                display:flex;
                align-items:center;
                justify-content:center;
                color:#1b5e20;
                text-align:center;
                ">
                <div>
                    <h2>🖼️</h2>
                    <b>Image unavailable</b><br>
                    {filename}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# =====================================================
# PRODUCT DATABASE
# =====================================================

PRODUCTS = {

    "Beans (Honey/Oloyin)": {
        "price": 45000,
        "image": "bean.jpg",
        "unit": "Bag"
    },

    "50kg Premium Rice": {
        "price": 65000,
        "image": "rice.jpg",
        "unit": "Bag"
    },

    "Semovita (10kg)": {
        "price": 12500,
        "image": "semovita.jpg",
        "unit": "Pack"
    },

    "Tin Tomatoes": {
        "price": 18000,
        "image": "tomato.jpg",
        "unit": "Carton"
    }

}


# =====================================================
# SHOPPING CART
# =====================================================

if "cart" not in st.session_state:

    st.session_state.cart = {}


# =====================================================
# HEADER
# =====================================================

st.markdown('<div class="brand">', unsafe_allow_html=True)

display_image("logo.jpg", 150)

st.markdown(
    f"""
    <h1>{BUSINESS_NAME}</h1>
    <p>{TAGLINE}</p>
    <b>Welcome! Quality foodstuffs at affordable prices.</b>
    """,
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# CEO SHOWCASE
# =====================================================

st.markdown(
    '<h2 class="section-title">LEADERSHIP & VISION</h2>',
    unsafe_allow_html=True
)

def get_image_data(filename):

    path = ASSET_FOLDER / filename

    if not path.exists():
        return None

    encoded = base64.b64encode(path.read_bytes()).decode()

    return f"data:image/jpeg;base64,{encoded}"


ceo_slides = [
    ("ceo.jpg", CEO_NAME, "CEO & Founder"),
    ("ceo2.jpg", "Quality Assurance", "Inspecting quality food products"),
    ("ceo3.jpg", "Customer Relations", "Serving customers with excellence")
]

slides = []

for filename, title, subtitle in ceo_slides:

    image_data = get_image_data(filename)

    if image_data:

        slides.append(
            (image_data, title, subtitle)
        )


if slides:

    slide_html = ""

    for index, (image, title, subtitle) in enumerate(slides):

        active = "active" if index == 0 else ""

        slide_html += f"""
        <div class="slide {active}">
            <img src="{image}">
            <div class="caption">
                <h3>{title}</h3>
                <p>{subtitle}</p>
            </div>
        </div>
        """

    carousel = f"""
    <html>
    <head>
    <style>

    * {{ box-sizing:border-box; }}

    body {{
        margin:0;
        font-family:Arial;
    }}

    .carousel {{
        position:relative;
        height:400px;
        overflow:hidden;
        border-radius:15px;
        background:#eee;
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

    components.html(
        carousel,
        height=420
    )

else:

    st.info("Upload CEO pictures into the assets folder to display the slideshow.")


# =====================================================
# PRODUCT DISPLAY
# =====================================================

st.markdown(
    '<h2 class="section-title">OUR PREMIUM PRODUCTS</h2>',
    unsafe_allow_html=True
)

columns = st.columns(4)

for index, (name, details) in enumerate(PRODUCTS.items()):

    with columns[index]:

        st.markdown('<div class="product-card">', unsafe_allow_html=True)

        display_image(details["image"])

        st.subheader(name)

        st.markdown(
            f'<div class="price">₦{details["price"]:,}</div>',
            unsafe_allow_html=True
        )

        st.caption(f'Price per {details["unit"]}')

        quantity = st.number_input(
            "Quantity",
            min_value=1,
            max_value=100,
            value=1,
            key=f"quantity_{index}"
        )

        if st.button(
            "ADD TO ORDER",
            key=f"add_{index}"
        ):

            if name in st.session_state.cart:

                st.session_state.cart[name]["quantity"] += quantity

            else:

                st.session_state.cart[name] = {
                    "price": details["price"],
                    "quantity": quantity
                }

            st.success(f"{name} added to cart.")

        st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# ORDER SUMMARY
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
            f'₦{amount:,} ({item["quantity"]} unit(s))'
        )

        if col3.button("❌", key=f"remove_{name}"):

            del st.session_state.cart[name]

            st.rerun()

    st.divider()

    st.markdown(
        f"## TOTAL: :green[₦{total:,}]"
    )

else:

    st.info("Your shopping cart is empty.")


if st.button("CLEAR SHOPPING CART"):

    st.session_state.cart = {}

    st.rerun()

st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# CUSTOMER INFORMATION
# =====================================================

st.markdown(
    '<h2 class="section-title">CUSTOMER DELIVERY INFORMATION</h2>',
    unsafe_allow_html=True
)

st.markdown('<div class="order-box">', unsafe_allow_html=True)

with st.form("customer_form"):

    customer_name = st.text_input(
        "Full Name *"
    )

    customer_phone = st.text_input(
        "Phone Number *"
    )

    customer_address = st.text_area(
        "Delivery Address *"
    )

    submit = st.form_submit_button(
        "SEND ORDER THROUGH WHATSAPP"
    )


if submit:

    if not st.session_state.cart:

        st.error("Please add products to your cart.")

    elif not customer_name or not customer_phone or not customer_address:

        st.error("Please complete all customer information.")

    elif WHATSAPP_NUMBER == "2348000000000":

        st.error("Please configure the business WhatsApp number in the code.")

    else:

        order_details = ""

        for name, item in st.session_state.cart.items():

            amount = item["price"] * item["quantity"]

            order_details += (
                f"\n{name} - {item['quantity']} unit(s) "
                f"- ₦{amount:,}"
            )

        message = f"""
NEW ORDER - {BUSINESS_NAME}

CUSTOMER DETAILS

Name: {customer_name}

Phone: {customer_phone}

Address: {customer_address}

ORDER DETAILS

{order_details}

TOTAL AMOUNT: ₦{total:,}

Please confirm product availability and delivery.
"""

        whatsapp_url = (
            f"https://wa.me/{WHATSAPP_NUMBER}"
            f"?text={quote(message)}"
        )

        st.success("Your order is ready.")

        st.link_button(
            "🟢 OPEN WHATSAPP TO SEND ORDER",
            whatsapp_url,
            use_container_width=True
        )

st.markdown('</div>', unsafe_allow_html=True)


# =====================================================
# FOOTER
# =====================================================

st.markdown(
    f"""
    <div class="footer">

    <h3>{BUSINESS_NAME}</h3>

    Quality & Farm-Fresh Raw Foodstuffs

    <p>© 2026 All Rights Reserved.</p>

    </div>
    """,
    unsafe_allow_html=True
)
