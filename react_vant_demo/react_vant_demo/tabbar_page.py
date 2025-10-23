# pages.py
import reflex as rx
# from .reflex_react_vant.tabbar import bottom_navbar

def navbar_page():
    # def on_tab_click(index: int):
    #     print(f"点击了 tab {index}")

    # def on_tab_change(index: int):
    #     print(f"激活 tab 改变为 {index}")

    # tabs = [
    #     {"label": "首页", "icon": "home"},
    #     {"label": "搜索", "icon": "search"},
    #     {"label": "好友", "icon": "users"},
    #     {"label": "设置", "icon": "settings"},
    # ]

    # navbar = bottom_navbar(
    #     tabs=tabs,
    #     on_click=on_tab_click,
    #     on_change=on_tab_change,
    # )

    return rx.vstack(
        rx.text("这是页面内容", font_size="20px", padding=4),
        rx.spacer(),
        # navbar
    )
