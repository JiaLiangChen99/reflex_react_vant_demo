from typing import Optional, Union, List
from reflex.components.component import Component
from reflex.vars import Var
from .base import ReactVantBase


class Space(ReactVantBase):
    """Space 间距组件。
    
    用于设置组件之间的间距，避免组件紧贴在一起，拉开统一的空间。
    """

    tag = "Space"

    # 间距大小
    gap: Var[Optional[Union[str, int, List[Union[str, int]]]]] = None

    # 主轴对齐方式
    justify: Var[Optional[str]] = None

    # 交叉轴对齐方式
    align: Var[Optional[str]] = None

    # 间距方向
    direction: Var[Optional[str]] = "horizontal"

    # 是否自动换行，仅在 horizontal 时有效
    wrap: Var[Optional[bool]] = None

    # 是否渲染为块级元素
    block: Var[Optional[bool]] = None

    # 分隔符
    divider: Var[Optional[Component]] = None


# 按照官方示例的方式定义工厂函数
space = Space.create


__all__ = ["Space", "space"]