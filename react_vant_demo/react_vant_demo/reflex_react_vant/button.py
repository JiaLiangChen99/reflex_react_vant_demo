from typing import Optional, Union, List
from reflex.components.component import Component
from reflex.vars import Var
from .base import ReactVantBase


class Button(ReactVantBase):
    """Button 按钮组件。"""

    tag = "Button"

    # 按钮类型，可选值为 primary success warning danger info
    type: Var[Optional[str]] = None

    # 按钮尺寸，可选值为 large small mini
    size: Var[Optional[str]] = None

    # 是否为朴素按钮
    plain: Var[Optional[bool]] = None

    # 是否为细边框
    hairline: Var[Optional[bool]] = None

    # 是否为圆角按钮
    round: Var[Optional[bool]] = None

    # 是否为方形按钮
    square: Var[Optional[bool]] = None

    # 是否禁用按钮
    disabled: Var[Optional[bool]] = None

    # 是否为加载状态
    loading: Var[Optional[bool]] = None

    # 加载图标类型，可选值为 spinner circular
    loading_type: Var[Optional[str]] = None

    # 加载图标大小
    loading_size: Var[Optional[str]] = None

    # 自定义加载图标，优先级高于 loading_type
    loading_text: Var[Optional[str]] = None

    # 图标名称或图片链接
    icon: Var[Optional[str]] = None

    # 图标位置，可选值为 left right top bottom
    icon_position: Var[Optional[str]] = None

    # 是否为块级元素
    block: Var[Optional[bool]] = None

    # 按钮形状，可选值为 default round square
    shape: Var[Optional[str]] = None


# 按照官方示例的方式定义工厂函数
button = Button.create


__all__ = ["Button", "button"]