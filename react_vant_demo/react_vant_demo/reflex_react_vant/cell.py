from typing import Optional, Union, List
from reflex.components.component import Component
from reflex.vars import Var
from .base import ReactVantBase


class Cell(ReactVantBase):
    """Cell 单元格组件。
    
    单元格为列表中的单个展示项，常用于展示信息、链接或操作。
    """

    tag = "Cell"

    # 左侧标题
    title: Var[Optional[Union[str, Component]]] = None

    # 右侧内容
    value: Var[Optional[Union[str, int]]] = None

    # 标题下方的描述信息
    label: Var[Optional[Union[str, Component]]] = None

    # 自定义单元格最右侧的额外内容
    extra: Var[Optional[Union[str, Component]]] = None

    # 单元格大小，可选值为 large
    size: Var[Optional[str]] = None

    # 左侧图标
    icon: Var[Optional[Component]] = None

    # 自定义右侧按钮，默认为箭头
    right_icon: Var[Optional[Component]] = None

    # 是否显示内边框
    border: Var[Optional[bool]] = True

    # 是否在跳转时替换当前页面历史
    replace: Var[Optional[bool]] = False

    # 是否开启点击反馈
    clickable: Var[Optional[bool]] = False

    # 是否展示右侧箭头并开启点击反馈
    is_link: Var[Optional[bool]] = False

    # 是否显示表单必填星号
    required: Var[Optional[bool]] = False

    # 是否使内容垂直居中
    center: Var[Optional[bool]] = False

    # 箭头方向，可选值为 left up down
    arrow_direction: Var[Optional[str]] = "right"

    # 左侧标题额外样式
    title_style: Var[Optional[str]] = None

    # 左侧标题额外类名
    title_class: Var[Optional[str]] = None

    # 右侧内容额外类名
    value_class: Var[Optional[str]] = None

    # 描述信息额外类名
    label_class: Var[Optional[str]] = None

    style: dict = {'width': '100%'}

class CellGroup(ReactVantBase):
    """Cell 分组组件。
    
    为 Cell 提供上下外边框，可用于对单元格进行分组。
    """

    tag = "Cell.Group"

    # 分组标题
    title: Var[Optional[str]] = None

    # 是否显示外边框
    border: Var[Optional[bool]] = True

    # 是否展示为圆角卡片风格
    inset: Var[Optional[bool]] = None

    # 是否展示卡片类型
    card: Var[Optional[bool]] = None

    style: dict = {'width': '100%'}

# 按照官方示例的方式定义工厂函数
cell = Cell.create
cell_group = CellGroup.create


__all__ = ["Cell", "CellGroup", "cell", "cell_group"]