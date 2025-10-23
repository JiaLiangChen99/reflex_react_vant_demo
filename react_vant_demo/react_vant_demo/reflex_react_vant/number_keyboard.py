from typing import Optional, Union, List
from reflex.components.component import Component
from reflex.vars import Var
import reflex as rx
from .base import ReactVantBase


def _on_close_spec():
    return []

def _on_delete_spce():
    return []

def _on_input_spce(var: str) -> list[Var]:
    #  rx.Var(f"{{...{e0}, activeStartDate: {e0}.activeStartDate.toDateString()}}")
    # 参考上面，的函数，var传入的是一个整数数值，我需要转为字符串
    return [rx.Var(f"{var}")] 

def _on_blur_spec():
    return []

def _on_show_spec():
    return []

def _on_hide_spce():
    return []

class NumberKeyboard(ReactVantBase):
    """NumberKeyboard 数字键盘组件。"""

    tag = "NumberKeyboard"

    # 当前输入值
    value: Var[Optional[str]] = None

    # 是否显示键盘
    visible: Var[bool] = False

    # 键盘标题
    title: Var[Optional[Union[str, Component]]] = None

    # 删除按钮内容
    delete: Var[Optional[Union[str, Component]]] = None

    # 自定义数字按键内容
    number_key_render: Var[Optional[str]] = None

    # 自定义删除按键内容
    delete_render: Var[Optional[str]] = None

    # 自定义左下角按键内容
    # extra_key_render: Var[Optional[str]] = None

    # 样式风格，可选值为 custom
    theme: Var[str] = "default"

    # 输入值最大长度
    maxlength: Var[Optional[Union[int, str]]] = None

    # 是否开启过场动画
    transition: Var[Optional[bool]] = True

    # 键盘 z-index 层级
    z_index: Var[Optional[int]] = 100

    # 底部额外按键的内容
    extra_key: Var[str] = ""

    # 关闭按钮文字，空则不展示
    close_button_text: Var[str] = ''

    # 删除按钮文字，空则展示删除图标
    delete_button_text: Var[Optional[str]] = None

    # 是否将关闭按钮设置为加载中状态，仅在 theme="custom" 时有效
    close_button_loading: Var[Optional[bool]] = False

    # 是否展示删除图标
    show_delete_key: Var[Optional[bool]] = True

    # 是否在点击关闭按钮时触发 blur 事件
    blur_on_close: Var[Optional[bool]] = True

    # 是否在点击外部时收起键盘
    hide_on_click_outside: Var[Optional[bool]] = True

    # 是否开启底部安全区适配
    safe_area_inset_bottom: Var[Optional[bool]] = True

    # 是否将通过随机顺序展示按键
    random_key_order: Var[Optional[bool]] = False

    # 点击按键时触发
    on_input: rx.EventHandler[_on_input_spce]

    # 点击删除键时触发
    on_delete: rx.EventHandler[_on_delete_spce]

    # 点击关闭按钮时触发
    on_close: rx.EventHandler[_on_close_spec]

    # 点击关闭按钮或非键盘区域时触发
    on_blur: rx.EventHandler[_on_blur_spec]

    # 键盘完全弹出时触发
    on_show: rx.EventHandler[_on_show_spec]

    # 键盘完全收起时触发
    on_hide: rx.EventHandler[_on_hide_spce]


# 按照官方示例的方式定义工厂函数
number_keyboard = NumberKeyboard.create


__all__ = ["NumberKeyboard", "number_keyboard"]