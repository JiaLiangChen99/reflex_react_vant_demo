from typing import Optional, Union, Dict, Any
from reflex.components.component import Component
from reflex.vars import Var
from .base import ReactVantBase


class Image(ReactVantBase):
    """Image 图片组件。
    
    增强版的 img 标签，提供多种图片填充模式，支持图片懒加载、加载中提示、加载失败提示。
    """

    tag = "Image"

    # 图片链接
    src: Var[Optional[str]] = None

    # 图片填充模式，可选值：contain、cover、fill、none、scale-down
    fit: Var[Optional[str]] = "fill"

    # 替代文本
    alt: Var[Optional[str]] = None

    # 宽度，默认单位为 px
    width: Var[Optional[Union[str, int]]] = None

    # 高度，默认单位为 px
    height: Var[Optional[Union[str, int]]] = None

    # 圆角大小，默认单位为 px
    radius: Var[Optional[Union[str, int]]] = 0

    # 是否显示为圆形
    round: Var[Optional[bool]] = False

    # 是否开启懒加载
    lazyload: Var[Optional[Union[bool, Dict[str, Any]]]] = False

    # 是否展示图片加载失败提示
    show_error: Var[Optional[bool]] = True

    # 是否展示图片加载中提示
    show_loading: Var[Optional[bool]] = True

    # 失败时提示的图标或内容
    error_icon: Var[Optional[Union[Component, str]]] = None

    # 加载时提示的图标或内容
    loading_icon: Var[Optional[Union[Component, str]]] = None

    # 加载图标和失败图标的大小
    icon_size: Var[Optional[Union[str, int]]] = "32px"


# 定义工厂函数
image = Image.create


__all__ = [
    "Image",
    "image",
]