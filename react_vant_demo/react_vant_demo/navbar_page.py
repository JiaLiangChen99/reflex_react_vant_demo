import reflex as rx
from react_vant_demo.reflex_react_vant import navbar, NavBar


class NavBarState(rx.State):
    """NavBar组件状态管理"""
    
    def handle_left_click(self):
        """处理左侧按钮点击事件"""
        return rx.toast.info("返回")
    
    def handle_right_click(self):
        """处理右侧按钮点击事件"""
        return rx.toast.info("按钮")


def basic_example() -> rx.Component:
    """基础用法"""
    return rx.card(
        rx.text("基础用法", size="4", style={"marginBottom": "16px"}),
        navbar(
            title="标题",
            left_text="< 返回",
            right_text="按钮",
            on_click_left=NavBarState.handle_left_click,
            on_click_right=NavBarState.handle_right_click
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def custom_content_example() -> rx.Component:
    """自定义内容"""
    return rx.card(
        rx.text("自定义内容", size="4", style={"marginBottom": "16px"}),
        navbar(
            title="标题",
            left_text="返回",
            right_text=rx.icon("search", size=20),
            on_click_left=NavBarState.handle_left_click,
            on_click_right=NavBarState.handle_right_click
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def left_arrow_example() -> rx.Component:
    """显示左侧箭头"""
    return rx.card(
        rx.text("显示左侧箭头", size="4", style={"marginBottom": "16px"}),
        navbar(
            title="< 标题",
            left_text="返回",
            on_click_left=NavBarState.handle_left_click
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def fixed_example() -> rx.Component:
    """固定在顶部"""
    return navbar(
            title="标题",
            left_text="< 返回",
            on_click_left=NavBarState.handle_left_click,
            fixed=True,
            placeholder=True
        )


def navbar_page() -> rx.Component:
    """NavBar导航栏组件示例页面"""
    return rx.container(
        rx.vstack(
            rx.text("NavBar 导航栏", size="5", weight="bold"),
            rx.text("为页面提供导航功能，常用于页面顶部", size="3"),
            
            basic_example(),
            custom_content_example(),
            left_arrow_example(),
            fixed_example(),
            spacing="8",
            align_items="stretch",
            style={"padding": "20px 0"}
        )
    )