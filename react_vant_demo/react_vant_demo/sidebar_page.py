import reflex as rx
from .reflex_react_vant import sidebar, sidebar_item


class SidebarState(rx.State):
    """Sidebar组件的状态管理类"""
    # 当前选中的索引
    active: int = 2
    
    # 处理导航项切换事件
    def handle_change(self, index: int):
        self.active = index
        return rx.toast.info(f"标签名 {index + 1}")
    
    # 处理内容区切换事件
    def handle_content_change(self, index: int):
        self.active = index
        return rx.toast.info(f"内容区 {index + 1}")


def basic_usage():
    """基础用法示例"""
    return rx.card(
        rx.heading("基础用法", size="8", style={"marginBottom": "16px"}),
        sidebar(
            sidebar_item(
                "我是内容区1",
                title="标签名1",
                content_style={"backgroundColor": "#fff", "padding": "18px 10px"},
                ),
            sidebar_item(
                "我是内容区2",
                title="标签名2",
                content_style={"backgroundColor": "#fff", "padding": "18px 10px"},
                ),
            sidebar_item(
                "我是内容区3",
                title="标签名3",
                content_style={"backgroundColor": "#fff", "padding": "18px 10px"},
                ),
            value=SidebarState.active,
            on_change=SidebarState.handle_change,
        ),
    )


def badge_example():
    """徽标提示示例"""
    return rx.card(
        rx.heading("徽标提示", size="8", style={"marginBottom": "16px"}),
        sidebar(
            sidebar_item(title="标签名", dot=True),
            sidebar_item(title="标签名", badge=5),
            sidebar_item(title="标签名", badge=20),
            style={'height': '100vh'}
        ),
        style={'height': '100vh'}
    )


def disabled_example():
    """禁用选项示例"""
    return rx.card(
        rx.heading("禁用选项", size="8", style={"marginBottom": "16px"}),
        sidebar(
            sidebar_item(title="标签名"),
            sidebar_item(title="标签名", disabled=True),
            sidebar_item(title="标签名"),
        ),
    )


def custom_content_example():
    """自定义内容区示例"""
    return rx.card(
        rx.heading("自定义内容区", size="8", style={"marginBottom": "16px"}),
        sidebar(
            sidebar_item(
                "我是内容区1",
                title="内容1",
                content_style={"backgroundColor": "#fff", "padding": "18px 10px"},
            ),
            sidebar_item(
                "我是内容区2",
                title="内容2",
                content_style={"backgroundColor": "#fff", "padding": "18px 10px"},
            ),
            sidebar_item(
                "我是内容区3",
                title="内容3",
                content_style={"backgroundColor": "#fff", "padding": "18px 10px"},
            ),
            value=0,
            on_change=lambda v: rx.toast.info(f"内容区 {v + 1}"),
        ),
    )

def sidebar_page():
    """Sidebar组件示例页面"""
    return rx.fragment(
        sidebar(
            sidebar_item(
                rx.el.div("我是内容区1"),
                title="标签名1",
                content_style={
                    "backgroundColor": "#fff",
                    "padding": "18px 10px",
                    "minHeight": "100%",  # 内容区域也拉伸
                },
            ),
            sidebar_item(
                rx.el.div("我是内容区2"),
                title="标签名2",
                content_style={
                    "backgroundColor": "#fff",
                    "padding": "18px 10px",
                    "minHeight": "100%",
                },
            ),
            sidebar_item(
                rx.el.div("我是内容区3"),
                title="标签名3",
                content_style={
                    "backgroundColor": "#fff",
                    "padding": "18px 10px",
                    "minHeight": "100%",
                },
            ),
            value=SidebarState.active,
            on_change=SidebarState.handle_change,
            style={
                "height": "100vh",  # ✅ Sidebar 占满整个视口高度
                "backgroundColor": "#f5f5f5",  # 背景浅灰
                "display": "flex",  # 确保左右布局正常
                "flex": "1",
            },
            side_style={
                "backgroundColor": "#fff",
                "borderRight": "1px solid #eee",
                "minWidth": "100px",  # 左侧导航宽度
            },
        ),
    )
