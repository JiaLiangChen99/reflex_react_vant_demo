from typing import Optional, Union, Any, Dict, Callable
from reflex.vars import Var
from .base import ReactVantBase
import reflex as rx

def _on_change_spec(args: int):
    return [args]

class Sidebar(ReactVantBase):
    """Sidebar 侧边导航组件"""
    tag = "Sidebar"

    # 当前导航项的索引
    value: Var[Union[int, str]] = 0

    # 自定义类名
    class_name: Var[Optional[str]] = None

    # 自定义样式
    style: Var[Optional[Dict[str, Any]]] = None

    # 左侧容器类名
    side_class_name: Var[Optional[str]] = None

    # 左侧容器样式
    side_style: Var[Optional[Dict[str, Any]]] = None

    # 切换导航项时触发
    on_change: rx.EventHandler[_on_change_spec]

    style: Var[Dict[str, Any]] = {"width": "100%"}


def sidebar(*children, **props) -> Sidebar:
    """创建 Sidebar 组件"""
    return Sidebar.create(*children, **props)


class SidebarItem(ReactVantBase):
    """Sidebar.Item 侧边导航项"""
    tag = "Sidebar.Item"

    # 内容标题
    title: Var[Optional[Union[str, Any]]] = ""

    # 是否显示右上角小红点
    dot: Var[bool] = False

    # 图标右上角徽标内容
    badge: Var[Optional[Union[int, str]]] = None

    # 是否禁用该项
    disabled: Var[bool] = False

    # 内容区域类名
    content_class_name: Var[Optional[str]] = None

    # 内容区域样式
    content_style: Var[Optional[Dict[str, Any]]] = None

    # 点击事件
    on_click: Optional[Callable[[int], None]] = None


# 注册 SidebarItem 以便 Sidebar.Item 语法生效
Sidebar.Item = SidebarItem


def sidebar_item(*children, **props) -> SidebarItem:
    """创建 Sidebar.Item 组件"""
    return SidebarItem.create(*children, **props)


__all__ = ["Sidebar", "sidebar", "SidebarItem", "sidebar_item"]
