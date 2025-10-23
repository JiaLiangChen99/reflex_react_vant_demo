from typing import Optional, Union, List, Dict, Any
from reflex.vars import Var
import reflex as rx
from .base import ReactVantBase

# 定义事件处理函数
def _on_change_spec(value: Dict[str, Any]) -> list[Var]:
    return [rx.Var(f"{value}")]

def _on_open_spec() -> list[Var]:
    return []

def _on_close_spec() -> list[Var]:
    return []

def _on_opened_spec() -> list[Var]:
    return []

def _on_closed_spec() -> list[Var]:
    return []

# 定义Option数据结构的类型
def _option_type(option: Dict[str, Any]) -> list[Var]:
    return [rx.Var(f"{option}")]

class DropdownMenu(ReactVantBase):
    """
    DropdownMenu 下拉菜单组件
    向下弹出的菜单列表。
    """
    tag = "DropdownMenu"
    _library = "react-vant"
    _component = "DropdownMenu"
    
    # 下拉菜单值
    value: Var[Optional[Dict[str, Any]]] = {}
    
    # 下拉菜单默认值
    default_value: Var[Optional[Dict[str, Any]]] = None
    
    # 是否禁用菜单
    disabled: Var[bool] = False
    
    # 菜单标题和选项的选中态颜色
    active_color: Var[Optional[str]] = "#ee0a24"
    
    # 自定义选项的选中态勾选icon
    active_icon: Var[Optional[Any]] = None
    
    # 菜单展开方向，可选值为up
    direction: Var[Optional[str]] = "down"
    
    # 菜单栏 z-index 层级
    z_index: Var[Union[float, str]] = 10
    
    # 动画时长，单位秒
    duration: Var[Union[float, str]] = 0.2
    
    # 是否显示遮罩层
    overlay: Var[bool] = True
    
    # 是否在点击遮罩层后关闭菜单
    close_on_click_overlay: Var[bool] = True
    
    # 是否在点击外部元素后关闭菜单
    close_on_click_outside: Var[bool] = True
    
    # 组件 value 变化时触发
    on_change: rx.EventHandler[_on_change_spec]
    
    # 打开菜单栏时触发
    on_open: rx.EventHandler[_on_open_spec]
    
    # 关闭菜单栏时触发
    on_close: rx.EventHandler[_on_close_spec]
    
    # 打开菜单栏且动画结束后触发
    on_opened: rx.EventHandler[_on_opened_spec]
    
    # 关闭菜单栏且动画结束后触发
    on_closed: rx.EventHandler[_on_closed_spec]

    style: dict = {'width': '100%'}

class DropdownMenu_Item(ReactVantBase):
    """
    DropdownMenu.Item 菜单项组件
    下拉菜单的单个选项。
    """
    tag = "DropdownMenu.Item"
    _library = "react-vant"
    _component = "DropdownMenu.Item"
    
    # 当前选中项对应的 value key
    name: Var[Union[str, int]] = ""
    
    # 菜单项标题
    title: Var[Optional[Any]] = None
    
    # 占位文本
    placeholder: Var[Optional[str]] = "请选择"
    
    # 选项数组
    options: List[Dict[str, Any]] = []
    
    # 是否禁用菜单
    disabled: Var[bool] = False
    
    # 标题额外类名
    title_class: Var[Optional[str]] = None
    
    # 指定挂载的节点
    teleport: Var[Optional[Any]] = None
    
    # 打开菜单栏时触发
    on_open: rx.EventHandler[_on_open_spec]
    
    # 关闭菜单栏时触发
    on_close: rx.EventHandler[_on_close_spec]
    
    # 打开菜单栏且动画结束后触发
    on_opened: rx.EventHandler[_on_opened_spec]
    
    # 关闭菜单栏且动画结束后触发
    on_closed: rx.EventHandler[_on_closed_spec]

    style: dict = {'width': '100%'}

# 按照官方示例的方式定义工厂函数
dropdown_menu = DropdownMenu.create
dropdown_menu_item = DropdownMenu_Item.create

# 将Item作为DropdownMenu的属性
# DropdownMenu.Item = DropdownMenu_Item

__all__ = ["DropdownMenu", "dropdown_menu", "DropdownMenu_Item", "dropdown_menu_item"]