import reflex as rx
from .reflex_react_vant import checkbox, checkbox_group


class CheckboxDemoState(rx.State):
    """Checkbox 组件演示状态管理。"""
    
    # 单个复选框状态
    checked: bool = False
    
    # 复选框组选中的值
    selected: list[str] = []
    
    # 水平排列的复选框组值
    horizontal_values: list[str] = []
    
    # 禁用状态的复选框组值
    disabled_values: list[str] = ["a"]
    
    # 最多选择2个的复选框组值
    max_values: list[str] = []
    
    @rx.event
    def toggle_checked(self, val: bool):
        """处理单个复选框变化。"""
        self.checked = val
    
    @rx.event
    def on_group_change(self, values: list[str]):
        """处理复选框组变化。"""
        self.selected = values
    
    @rx.event
    def handle_horizontal_change(self, values: list):
        """处理水平复选框组变化。"""
        self.horizontal_values = values
    
    @rx.event
    def handle_disabled_change(self, values: list):
        """处理禁用复选框组变化。"""
        self.disabled_values = values
    
    @rx.event
    def handle_max_change(self, values: list):
        """处理最多选择数量的复选框组变化。"""
        self.max_values = values


def checkbox_demo() -> rx.Component:
    """Checkbox 组件演示页面。"""
    return rx.vstack(
        rx.heading("Checkbox 复选框", size="6"),
        rx.text("Reflex wrapper for the React-Vant UI library - Checkbox 组件"),
        
        # 基本用法
        rx.card(
            rx.heading("基本用法", size="5"),
            rx.hstack(
                checkbox(
                    "复选框",
                    checked=CheckboxDemoState.checked,
                    on_change=CheckboxDemoState.toggle_checked,
                ),
            ),
            rx.text(f"选中状态: {CheckboxDemoState.checked}"),
            padding="16px"
        ),
        
        # 默认状态
        rx.card(
            rx.heading("默认状态", size="5"),
            rx.vstack(
                checkbox("默认勾选", default_checked=True),
                checkbox("禁用复选框", disabled=True),
                checkbox("禁用且选中", default_checked=True, disabled=True),
                checkbox("禁止文本点击", default_checked=True, label_disabled=True),
            ),
            padding="16px"
        ),
        
        # 复选框组
        rx.card(
            rx.heading("复选框组", size="5"),
            checkbox_group(
                checkbox("苹果", name="apple"),
                checkbox("香蕉", name="banana"),
                checkbox("葡萄", name="grape"),
                value=CheckboxDemoState.selected,
                on_change=CheckboxDemoState.on_group_change,
            ),
            rx.text(f"选中的值: {CheckboxDemoState.selected}"),
            padding="16px"
        ),
        
        # 水平排列
        rx.card(
            rx.heading("水平排列", size="5"),
            checkbox_group(
                checkbox("选项 A", name="a"),
                checkbox("选项 B", name="b"),
                checkbox("选项 C", name="c"),
                direction="horizontal",
                value=CheckboxDemoState.horizontal_values,
                on_change=CheckboxDemoState.handle_horizontal_change,
            ),
            padding="16px"
        ),
        
        # 最大选择数量
        rx.card(
            rx.heading("最大选择数量", size="5"),
            checkbox_group(
                checkbox("选项 1", name="1"),
                checkbox("选项 2", name="2"),
                checkbox("选项 3", name="3"),
                checkbox("选项 4", name="4"),
                max=2,
                value=CheckboxDemoState.max_values,
                on_change=CheckboxDemoState.handle_max_change,
            ),
            rx.text("最多只能选择2个"),
            padding="16px"
        ),
        
        # 不同形状和颜色
        rx.card(
            rx.heading("自定义样式", size="5"),
            rx.vstack(
                rx.heading("不同形状", size="4"),
                rx.hstack(
                    checkbox("圆角", shape="round"),
                    checkbox("方形", shape="square"),
                ),
                rx.heading("自定义颜色", size="4"),
                checkbox_group(
                    checkbox("红色", name="red", checked_color="#ee0a24"),
                    checkbox("绿色", name="green", checked_color="#07c160"),
                    checkbox("蓝色", name="blue", checked_color="#1989fa"),
                ),
            ),
            padding="16px"
        ),
        
        spacing="6",
        padding="2em",
        align="stretch",
        max_width="800px"
    )
