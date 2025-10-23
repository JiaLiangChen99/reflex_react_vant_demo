import reflex as rx
from typing import List, Dict, Any
from react_vant_demo.reflex_react_vant import dropdown_menu, dropdown_menu_item, cell


# 定义选项数据
option1 = [
    {"text": "全部商品", "value": ""},
    {"text": "新款商品", "value": "new"},
    {"text": "活动商品", "value": "activity"},
]

option2 = [
    {"text": "综合排序", "value": ""},
    {"text": "销量优先", "value": "sales"},
    {"text": "价格从低到高", "value": "price-asc"},
    {"text": "价格从高到低", "value": "price-desc"},
]

option3 = [
    {"text": "默认", "value": "default"},
    {"text": "仅看有货", "value": "instock"},
    {"text": "只看优惠", "value": "discount"},
]


class DropdownMenuState(rx.State):
    """
    DropdownMenu 组件的状态管理
    """
    # 基础用法的选中值
    basic_value: Dict[str, str] = {}
    
    # 自定义颜色的选中值
    custom_color_value: Dict[str, str] = {}
    
    # 向上展开的选中值
    up_direction_value: Dict[str, str] = {}
    
    # 禁用菜单的选中值
    disabled_value: Dict[str, str] = {}
    
    # 自定义内容的选中值
    custom_content_value: Dict[str, str] = {}
    
    # 筛选状态
    free_shipping: bool = False
    group_buy: bool = False
    
    @rx.event
    def handle_basic_change(self, value: Dict[str, str]):
        """处理基础用法的变化"""
        self.basic_value = value
    
    @rx.event
    def handle_custom_color_change(self, value: Dict[str, str]):
        """处理自定义颜色的变化"""
        self.custom_color_value = value
    
    @rx.event
    def handle_up_direction_change(self, value: Dict[str, str]):
        """处理向上展开的变化"""
        self.up_direction_value = value
    
    @rx.event
    def handle_disabled_change(self, value: Dict[str, str]):
        """处理禁用菜单的变化"""
        self.disabled_value = value
    
    @rx.event
    def handle_custom_content_change(self, value: Dict[str, str]):
        """处理自定义内容的变化"""
        self.custom_content_value = value
    
    @rx.event
    def toggle_free_shipping(self, checked: bool):
        """切换包邮选项"""
        self.free_shipping = checked
    
    @rx.event
    def toggle_group_buy(self, checked: bool):
        """切换团购选项"""
        self.group_buy = checked


def basic_example():
    """基础用法示例"""
    return rx.vstack(
        rx.text("基础用法", size="4"),
        dropdown_menu(
            dropdown_menu_item(name="value1", options=option1),
            dropdown_menu_item(name="value2", options=option2),
            dropdown_menu_item(name="value3", options=option3),
            value=DropdownMenuState.basic_value,
            on_change=DropdownMenuState.handle_basic_change,
        ),
        rx.text(f"当前选中值: {DropdownMenuState.basic_value}", size="3"),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def custom_content_example():
    """自定义菜单内容示例"""
    return rx.vstack(
        rx.text("自定义菜单内容", size="4"),
        dropdown_menu(
            dropdown_menu_item(name="value1", options=option1),
            dropdown_menu_item(
                cell(
                    center=True,
                    title="包邮",
                    # right_icon=rx.switch(
                    #     checked=DropdownMenuState.free_shipping,
                    #     on_change=DropdownMenuState.toggle_free_shipping
                    # )
                ),
                cell(
                    center=True,
                    title="团购",
                    # right_icon=rx.switch(
                    #     checked=DropdownMenuState.group_buy,
                    #     on_change=DropdownMenuState.toggle_group_buy
                    # )
            ),title="筛选", name="value2"),
            value=DropdownMenuState.custom_content_value,
            on_change=DropdownMenuState.handle_custom_content_change,
        ),
        rx.text(f"筛选状态 - 包邮: {DropdownMenuState.free_shipping}, 团购: {DropdownMenuState.group_buy}", size="3"),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def custom_color_example():
    """自定义高亮颜色示例"""
    return rx.vstack(
        rx.text("自定义高亮颜色", size="4"),
        dropdown_menu(
            dropdown_menu_item(name="value1", options=option1),
            dropdown_menu_item(name="value2", options=option2),
            active_color="#f44336",
            value=DropdownMenuState.custom_color_value,
            on_change=DropdownMenuState.handle_custom_color_change,
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def up_direction_example():
    """向上展开示例"""
    return rx.vstack(
        rx.text("向上展开", size="4"),
        dropdown_menu(
            dropdown_menu_item(name="value1", options=option1),
            dropdown_menu_item(name="value2", options=option2),
            direction="up",
            value=DropdownMenuState.up_direction_value,
            on_change=DropdownMenuState.handle_up_direction_change,
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def disabled_example():
    """禁用菜单示例"""
    return rx.vstack(
        rx.text("禁用菜单", size="4"),
        dropdown_menu(
            dropdown_menu_item(disabled=True, name="value1", options=option1),
            dropdown_menu_item(disabled=True, name="value2", options=option2),
            value=DropdownMenuState.disabled_value,
            on_change=DropdownMenuState.handle_disabled_change,
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def dropdown_menu_page():
    """DropdownMenu 组件示例页面"""
    return rx.container(
        rx.vstack(
            rx.heading("DropdownMenu 下拉菜单", size="2"),
            rx.divider(),
            basic_example(),
            custom_content_example(),
            custom_color_example(),
            up_direction_example(),
            disabled_example(),
            spacing="2",
            align_items="stretch",
            style={"max_width": "800px", "margin": "0 auto", "padding": "20px"}
        )
    )