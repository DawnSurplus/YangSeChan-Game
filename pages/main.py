#region Import
import streamlit as st
#endregion


#region Function
def run_selected_page(page_name):
    if page_name == "📚 Rule Description":
        home.run()
    elif page_name == "▶️ Play":
#endregion


#region UI
st.sidebar.title("메뉴")

page = st.sidebar.radio(
    "이동할 페이지를 선택하세요:",
    ["📚 Rule Description", "▶️ Play"]
)
#endregion



#region Main
run_selected_page(page)
#endregion