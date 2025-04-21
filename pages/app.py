#region IMPORT
import streamlit as st
import rule
import game
#endregion





# 세션 상태 초기화
st.session_state.page = rule.RULE_PAGE_NAME



# 사이드바 메뉴
with st.sidebar:
    st.title("양세찬 게임 메뉴")
    menu = st.radio(
        "MENU",
        (rule.RULE_PAGE_NAME, game.GAME_PAGE_NAME),
    )
    st.session_state.page = menu



# show page
if st.session_state.page == rule.RULE_PAGE_NAME:
    rule.show_rule_page()
elif st.session_state.page == game.GAME_PAGE_NAME:
    game.show_game_page()
