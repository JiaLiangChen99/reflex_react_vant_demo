from reflex import Var
from .base import ReactVantBase
import reflex as rx


def _on_change_spec(date: str) -> list[rx.Var]:
    # 添加类型检查，确保能够处理不同类型的输入（特别是time类型的picker）
    # 如果不是Date对象，尝试转换或直接返回
    return [rx.Var(f"(typeof {date} === 'object' && {date} instanceof Date ? {date}.toISOString() : String({date}))")]

def _on_confirm_spec(date: str) -> list[rx.Var]:
    # 添加类型检查，确保能够处理不同类型的输入（特别是time类型的picker）
    # 如果不是Date对象，尝试转换或直接返回
    return [rx.Var(f"(typeof {date} === 'object' && {date} instanceof Date ? {date}.toISOString() : String({date}))")]

def _on_cancel_spec():
    return []


class DatetimePicker(ReactVantBase):
    """DatetimePicker 日期时间选择器组件"""

    library = "react-vant"
    tag = "DatetimePicker"

    # 基本属性 - 使用snake_case以符合Python习惯
    type: Var[str] = "datetime"
    title: Var[str] = ""
    confirm_button_text: Var[str] = "确认"
    cancel_button_text: Var[str] = "取消"
    show_toolbar: Var[bool] = True
    loading: Var[bool] = False
    read_only: Var[bool] = False
    filter: Var[str] = None

    formatter: Var[str] = None

    columns_order: Var[str] = None
    item_height: Var[float] = 44
    visible_item_count: Var[int] = 6
    swipe_duration: Var[int] = 1000
    columns_top: Var[str] = None
    columns_bottom: Var[str] = None
    option_render: Var[str] = None

    # timepicker为time的参数
    min_hour: Var[int] = 0
    max_hour: Var[int] = 23
    min_minute: Var[int] = 0
    max_minute: Var[int] = 59

    # 事件处理
    on_change: rx.EventHandler[_on_change_spec]
    on_confirm: rx.EventHandler[_on_confirm_spec]
    on_cancel: rx.EventHandler[_on_cancel_spec]

    def _get_props(self):
        # 从ReactVantBase获取基础属性
        props = super()._get_props()
        # 转换所有属性名从snake_case到camelCase
        camel_case_props = {}
        for key, value in props.items():
            # 跳过任何已经以camelCase格式存在的属性
            if value is None:
                continue
            if key == "on_change":
                camel_case_props["onChange"] = value
            elif key == "on_confirm":
                camel_case_props["onConfirm"] = value
            elif key == "on_cancel":
                camel_case_props["onCancel"] = value
            elif "_" in key:
                parts = key.split("_")
                camel_key = parts[0] + "".join(x.title() for x in parts[1:])
                camel_case_props[camel_key] = value
            else:
                camel_case_props[key] = value
        # 根据JavaScript源码，明确设置minDate和maxDate为Date对象
        # 与React Vant组件中的默认值保持一致
        # 这里还有bug，这里的强设置会导致minDate和maxDate固定十年了，函数中怎么定义都会没用
        camel_case_props["min_date"] = Var.create("new Date(new Date().getFullYear() - 10, 0, 1)", _var_is_local=True)
        camel_case_props["max_date"] = Var.create("new Date(new Date().getFullYear() + 10, 11, 31)", _var_is_local=True)
        return camel_case_props


# 注册组件
datetime_picker = DatetimePicker.create