import streamlit as st
import os

def save_data(data):
    with open("saved_text.txt", "a", encoding="utf-8") as file:
        file.write(data + "\n")
def load_text():
    if os.path.exists("saved_text.txt"):
        with open("saved_text.txt", "r", encoding="utf-8") as file:
            return file.readlines()[::-1]
    return []
def delete_all_data():
    if os.path.exists("saved_text.txt"):
        os.remove("saved_text.txt")
def main():
    st.title("Aɴᴏɴʏᴍᴏᴜs ᴄʜᴀᴛ")
    text_input = st.text_area("𝗪𝗿𝗶𝘁𝗲 𝘀𝗼𝗺𝗲𝘁𝗵𝗶𝗻𝗴:", key="text_input")
    save_button = st.button("𝙎𝙖𝙣𝙙 𝙢𝙚𝙨𝙨𝙖𝙜𝙚")
    if st.button("𝗥𝗲𝗳𝗿𝗲𝘀𝗵"):
        st.experimental_rerun()
    show_delete_button = st.checkbox("Show Delete Button")
    if show_delete_button and st.button("𝘿𝙚𝙡𝙚𝙩𝙚 𝙀𝙫𝙚𝙧𝙮𝙩𝙝𝙞𝙣𝙜"):
        delete_all_data()
        st.success("Deleted Successfully!")
    if save_button and text_input:
        save_data(text_input)
        st.success("𝗠𝗲𝘀𝘀𝗮𝗴𝗲 𝗦𝗲𝗻𝗱")
    saved_text = load_text()
    if saved_text:
        st.subheader("𝘾𝙝𝙖𝙩 𝙃𝙞𝙨𝙩𝙤𝙧𝙮")
        text_display = st.empty()
        text_display.write(saved_text)
    st.markdown(
        """<meta http-equiv="refresh" content="1000">""",
        unsafe_allow_html=True,
    )
if __name__ == "__main__":
    main()
