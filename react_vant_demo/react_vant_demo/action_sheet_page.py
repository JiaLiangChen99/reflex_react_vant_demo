import reflex as rx
from typing import List, Dict, Any
from react_vant_demo.reflex_react_vant import action_sheet, cell, button


class ActionSheetState(rx.State):
    """
    ActionSheet 组件的状态管理
    """
    # 基础用法的显示状态
    visible: int = -1
    
    # 选项状态的显示状态
    state_visible: bool = False
    
    # 自定义面板的显示状态
    custom_visible: bool = False
    
    # 选项数据
    actions = [
        {"name": "选项一"},
        {"name": "选项二"},
        {"name": "选项三"}
    ]
    
    actions_with_desc = [
        {"name": "选项一"},
        {"name": "选项二"},
        {"name": "选项三", "subname": "描述信息"},
    ]
    
    actions_with_state = [
        {"name": "选项一", "color": "#ee0a24"},
        {"name": "选项二", "disabled": True},
        {"loading": True},
    ]
    
    # 选择结果
    selected_result: str = ""
    
    @rx.event
    def handle_cancel(self):
        """处理取消事件"""
        self.visible = -1
        self.state_visible = False
        self.custom_visible = False
    
    @rx.event
    def handle_select(self, action: Dict[str, Any], index: int):
        """处理选项选择事件"""
        self.selected_result = f"选择了: {action.get('name', '加载中')}, 索引: {index}"
        
    @rx.event
    def handle_basic_open(self):
        """打开基础用法面板"""
        self.visible = 1
    
    @rx.event
    def handle_cancel_button_open(self):
        """打开带取消按钮的面板"""
        self.visible = 2
    
    @rx.event
    def handle_description_open(self):
        """打开带描述信息的面板"""
        self.visible = 3
    
    @rx.event
    def handle_state_open(self):
        """打开带选项状态的面板"""
        self.state_visible = True
    
    @rx.event
    def handle_custom_open(self):
        """打开自定义面板"""
        self.custom_visible = True


def basic_example():
    """基础用法示例"""
    return rx.vstack(
        rx.text("基础用法", size="4"),
        cell(
            title="基础用法",
            is_link=True,
            on_click=ActionSheetState.handle_basic_open
        ),
        action_sheet(
            visible=ActionSheetState.visible == 1,
            on_cancel=ActionSheetState.handle_cancel,
            actions=ActionSheetState.actions,
            on_select=ActionSheetState.handle_select
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def cancel_button_example():
    """展示取消按钮示例"""
    return rx.vstack(
        rx.text("展示取消按钮", size="4"),
        cell(
            title="展示取消按钮",
            is_link=True,
            on_click=ActionSheetState.handle_cancel_button_open
        ),
        action_sheet(
            visible=ActionSheetState.visible == 2,
            on_cancel=ActionSheetState.handle_cancel,
            actions=ActionSheetState.actions,
            cancel_text="取消",
            on_select=ActionSheetState.handle_select
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def description_example():
    """展示描述信息示例"""
    return rx.vstack(
        rx.text("展示描述信息", size="4"),
        cell(
            title="展示描述信息",
            is_link=True,
            on_click=ActionSheetState.handle_description_open
        ),
        action_sheet(
            visible=ActionSheetState.visible == 3,
            on_cancel=ActionSheetState.handle_cancel,
            description="这是一段描述信息",
            actions=ActionSheetState.actions_with_desc,
            cancel_text="取消",
            on_select=ActionSheetState.handle_select
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def option_state_example():
    """选项状态示例"""
    return rx.vstack(
        rx.text("选项状态", size="4"),
        cell(
            title="选项状态",
            is_link=True,
            on_click=ActionSheetState.handle_state_open
        ),
        action_sheet(
            visible=ActionSheetState.state_visible,
            on_cancel=ActionSheetState.handle_cancel,
            actions=ActionSheetState.actions_with_state,
            cancel_text="取消",
            on_select=ActionSheetState.handle_select
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def custom_panel_example():
    """自定义面板示例"""
    return rx.vstack(
        rx.text("自定义面板", size="4"),
        cell(
            title="自定义面板",
            is_link=True,
            on_click=ActionSheetState.handle_custom_open
        ),
        action_sheet(
            rx.el.div(
                    rx.text("这是自定义面板内容", size="4"),
                    rx.text("可以放置任何自定义组件", size="3"),
                    button("确认", on_click=ActionSheetState.handle_cancel),
                    style={"padding": "16px", "textAlign": "center"}
                ),
            visible=ActionSheetState.custom_visible,
            on_cancel=ActionSheetState.handle_cancel,
            title="自定义内容",
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def action_sheet_page():
    """ActionSheet 组件示例页面"""
    return rx.container(
        rx.vstack(
            rx.heading("ActionSheet 动作面板", size="2"),
            rx.divider(),
            rx.text("选择结果: " + ActionSheetState.selected_result, size="3"),
            basic_example(),
            cancel_button_example(),
            description_example(),
            option_state_example(),
            custom_panel_example(),
            spacing="2",
            align_items="stretch",
            style={"max_width": "600px", "margin": "0 auto", "padding": "20px"}
        )
    )