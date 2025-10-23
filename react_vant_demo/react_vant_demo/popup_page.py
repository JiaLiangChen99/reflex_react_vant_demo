import reflex as rx
from .reflex_react_vant import Popup, popup, cell, button, flex, flex_item, space


class PopupDemoState(rx.State):
    """Popup 组件演示状态管理。"""
    
    # 基础弹窗显示状态
    basic_visible: bool = False
    
    # 位置弹窗状态
    position: str = ""
    
    # 关闭图标弹窗状态
    show_close_icon: bool = False
    show_custom_close_icon: bool = False
    show_custom_icon_position: bool = False
    
    # 圆角弹窗状态
    round_visible: bool = False
    
    # 标题弹窗状态
    title_visible: bool = False
    
    @rx.event
    def set_basic_visible(self, visible: bool):
        """设置基础弹窗显示状态。"""
        self.basic_visible = visible

    def open_position_popup(self, pos: str):
        """打开位置弹窗。"""
        self.position = pos
    
    def close_position_popup(self):
        """关闭位置弹窗。"""
        self.position = ""

    @rx.event
    def set_show_close_icon(self, visible: bool):
        """设置显示关闭图标弹窗状态。"""
        self.show_close_icon = visible

    @rx.event
    def set_show_custom_close_icon(self, visible: bool):
        """设置显示自定义关闭图标弹窗状态。"""
        self.show_custom_close_icon = visible

    @rx.event
    def set_show_custom_icon_position(self, visible: bool):
        """设置显示自定义图标位置弹窗状态。"""
        self.show_custom_icon_position = visible

    @rx.event
    def set_round_visible(self, visible: bool):
        """设置圆角弹窗显示状态。"""
        self.round_visible = visible

    @rx.event
    def set_title_visible(self, visible: bool):
        """设置标题弹窗显示状态。"""
        self.title_visible = visible


def basic_popup_demo() -> rx.Component:
    """基础用法演示。"""
    return rx.vstack(
        rx.heading("基础用法", size="5"),
        rx.text("通过 visible 以及 onClose 控制弹出层是否展示"),
        rx.el.div(
            cell(title="展示弹出层", is_link=True, on_click=PopupDemoState.set_basic_visible(True)),
            popup(
                rx.el.div("内容", style={"padding": "30px 50px"}),
                visible=PopupDemoState.basic_visible,
                on_close=PopupDemoState.set_basic_visible(False),
                closeable=True,
                overlay=True,
                close_on_click_overlay=True,
                style={"z-index": "2000"}
            ),
        ),
        width="100%",
        margin_bottom="2em"
    )


def position_popup_demo() -> rx.Component:
    """弹出位置演示。"""
    return rx.vstack(
        rx.heading("弹出位置", size="5"),
        rx.text("通过 position 属性设置弹出位置，支持 top、bottom、left、right"),
        rx.el.div(
            flex(
                flex_item(cell(title="顶部弹出", is_link=True, on_click=lambda: PopupDemoState.open_position_popup("top"))),
                flex_item(cell(title="底部弹出", is_link=True, on_click=lambda: PopupDemoState.open_position_popup("bottom"))),
                justify="space-around",
                margin_bottom="1em"
            ),
            flex(
                flex_item(cell(title="左侧弹出", is_link=True, on_click=lambda: PopupDemoState.open_position_popup("left"))),
                flex_item(cell(title="右侧弹出", is_link=True, on_click=lambda: PopupDemoState.open_position_popup("right"))),
                justify="space-around"
            ),
            # 顶部弹窗
            popup(
                rx.el.div("顶部弹出内容", style={"padding": "30px", "textAlign": "center"}),
                visible=PopupDemoState.position == "top",
                position="top",
                on_close=PopupDemoState.close_position_popup,
                closeable=True,
                style={"height": "30%", "z-index": "2000"}
            ),
            # 底部弹窗
            popup(
                rx.el.div("底部弹出内容", style={"padding": "30px", "textAlign": "center"}),
                visible=PopupDemoState.position == "bottom",
                position="bottom",
                on_close=PopupDemoState.close_position_popup,
                closeable=True,
                style={"height": "30%", "z-index": "2000"}
            ),
            # 左侧弹窗
            popup(
                rx.el.div("左侧弹出内容", style={"padding": "30px", "textAlign": "center"}),
                visible=PopupDemoState.position == "left",
                position="left",
                on_close=PopupDemoState.close_position_popup,
                closeable=True,
                style={"width": "30%", "height": "100%", "z-index": "2000"}
            ),
            # 右侧弹窗
            popup(
                rx.el.div("右侧弹出内容", style={"padding": "30px", "textAlign": "center"}),
                visible=PopupDemoState.position == "right",
                position="right",
                on_close=PopupDemoState.close_position_popup,
                closeable=True,
                style={"width": "30%", "height": "100%", "z-index": "2000"}
            ),
        ),
        width="100%",
        margin_bottom="2em"
    )


