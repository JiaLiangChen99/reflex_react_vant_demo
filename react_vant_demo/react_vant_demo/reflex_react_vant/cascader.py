import reflex as rx
from reflex import Var
from typing import Optional, List, Dict, Any, Union, Literal
from .base import ReactVantBase


# ------------------- 事件定义 -------------------

def _on_change_spec(val: str, rows: str) -> list[Var]:
    """选中项变化"""
    return [Var(f"{{ value: {val}, rows: {rows} }}")]

def _on_finish_spec(val: str, rows: str) -> list[Var]:
    """选择完成"""
    return [Var(f"{{ value: {val}, rows: {rows} }}")]

def _on_close_spec() -> list[Var]:
    """点击关闭图标"""
    return []

def _on_click_tab_spec(tab_index: str, title: str) -> list[Var]:
    """点击标签"""
    return [Var(f"{{ tabIndex: {tab_index}, title: {title} }}")]


# ------------------- 组件定义 -------------------

class Cascader(ReactVantBase):
    """ReactVant Cascader 级联选择组件"""

    tag = "Cascader"

    # 基本属性
    title: Optional[str] = None
    value: Optional[List[str]] = None
    default_value: Optional[List[str]] = None
    placeholder: Optional[str] = None
    active_color: Optional[str] = None
    closeable: Optional[bool] = None
    close_icon: Optional[str] = None

    # 选项数据
    options: Optional[List[Dict[str, Any]]] = None
    field_names: Optional[Dict[str, str]] = None


    # 事件
    on_change: rx.EventHandler[_on_change_spec]
    on_finish: rx.EventHandler[_on_finish_spec]
    on_close: rx.EventHandler[_on_close_spec]
    on_click_tab: rx.EventHandler[_on_click_tab_spec]

    @classmethod
    def create(cls, *children, **props):
        return super().create(*children, **props)


def cascader(**props):
    """Cascader 工厂函数"""
    return Cascader.create(**props)
