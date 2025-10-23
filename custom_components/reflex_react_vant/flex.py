from typing import Optional, Union, List, Tuple
from reflex.components.component import Component
from reflex.components.tags import Tag
from reflex.vars import Var
from .base import ReactVantBase


class Flex(ReactVantBase):
    """Flex 布局组件，是 CSS flex 布局的封装。"""

    tag = "Flex"

    # 项目定位方向，可选值为 row row-reverse column column-reverse
    direction: Var[Optional[str]] = None

    # 子元素的换行方式，可选值为 nowrap wrap wrap-reverse
    wrap: Var[Optional[str]] = None

    # 列元素之间的间距。可以使用数组形式同时设置 [水平间距, 垂直间距]
    gutter: Var[Optional[Union[int, List[int], Tuple[int, int]]]] = None

    # 垂直对齐方式，可选值为 start center end baseline stretch
    align: Var[Optional[str]] = None

    # 水平排列方式，可选值为 start end center around between
    justify: Var[Optional[str]] = None


class FlexItem(ReactVantBase):
    """Flex 布局的子项组件。"""

    tag = "Flex.Item"

    # flex 布局属性
    flex: Var[Optional[Union[str, int]]] = None

    # 栅格占位格数，为 0 时相当于 display: none
    span: Var[Optional[int]] = None


# 按照官方示例的方式定义工厂函数
flex = Flex.create
flex_item = FlexItem.create


__all__ = ["Flex", "FlexItem", "flex", "flex_item"]