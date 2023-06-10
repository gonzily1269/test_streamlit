import streamlit as st

st.title("test")
st.caption("this is test")
st.subheader("あああ")


with st.form(key="name_form"):
    # テキストボックス
    name = st.text_input("name")

    # ボタン
    submit_button = st.form_submit_button("送信")

    if submit_button:
        st.text(f"ようこそ、{name}さん")
