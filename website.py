import streamlit as st
from PIL import Image
import base64

# Set page configuration
st.set_page_config(page_title="Shri Ram Ji Computerised Tounch", layout="wide")

# Function to load images and convert them to base64
def load_image(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

# Load images
logo_img = load_image("Screenshot_2024-08-21-22-12-35-282_com.whatsapp.w4b.jpg")
cert_img = load_image("SHRI_RAM_JI_COMPUTERISED_TOUNCH 9_1.jpg")
pic_img = load_image("1724258365130.jpg")

# Apply CSS styling for a professional look

st.markdown(f"""
    <style>
    body {{
        background-image: url(data:image/jpeg;base64,{logo_img});
        background-repeat: no-repeat;
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        margin: 0;
        padding: 0;
        font-family: Arial, sans-serif;
    }}
    .container {{
        display: flex;
        flex-wrap: wrap;
        margin: 20px;
    }}
    .main-content {{
        flex: 1;
        margin-left: 20px;
        padding: 20px;
        min-width: 300px;
        max-width: 70%;
        box-sizing: border-box;
    }}
    .reviews {{
        flex-basis: 25%;
        background-color: #ffffff;
        border-left: 2px solid #ddd;
        max-height: 100vh;
        overflow-y: scroll;
        padding: 10px;
        box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
        margin-top: 20px;
        box-sizing: border-box;
    }}
    .reviews::-webkit-scrollbar {{
        width: 12px;
    }}
    .reviews::-webkit-scrollbar-thumb {{
        background-color: #888;
        border-radius: 6px;
    }}
    .reviews::-webkit-scrollbar-thumb:hover {{
        background-color: #555;
    }}
    .footer {{
        background-color: #333;
        color: #ffffff;
        padding: 10px;
        text-align: center;
        width: 100%;
        box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
    }}
    .footer .button {{
        color: #ffffff;
        background-color: #007bff;
        border: none;
        padding: 10px 20px;
        margin: 5px;
        text-decoration: none;
        border-radius: 4px;
    }}
    .footer .button:hover {{
        background-color: #0056b3;
    }}
    .logo {{
        text-align: center;
        margin-bottom: 20px;
    }}
    .logo img {{
        max-width: 200px;
        height: auto;
    }}
    .certificate {{
        text-align: center;
        margin-top: 20px;
        margin-bottom: 20px;
    }}
    .certificate img {{
        max-width: 100%;
        height: auto;
    }}
    .pictures {{
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        justify-content: center;
    }}
    .pictures img {{
        max-width: 300px;
        height: auto;
    }}
    /* Mobile-specific styles */
    @media only screen and (max-width: 768px) {{
        .container {{
            flex-direction: column;
            padding: 10px;
        }}
        .main-content {{
            margin-left: 0;
            padding: 10px;
            max-width: 100%;
        }}
        .reviews {{
            flex-basis: 100%;
            max-height: none;
            margin-top: 20px;
            padding: 10px;
            width: 100%;
        }}
    }}
    </style>
""", unsafe_allow_html=True)


# Main content
st.markdown(f"""
    <div class="container">
        <div class="main-content">
            <div class="logo">
                <img src="data:image/jpeg;base64,{logo_img}" alt="Logo">
            </div>
            <h1>Shri Ram Ji Computerised Tounch [SILVER TESTING]</h1>
            <h2>Overview</h2>
            <p>At Shri Ram Ji Computerised Tounch, we specialize in testing the purity of silver ornaments with an accuracy of 99.75%. Our process begins with melting the object and meticulously testing it, ensuring the highest level of precision. With years of experience under our belts, our skilled workers, alongside the owner who personally oversees the testing, guarantee reliable results.

We are proud to serve some of the most renowned silver jewelers and retailers across India, who trust us for our fast service and competitive rates. To ensure the utmost accuracy, we recheck each test three additional times, making us one of the best silver testing providers in the region.

Certified by BQM, our data is widely accepted by retailers, giving you peace of mind. We also offer the convenience of accepting courier services, making our top-notch testing services accessible to clients nationwide.</p>
            <div class="certificate">
                <img src="data:image/jpeg;base64,{cert_img}" alt="Certificate">
            </div>
            <div class="pictures">
                <img src="data:image/jpeg;base64,{pic_img}" alt="Picture">
            </div>
        </div>
        <div class="reviews">
            <h2>Reviews</h2>
            <strong>sapan kumar:</strong> this provides best services and shop owner is so good because his behaviour is very good.<br><br>
            <strong>Faizan Saifi:</strong> Best service available in this shop. In market shop owner behaviour is so good.<br><br>
            <strong>Pankaj Barakoti:</strong> The owner is very kind and cooperative. I am a regular customer at this shop. Accuracy is maintained.<br><br>
            <strong>Dr. Shabeena Bano:</strong> This Shop Selling The Best. And They Are Very Honest And Trusted In UP.☺️<br><br>
            <strong>Priyanshu Yadav:</strong> More accurate and precise workmanship. One of the best in the market.<br><br>
            <strong>SADIQ BHAI:</strong> This shop is very Trustable.. you can try it.. because gold and silver accuracy 100%.<br><br>
            <strong>Ghost:</strong> They Are Working Good And This Shop Owner Is Very Honest.. It's Work Is 👍🏻 Good …<br><br>
            <strong>Peter Stark:</strong> When we buy jewellery we always have to check authenticity because we pay huge money. Overall Good Service 👍 …<br><br>
            <strong>Sadiq Ji:</strong> Very Trusted Shop. And Works Good 👍🏻😊 …<br><br>
            <strong>Manish Kumar Rajput:</strong> Best shop in India. And the owner behavior is so good.<br><br>
            <strong>Trillionaire Dinner:</strong> Best Wholesale Shop in UP.. They Are Very Trusted And Classic.<br><br>
            <strong>Amit Gupta:</strong> They really care about their customers. Shri Ram Ji provides personalized service.<br><br>
            <strong>Ashlynn Nicholson:</strong> I was impressed with the accuracy of their testing. Shri Ram Ji is my go-to place now.<br><br>
            <strong>Tech Samrat:</strong> They use the latest technology for testing, ensuring accuracy. Highly recommended!<br><br>
            <strong>Altaf Alam:</strong> Best shop in market and respect his own customer.<br><br>
            <strong>Pop Corn:</strong> Amazing Work In The Market. And It's Trusted By Many Peoples..<br><br>
            <strong>Rajnish Kumar:</strong> Owner behaviour regarding customer is good.<br><br>
            <strong>Shivani Sharma:</strong> Best service available in this shop.<br><br>
            <strong>Priya Jha:</strong> I've been using Shri Ram Ji for years. Always precise and reliable.<br><br>
            <strong>Brijesh Gupta:</strong> Shri Ram Ji Computerised Touch is the best place for accurate silver testing. Highly recommend! Reliable and Trustworthy.<br><br>
            <strong>Dr. SHABEENA KHAN:</strong> This Is The Best Shop In The Market 🤠.<br><br>
            <strong>Pooja Garg:</strong> Accurate test results and good behaviour 👌.<br><br>
            <strong>Jatinseshya:</strong> Best services available here.<br><br>
            <strong>FF ZONE:</strong> Good behaviour and good service 💯.<br><br>
            <strong>Akanksha Salaria:</strong> Good work and good service.<br><br>
            <strong>Deepanshu Sharma:</strong> Best service 🙏🏻❤.<br><br>
            <strong>I'm BARAKOTI:</strong> Best service provider.<br>
        </div>
    </div>
    <div class="footer">
        <a class="button" href="mailto:shubhanggoyal4@gmail.com">Email Us</a>
        <a class="button" href="https://maps.app.goo.gl/PGAGbwWHAEa6HE5k6">Get Directions</a>
    </div>
    """, unsafe_allow_html=True)
