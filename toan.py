import streamlit as st
import sqlite3

# Kết nối hoặc tạo mới CSDL SQLite
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Tạo bảng nếu chưa có
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT NOT NULL
    )
''')
conn.commit()

# Thêm người dùng mới
def register_user(username, password):
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # Username đã tồn tại

# Kiểm tra đăng nhập
def check_login(username, password):
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    return cursor.fetchone() is not None

# Giao diện đăng nhập
def login_page():
    st.subheader("🔐 Đăng nhập")
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    if st.button("Đăng nhập"):
        if check_login(username, password):
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
        if new_username == "" or new_password == "":
            st.warning("Vui lòng nhập đầy đủ thông tin.")
        elif register_user(new_username, new_password):
            st.success("Đăng ký thành công! Bây giờ bạn có thể đăng nhập.")
        else:
            st.warning("Tên đăng nhập đã tồn tại.")

# Trang chính sau khi đăng nhập
def main_page():
    st.title("🎉 Trang chính")
    st.write(f"Chào mừng **{st.session_state['username']}** đến với hệ thống.")
    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.experimental_rerun()

# Chạy ứng dụng
def main():
    st.title("Hệ thống đăng nhập/đăng ký với SQLite")

    if "logged_in" not in st.session_state:
        st.session_state["logged_in"] = False

    menu = st.sidebar.radio("Chọn chức năng", ["Đăng nhập", "Đăng ký"])

    if st.session_state["logged_in"]:
        main_page()
    elif menu == "Đăng nhập":
        login_page()
    elif menu == "Đăng ký":
        register_page()

if __name__ == "__main__":
    main()
