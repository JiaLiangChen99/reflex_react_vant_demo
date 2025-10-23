# bottom_navbar.py
import reflex as rx
from typing import List, Dict, Callable, Optional

class BottomNavbarState(rx.ComponentState):
    """每个 BottomNavbar 实例的状态"""
    active_index: int = 0  # 当前激活的 tab
    tabs: List[Dict[str, str]] = []  # 每个 tab: {"label": str, "icon": str}

    # 父组件可以传入的回调
    on_click: Optional[Callable[[int], None]] = None
    on_change: Optional[Callable[[int], None]] = None

    @rx.event
    def set_active(self, index: int):
        """设置激活 tab"""
        self.active_index = index
        # 调用 on_change 回调，如果有的话
        if self.on_change:
            self.on_change(index)

    @rx.event
    def handle_click(self, index: int):
        """点击 tab"""
        self.set_active(index)
        # 调用 on_click 回调，如果有的话
        if self.on_click:
            self.on_click(index)

    @classmethod
    def get_component(cls, **props):
        """
        渲染底部导航栏
        props:
            tabs: List[Dict[str, str]] -> 每个 tab 的 label 和 icon
            height: int -> 导航栏高度，默认 60px
            bg_color: str -> 背景色，默认白色
            active_color: str -> 激活 tab 颜色
            inactive_color: str -> 未激活 tab 颜色
            on_click: Callable[[int], None] -> 点击事件
            on_change: Callable[[int], None] -> 改变激活 tab 事件
        """
        tabs = props.pop("tabs", cls.tabs)
        height = props.pop("height", 60)
        bg_color = props.pop("bg_color", "white")
        active_color = props.pop("active_color", "#3f45ff")
        inactive_color = props.pop("inactive_color", "#7d7e80")
        cls.on_click = props.pop("on_click", None)
        cls.on_change = props.pop("on_change", None)

        # 渲染每个 tab
        tab_buttons = []
        for i, tab in enumerate(tabs):
            is_active = i == cls.active_index
            color = active_color if is_active else inactive_color

            tab_button = rx.vstack(
                rx.icon(tab.get("icon", "circle")),
                rx.text(tab.get("label", ""), color=color, font_size="12px"),
                align="center",
                spacing=2,
                flex=1,
                on_click=lambda i=i: cls.handle_click(i),  # 每个 tab 都有事件
            )
            tab_buttons.append(tab_button)

        return rx.hstack(
            *tab_buttons,
            height=f"{height}px",
            bg=bg_color,
            width="100%",
            position="fixed",
            bottom="0px",
            box_shadow="0 -2px 5px rgba(0,0,0,0.1)",
            **props,
        )

# 工厂方法
bottom_navbar = BottomNavbarState.create
