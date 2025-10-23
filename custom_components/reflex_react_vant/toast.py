import reflex as rx
from .base import ReactVantBase
from typing import Optional, Union, Literal, Any, Dict

# 定义事件规格函数
def _on_close_spec():
    return []

# 定义Toast配置类型
class ToastConfig:
    """Toast配置类型。"""
    
    def __init__(self):
        pass


class Toast(ReactVantBase):
    """Toast 轻提示组件。"""
    
    # 组件名称
    tag = "Toast"
    
    # 提示信息
    message: Optional[str] = None
    
    # 图标名称或自定义图标
    icon: Optional[Union[str, rx.Component]] = None
    
    # 加载图标类型，可选值为 spinner
    loading_type: Optional[Literal["spinner"]] = None
    
    # 提示类型，可选值为 info、success、fail、loading
    type: Optional[Literal["info", "success", "fail", "loading"]] = None
    
    # 动画时长，单位为毫秒
    duration: Optional[int] = None
    
    # 提示显示位置，可选值为 top、middle、bottom
    position: Optional[Literal["top", "middle", "bottom"]] = None
    
    # 是否禁止背景点击
    forbid_click: Optional[bool] = None
    
    # 是否显示背景遮罩
    overlay: Optional[bool] = None
    
    # 遮罩层颜色
    overlay_style: Optional[dict] = None
    
    # 关闭时的回调函数
    on_close: rx.EventHandler[_on_close_spec]
    
    # 点击事件回调
    onClick: Optional[rx.EventHandler[_on_close_spec]] = None
    
    @classmethod
    def create(cls, *children, **props):
        """创建Toast组件实例。"""
        return super().create(*children, **props)


# 工厂函数
def toast(
    message: Optional[str] = None,
    type: Optional[Literal["info", "success", "fail", "loading"]] = None,
    icon: Optional[Union[str, rx.Component]] = None,
    duration: Optional[int] = None,
    position: Optional[Literal["top", "middle", "bottom"]] = None,
    forbid_click: Optional[bool] = None,
    overlay: Optional[bool] = None,
    overlay_style: Optional[dict] = None,
    on_close: Optional[rx.EventHandler] = None,
    **props
) -> rx.Component:
    """Toast 工厂函数，创建轻提示组件。"""
    return Toast.create(
        message=message,
        type=type,
        icon=icon,
        duration=duration,
        position=position,
        forbid_click=forbid_click,
        overlay=overlay,
        overlay_style=overlay_style,
        on_close=on_close,
        **props
    )


# 工具函数
def toast_info(message: Union[str, Dict], **kwargs) -> rx.Component:
    """显示文字提示。"""
    if isinstance(message, str):
        kwargs["message"] = message
        kwargs["type"] = "info"
    else:
        kwargs.update(message)
        kwargs["type"] = "info"
    return toast(**kwargs)


def toast_success(message: Union[str, Dict], **kwargs) -> rx.Component:
    """显示成功提示。"""
    if isinstance(message, str):
        kwargs["message"] = message
        kwargs["type"] = "success"
    else:
        kwargs.update(message)
        kwargs["type"] = "success"
    return toast(**kwargs)


def toast_fail(message: Union[str, Dict], **kwargs) -> rx.Component:
    """显示失败提示。"""
    if isinstance(message, str):
        kwargs["message"] = message
        kwargs["type"] = "fail"
    else:
        kwargs.update(message)
        kwargs["type"] = "fail"
    return toast(**kwargs)


def toast_loading(message: Union[str, Dict] = None, **kwargs) -> rx.Component:
    """显示加载提示。"""
    if isinstance(message, str):
        kwargs["message"] = message
        kwargs["type"] = "loading"
    elif isinstance(message, dict):
        kwargs.update(message)
        kwargs["type"] = "loading"
    else:
        kwargs["type"] = "loading"
    return toast(**kwargs)


def set_default_options(options: Dict) -> None:
    """全局修改 Toast 的默认配置。"""
    pass


def reset_default_options() -> None:
    """重置 Toast 的默认配置。"""
    pass


def allow_multiple(allow: bool) -> None:
    """是否允许同时存在多个 Toast。"""
    pass