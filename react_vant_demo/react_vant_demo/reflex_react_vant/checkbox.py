import reflex as rx
from reflex import Var
from typing import Optional, Any, List, Dict, Callable, Union
from .base import ReactVantBase  # 你已有的基础封装父类

def _on_change_spec(value: bool) -> list[Var]:
    return [value]

def _on_click_spec(event: dict) -> list[Var]:
    return [Var(f"{event}")]

def _on_group_change_spec(values: list) -> list[Var]:
    return [Var(f"{values}")]


# ✅ 单个 Checkbox
class Checkbox(ReactVantBase):
    tag = "Checkbox"

    # Props
    checked: Optional[bool] = False
    default_checked: Optional[bool] = False
    name: Optional[Any] = None
    shape: Optional[str] = "round"  # 'square' 或 'round'
    disabled: Optional[bool] = False
    label_disabled: Optional[bool] = False
    label_position: Optional[str] = "right"  # 'left' or 'right'
    icon_size: Optional[Union[int, str]] = "20px"
    checked_color: Optional[str] = "#3f45ff"
    bind_group: Optional[bool] = True

    # Events
    on_change: rx.EventHandler[_on_change_spec]
    on_click: rx.EventHandler[_on_click_spec]


# ✅ Checkbox 组
class CheckboxGroup(ReactVantBase):
    tag = "Checkbox.Group"

    value: Optional[List[Any]] = None
    default_checked: Optional[List[Any]] = None
    disabled: Optional[bool] = False
    max: Optional[Union[int, str]] = None
    direction: Optional[str] = "vertical"  # 'vertical' | 'horizontal'
    icon_size: Optional[Union[int, str]] = "20px"
    checked_color: Optional[str] = "#3f45ff"

    on_change: rx.EventHandler[_on_group_change_spec]


checkbox = Checkbox.create
checkbox_group = CheckboxGroup.create