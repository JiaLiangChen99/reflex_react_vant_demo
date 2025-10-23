from typing import Optional, Union, List, Dict
from reflex.vars import Var
import reflex as rx
from .base import ReactVantBase


def _on_change_spec(var: str | list[str]) -> list[Var]:
    return [rx.Var(f"{var}")]

def _on_confirm_spec():
    return []

def _on_cancel_spec():
    return []

def _on_stop_scroll_spec():
    return []

class Picker(ReactVantBase):
    """
    Picker 选择器组件
    提供多个选项集合供用户选择，支持单列选择和多列级联，通常与弹出层组件配合使用。
    """
    tag = "Picker"
    _library = "react-vant"
    _component = "Picker"
    
    # 选项数据
    columns: list[dict] | list[list] = []
    # 当前选中的值
    value: Var[Optional[str] | list[str]] = None
    
    # 顶部栏标题
    title: Var[Optional[str]] = "基础使用"
    
    # 是否显示加载状态
    loading: Var[bool] = False
    
    # 是否显示确认按钮
    show_confirm: Var[bool] = True
    
    # 是否显示取消按钮
    show_cancel: Var[bool] = True
    
    # 确认按钮文字
    confirm_text: Var[Optional[str]] = "确认"
    
    # 取消按钮文字
    cancel_text: Var[Optional[str]] = "取消"
    
    # 可见选项的数量
    visible_item_count: Var[Optional[int]] = 6
    
    # 选项改变时触发
    on_change: rx.EventHandler[_on_change_spec]

    # 点击确认按钮时触发
    on_confirm: rx.EventHandler[_on_confirm_spec]
    
    # 点击取消按钮时触发
    on_cancel: rx.EventHandler[_on_cancel_spec]
    
    # 滚动动画结束后触发
    on_stop_scroll: rx.EventHandler[_on_stop_scroll_spec]

    style = {'width': '100%'}

# 按照官方示例的方式定义工厂函数
picker = Picker.create


__all__ = ["Picker", "picker"]