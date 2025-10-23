from typing import Optional, Union, Dict, Any
from reflex.vars import Var
import reflex as rx
from .base import ReactVantBase


class Empty(ReactVantBase):
    """
    Empty组件用于显示空状态时的占位提示。
    """
    # 组件的标签名称
    tag = "Empty"
    children: Var[Optional[rx.Component]] = None
    
    # 图片类型，可选值为 error network search，支持传入图片 URL
    image: Var[Optional[Union[str, rx.Component]]] = None
    
    # 图片下方的描述文字
    description: Var[Optional[rx.Component] | str] = None
    
    # 组件样式
    style: Dict[str, Any] = {}
    
    # 图片大小
    image_size: Var[Optional[int]] = None
    
    style: dict[str, str] = {'width': '100%'}

# 按照官方示例的方式定义工厂函数
empty = Empty.create

__all__ = ["Empty", "empty"]