def close_icon_popup_demo() -> rx.Component:
    """关闭图标演示。"""
    return rx.vstack(
        rx.heading("关闭图标", size="5"),
        rx.text("设置 closeable 属性后，会在弹出层的右上角显示关闭图标"),
        rx.el.div(
            cell(title="默认关闭图标", is_link=True, on_click=PopupDemoState.set_show_close_icon(True)),
            cell(title="自定义关闭图标", is_link=True, on_click=PopupDemoState.set_show_custom_close_icon(True)),
            cell(title="自定义图标位置", is_link=True, on_click=PopupDemoState.set_show_custom_icon_position(True)),
            
            # 默认关闭图标
            popup(
                rx.el.div("默认关闭图标", style={"padding": "30px", "textAlign": "center"}),
                visible=PopupDemoState.show_close_icon,
                position="bottom",
                closeable=True,
                on_close=PopupDemoState.set_show_close_icon(False),
                style={"height": "30%", "z-index": "2000"}
            ),
            
            # 自定义关闭图标
            popup(
                rx.el.div("自定义关闭图标", style={"padding": "30px", "textAlign": "center"}),
                visible=PopupDemoState.show_custom_close_icon,
                position="bottom",
                closeable=True,
                close_icon="fire",  # 使用React-Vant内置图标名称
                on_close=PopupDemoState.set_show_custom_close_icon(False),
                style={"height": "30%", "z-index": "2000"}
            ),
            
            # 自定义图标位置
            popup(
                rx.el.div("自定义图标位置", style={"padding": "30px", "textAlign": "center"}),
                visible=PopupDemoState.show_custom_icon_position,
                position="bottom",
                closeable=True,
                close_icon_position="top-left",
                on_close=PopupDemoState.set_show_custom_icon_position(False),
                style={"height": "30%", "z-index": "2000"}
            ),
        ),
        width="100%",
        margin_bottom="2em"
    )


def round_popup_demo() -> rx.Component:
    """圆角弹窗演示。"""
    return rx.vstack(
        rx.heading("圆角弹窗", size="5"),
        rx.text("设置 round 属性后，弹窗会根据弹出位置添加不同的圆角样式"),
        rx.el.div(
            cell(title="圆角弹窗", is_link=True, on_click=PopupDemoState.set_round_visible(True)),
            popup(
                rx.el.div("圆角弹窗内容", style={"padding": "30px", "textAlign": "center"}),
                visible=PopupDemoState.round_visible,
                position="bottom",
                closeable=True,
                round=True,
                on_close=PopupDemoState.set_round_visible(False),
                style={"height": "30%", "z-index": "2000"}
            ),
        ),
        width="100%",
        margin_bottom="2em"
    )


def title_popup_demo() -> rx.Component:
    """标题弹窗演示。"""
    return rx.vstack(
        rx.heading("标题弹窗", size="5"),
        rx.text("设置 title 和 description 属性后，弹窗会显示标题和描述文字"),
        rx.el.div(
            cell(title="标题弹窗", is_link=True, on_click=PopupDemoState.set_title_visible(True)),
            popup(
                visible=PopupDemoState.title_visible,
                position="bottom",
                closeable=True,
                round=True,
                title="标题",
                description="这是一段很长很长的描述这是一段很长很长的描述这是一段很长很长的描述这是一段很长很长的描述",
                on_close=PopupDemoState.set_title_visible(False),
                style={"height": "30%", "z-index": "2000"}
            ),
        ),
        width="100%"
    )


def popup_page() -> rx.Component:
    """Popup 组件演示页面。"""
    return rx.vstack(
        rx.heading("Popup Demo", size="6"),
        rx.text("Reflex wrapper for the React-Vant UI library - Popup 组件"),
        basic_popup_demo(),
        position_popup_demo(),
        close_icon_popup_demo(),
        round_popup_demo(),
        title_popup_demo(),
        spacing="6",
        padding="2em",
        align="stretch",
        max_width="800px",
    )