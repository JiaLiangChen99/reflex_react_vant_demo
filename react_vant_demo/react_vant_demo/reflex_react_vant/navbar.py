from typing import Optional, Union, Any, Callable
from reflex.vars import Var
from .base import ReactVantBase
import reflex as rx

def _on_click_left_spec():
    return []

def _on_click_right_spec():
    return []

class NavBar(ReactVantBase):
    """NavBar 导航栏组件"""
    tag = "NavBar"
    
    # Props
    # 标题
    title: Var[Optional[Any]] = None
    
    # 左侧文案
    left_text: Var[Optional[Any]] = None
    
    # 右侧文案
    right_text: Var[Optional[Any]] = None
    
    # 自定义左侧箭头
    left_arrow: Var[bool] = False
    
    # 是否显示下边框
    border: Var[bool] = True
    
    # 是否固定在顶部
    fixed: Var[bool] = False
    
    # 导航栏 z-index
    z_index: Var[Union[int, str]] = 1
    
    # 固定在顶部时，是否在标签位置生成一个等高的占位元素
    placeholder: Var[bool] = False
    
    # 是否开启顶部安全区适配
    safe_area_inset_top: Var[bool] = False
    
    # 事件
    # 点击左侧按钮时触发
    on_click_left: rx.EventHandler[_on_click_left_spec] = None
    
    # 点击右侧按钮时触发
    on_click_right: rx.EventHandler[_on_click_right_spec] = None


def navbar(*children, **props) -> NavBar:
    """创建导航栏组件的工厂函数"""
    return NavBar.create(*children, **props)


__all__ = ["NavBar", "navbar"]