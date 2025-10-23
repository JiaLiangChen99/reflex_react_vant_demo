from typing import Optional, Union, List, Callable
from reflex.components.component import Component
from reflex.vars import Var
from .base import ReactVantBase
import reflex as rx


def _on_change_spec(val: str) -> list[Var]:
    return [rx.Var(f"{val}")]


def _on_submit_spec(val: str) -> list[Var]:
    return [rx.Var(f"{val}")]


def _on_focus_spec() -> list[Var]:
    return []


class PasswordInput(ReactVantBase):
    """PasswordInput 密码输入框组件。"""

    tag = "PasswordInput"

    # 值
    value: Var[Optional[str]] = None

    # 类型 默认为 text
    type: Var[Optional[str]] = "text"

    # 输入框下方文字提示
    info: Var[Optional[Union[str, Component]]] = None

    # 密码最大长度
    length: Var[Optional[Union[int, str]]] = 6

    # 输入框格子之间的间距，如 20px 2em，默认单位为px
    gutter: Var[Optional[Union[int, str]]] = 0

    # 自动聚焦
    auto_focus: Var[Optional[bool]] = False

    # 是否隐藏密码
    mask: Var[Optional[bool]] = True

    # 自定义规则, 这个规则并非单个输入框的
    validator: Var[Optional[str]] = None

    # 高亮样式(mask=true 时不生效)
    highlight_class: Var[Optional[str]] = None

    # 数据改变时触发
    on_change: rx.EventHandler[_on_change_spec]

    # 数据输满时触发
    on_submit: rx.EventHandler[_on_submit_spec]

    # 输入框聚焦时触发
    on_focus: rx.EventHandler[_on_focus_spec]

    style: Var[Optional[dict]] = {'width': '100%'}



# 按照官方示例的方式定义工厂函数
password_input = PasswordInput.create


__all__ = ["PasswordInput", "password_input"]