import streamlit as st
from pathlib import Path
st.set_page_config(page_title="ArtVault", page_icon="🎨", layout="wide")
st.markdown("""<style>.stApp{background:#0b0b0d;color:#f7f7f7}.card{background:#121216;border:1px solid #25252b;border-radius:18px;padding:12px;margin-bottom:15px}.price{font-weight:800;font-size:18px}</style>""",unsafe_allow_html=True)
st.markdown('<h1>ArtVault 🎨</h1><p>Digital art marketplace — own art instantly.</p>',unsafe_allow_html=True)
arts=[
{"title":"Moonlit Soul","artist":"Aarav","cat":"Digital","price":149,"img":"https://images.unsplash.com/photo-1549490349-8643362247b5?auto=format&fit=crop&w=800&q=80"},
{"title":"Golden Silence","artist":"Mira","cat":"Painting","price":249,"img":"https://images.unsplash.com/photo-1579783902614-a3fb3927b6a5?auto=format&fit=crop&w=800&q=80"},
{"title":"The Wanderer","artist":"Rohan","cat":"Sketch","price":99,"img":"https://images.unsplash.com/photo-1513364776144-60967b0f800f?auto=format&fit=crop&w=800&q=80"},
{"title":"Neon Dreams","artist":"Zoya","cat":"Digital","price":199,"img":"https://images.unsplash.com/photo-1541701494587-cb58502866ab?auto=format&fit=crop&w=800&q=80"}]
if "cart" not in st.session_state: st.session_state.cart=[]
st.subheader("Featured artwork")
q=st.text_input("🔎 Search artwork...")
cat=st.selectbox("Category",["All","Painting","Sketch","Digital"])
items=[a for a in arts if (cat=="All" or a["cat"]==cat) and q.lower() in a["title"].lower()]
cols=st.columns(4)
for i,a in enumerate(items):
    with cols[i%4]:
        st.image(a["img"],use_container_width=True)
        st.markdown(f'**{a["title"]}**')
        st.caption(f'{a["cat"]} · by {a["artist"]}')
        st.markdown(f'<div class="price">₹{a["price"]}</div>',unsafe_allow_html=True)
        if st.button("Buy & download",key=f"buy{i}"): st.session_state.cart.append(a); st.success("Added to cart")
st.divider(); st.subheader("🛒 Cart")
if st.session_state.cart:
    total=sum(a["price"] for a in st.session_state.cart)
    for a in st.session_state.cart: st.write(f'{a["title"]} — ₹{a["price"]}')
    st.write(f"### Total: ₹{total}")
    upi=st.text_input("Enter UPI ID",placeholder="example@upi")
    if st.button("Pay with UPI & unlock"):
        if upi: st.success("Demo payment successful 🎉"); st.session_state.cart=[]
        else: st.warning("Please enter your UPI ID.")
else: st.caption("Your cart is empty.")
st.divider(); st.subheader("📱 Scan & Pay with PhonePe")
if Path("phonepe-upi-qr.png").exists(): st.image("phonepe-upi-qr.png",width=240)
else: st.info("Add phonepe-upi-qr.png beside app.py to display your QR code.")
st.divider(); st.subheader("🎨 Artist dashboard")
with st.form("artist"):
    title=st.text_input("Artwork title"); artist=st.text_input("Artist name"); category=st.selectbox("Category",["Painting","Sketch","Digital"]); price=st.number_input("Price in ₹",min_value=0,step=1); preview=st.file_uploader("Artwork preview",type=["png","jpg","jpeg","webp"]); ok=st.form_submit_button("Add artwork to store")
    if ok and title and artist and preview: st.success("Artwork added to your store.")
st.divider(); st.subheader("How ArtVault works"); st.write("1. Artists upload artwork → 2. Customers browse previews → 3. Customer pays → 4. High-resolution file becomes downloadable.")
st.caption("Demo MVP. Real payments and secure downloads require a payment gateway and backend verification. © 2026 ArtVault")
