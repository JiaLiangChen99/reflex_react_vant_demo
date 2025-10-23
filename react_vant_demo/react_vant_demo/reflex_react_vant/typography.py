from typing import Optional, Union, List, Dict, Any
from reflex.components.component import Component
from reflex.vars import Var
from .base import ReactVantBase


# 定义EllipsisConfig类型
typing_EllipsisConfig = Dict[str, Union[Optional[int], Optional[str], Optional[callable]]]


class TypographyText(ReactVantBase):
    """Typography.Text 文本组件。
    
    用于展示文本内容，支持多种文本样式和文本省略配置。
    """

    tag = "Typography.Text"

    # 文本类型，可选值danger secondary light primary success warning
    type: Var[Optional[str]] = None

    # 文本大小，可选值xs sm md lg xl xxl
    size: Var[Optional[str]] = "md"

    # 禁用文本
    disabled: Var[Optional[bool]] = False

    # 文本省略，支持布尔值、数字或配置对象
    ellipsis: Var[Optional[Union[bool, int, typing_EllipsisConfig]]] = False

    # 添加删除线样式
    delete: Var[Optional[bool]] = False

    # 添加下划线样式
    underline: Var[Optional[bool]] = False

    # 文本居中
    center: Var[Optional[bool]] = False

    # 文本加粗
    strong: Var[Optional[bool]] = False


class TypographyTitle(ReactVantBase):
    """Typography.Title 标题组件。
    
    用于展示不同级别的标题文本。
    """

    tag = "Typography.Title"

    # 重要程度，可选值 1 2 3 4 5 6
    level: Var[Optional[int]] = 5

    # 文本居中
    center: Var[Optional[bool]] = False

    # 文本加粗
    strong: Var[Optional[bool]] = False

    # 文本大小，可选值xs sm md lg xl xxl
    size: Var[Optional[str]] = None


class TypographyLink(ReactVantBase):
    """Typography.Link 链接组件。
    
    用于展示可点击的链接文本。
    """

    tag = "Typography.Link"

    # 链接地址
    href: Var[Optional[str]] = None

    # 打开方式，可选值 _blank _self _parent _top
    target: Var[Optional[str]] = None

    # 链接类型，可选值danger secondary light primary success warning
    type: Var[Optional[str]] = None

    # 禁用链接
    disabled: Var[Optional[bool]] = False

    # 添加下划线样式
    underline: Var[Optional[bool]] = False

    # 文本大小，可选值xs sm md lg xl xxl
    size: Var[Optional[str]] = "md"


# 为了方便使用，创建一个Typography类作为命名空间
class Typography:
    Text = TypographyText
    Title = TypographyTitle
    Link = TypographyLink


# 按照官方示例的方式定义工厂函数
typography_text = TypographyText.create
typography_title = TypographyTitle.create
typography_link = TypographyLink.create


__all__ = [
    "Typography",
    "TypographyText",
    "TypographyTitle",
    "TypographyLink",
    "typography_text",
    "typography_title",
    "typography_link",
]