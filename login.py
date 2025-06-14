import streamlit as st

# Danh sách người dùng mẫu
users = {
    "admin": "admin123",
    "user1": "pass1",
    "user2": "pass2"
}

# Hàm kiểm tra đăng nhập
def login(username, password):
    return username in users and users[username] == password

# Tạo giao diện đăng nhập
def login_page():
    st.title("🔐 Đăng nhập hệ thống")

    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    login_button = st.button("Đăng nhập")

    if login_button:
        if login(username, password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"Chào mừng {username}!")
        else:
            st.error("Sai tên đăng nhập hoặc mật khẩu.")

# Trang chính sau khi đăng nhập
def main_page():
    st.title("🎉 Chào mừng đến trang chính!")
    st.write(f"Bạn đang đăng nhập với tài khoản: **{st.session_state['username']}**")
    if st.button("Đăng xuất"):
        st.session_state["logged_in"] = False
        st.experimental_rerun()

# Chạy app
def main():
    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    if st.session_state["logged_in"]:
        main_page()
    else:
        login_page()

if __name__ == "__main__":
    main()
