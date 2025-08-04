import streamlit as st
import random

# Khởi tạo session state cho lịch sử nếu chưa có
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("🎲 Game Tài Xỉu ")

dice_emojis = {
    1: "⚀",
    2: "⚁",
    3: "⚂",
    4: "⚃",
    5: "⚄",
    6: "⚅"
}

# Người dùng chọn cược
choice = st.radio("Chọn của bạn:", ["Tài (11-17)", "Xỉu (4-10)"])

# Khi người chơi nhấn nút
if st.button("Tung xúc xắc"):
    dice = [random.randint(1, 6) for _ in range(3)]
    total = sum(dice)

    result = "Xỉu" if 4 <= total <= 10 else "Tài"
    win = (choice.startswith(result))

    # Hiển thị xúc xắc
    st.markdown(
        f"<h1 style='font-size: 60px; text-align: center;'>{dice_emojis[dice[0]]} {dice_emojis[dice[1]]} {dice_emojis[dice[2]]}</h1>",
        unsafe_allow_html=True
    )

    st.write(f"Tổng: **{total}** → {result}")
    st.success("🎉 Bạn đã thắng!") if win else st.error("😢 Bạn đã thua!")

    # Lưu vào lịch sử
    st.session_state.history.append({
        "Bạn chọn": choice.split()[0],
        "Kết quả": result,
        "Tổng": total,
        "Kết luận": "Thắng" if win else "Thua"
    })

# Hiển thị lịch sử chơi
if st.session_state.history:
    st.subheader("📜 Lịch sử chơi")
    st.table(st.session_state.history)
