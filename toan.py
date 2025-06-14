import streamlit as st
import json
import os

USER_FILE = "users.json"

# Tạo file users.json nếu chưa tồn tại
if not os.path.exists(USER_FILE):
    with open(USER_FILE, "w") as f:
        json.dump({}, f)

# Đọc danh sách người dùng
def load_users():
    with open(USER_FILE, "r") as f:
        return json.load(f)

# Ghi danh sách người dùng
def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

# Giao diện đăng nhập
def login_page():
    st.subheader("🔐 Đăng nhập")
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    if st.button("Đăng nhập"):
        users = load_users()
        if username in users and users[username] == password:
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.success(f"Đăng nhập thành công! Xin chào {username}")
        else:
            st.error("Tên đăng nhập hoặc mật khẩu không đúng.")

# Giao diện đăng ký
def register_page():
    st.subheader("📝 Đăng ký tài khoản")
    new_username = st.text_input("Tên đăng nhập mới")
    new_password = st.text_input("Mật khẩu mới", type="password")
    if st.button("Đăng ký"):
        users = load_users()
        if new_username in users:
            st.warning("Tên đăng nhập đã tồn tại.")
        elif new_username == "" or new_password == "":
            st.warning("Vui lòng nhập đầy đủ thông tin.")
        else:
            users[new_username] = new_password
            save_users(users)
            st.success("Đăng ký thành công! Bây giờ bạn có thể đăng nhập.")

# Trang chính sau đăng nhập
def main_page():
    st.title("🎉 Chào mừng đến trang chính!")
    st.write(f"Xin chào **{st.session_state['username']}** 👋")
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# Hàm chính
def main():
    st.title("Hệ thống đăng nhập/đăng ký")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    menu = st.sidebar.selectbox("Chọn chức năng", ["Đăng nhập", "Đăng ký"])

    if st.session_state["logged_in"]:
        main_page()
    elif menu == "Đăng nhập":
        login_page()
    elif menu == "Đăng ký":
        register_page()

if __name__ == "__main__":
    main()
