import reflex as rx
from reflex import Var
from typing import Any, Optional, Union, Literal, List
from .base import ReactVantBase


# ---------------- 事件规格函数 ----------------

def _on_select_spec(value: str) -> list[Var]:
    return [
        rx.cond(
            Var(f"Array.isArray({value})"),
            Var(f"{value}.map(d => d.toISOString())"),
            Var(f"{value}.toISOString()"),
        )
    ]

def _on_confirm_spec(value: str) -> list[Var]:
    return _on_select_spec(value)

def _on_close_spec():
    return []

def _on_closed_spec():
    return []

def _on_unselect_spec(value: str) -> list[Var]:
    return _on_select_spec(value)

def _on_open_spec():
    return []

def _on_month_show_spec(e0: dict) -> list[Var]:
    return [
        Var(f"{{date: {e0}.date.toISOString(), title: {e0}.title}}")
    ]

def _on_over_range_spec():
    return []


# ---------------- 组件定义 ----------------

class Calendar(ReactVantBase):
    """ReactVant Calendar 日历组件"""

    tag = "Calendar"

    type: Optional[Literal["single", "multiple", "range"]] = None
    visible: Optional[bool] = None
    value: Optional[Union[List[str], str]] = None
    min_date: Optional[str] = None
    max_date: Optional[str] = None
    title: Optional[str] = None
    color: Optional[str] = None
    confirm_text: Optional[str] = None
    first_day_of_week: Optional[int] = None
    horizontal: Optional[bool] = None

    max_range:  Optional[int] = None
    range_prompt: Optional[str] = None
    show_range_prompt: bool = True
    allow_sameDay: bool = False

    # events
    on_select: rx.EventHandler[_on_select_spec]
    on_confirm: rx.EventHandler[_on_confirm_spec]
    on_close: rx.EventHandler[_on_close_spec]
    on_closed: rx.EventHandler[_on_closed_spec]
    on_unselect: rx.EventHandler[_on_unselect_spec]
    on_open: rx.EventHandler[_on_open_spec]
    on_month_show: rx.EventHandler[_on_month_show_spec]
    on_over_range: rx.EventHandler[_on_over_range_spec]

    @classmethod
    def create(cls, *children, **props):
        return super().create(*children, **props)


def calendar(**props):
    """工厂函数"""
    return Calendar.create(**props)
