import streamlit as st

# Dữ liệu sản phẩm mẫu
products = {
    "Áo thun": {"price": 150000, "description": "Áo thun cotton thoáng mát", "image": "https://via.placeholder.com/150"},
    "Giày thể thao": {"price": 450000, "description": "Giày chạy bộ nhẹ và bền", "image": "https://via.placeholder.com/150"},
    "Túi xách": {"price": 250000, "description": "Túi xách thời trang nữ", "image": "https://via.placeholder.com/150"},
}
 
# Giao diện tiêu đề
st.set_page_config(page_title="Cửa hàng Online", layout="wide")
st.title("🛒 Cửa hàng Trực tuyến Mini")
st.markdown("Chào mừng bạn đến với cửa hàng của chúng tôi! Hãy chọn sản phẩm bạn yêu thích.")

# Hiển thị danh sách sản phẩm
for name, info in products.items():
    with st.container():
        cols = st.columns([1, 2])
        with cols[0]:
            st.image(info["image"], width=150)
        with cols[1]:
            st.subheader(name)
            st.write(info["description"])
            st.write(f"**Giá:** {info['price']:,} VND")
            quantity = st.number_input(f"Số lượng - {name}", min_value=0, step=1, key=name)
            if quantity > 0:
                st.success(f"Bạn đã thêm {quantity} {name} vào giỏ hàng.")

# Footer
st.markdown("---")
st.caption("© 2025 Cửa hàng mini. Được tạo bằng Streamlit.")

