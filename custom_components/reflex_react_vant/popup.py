import reflex as rx
from .base import ReactVantBase
from typing import Optional, Union, Literal, Any

# 定义事件规格函数
def _on_click_overlay_spec():
    return []

def _on_close_spec():
    return []

def _on_open_spec():
    return []

def _on_opened_spec():
    return []

def _on_closed_spec():
    return []


class Popup(ReactVantBase):
    """Popup 弹出层组件。"""
    
    # 组件名称
    tag = "Popup"
    
    # 是否显示弹出层
    visible: Optional[bool] = None
    
    # 弹出位置，可选值为 top、bottom、left、right
    position: Optional[Literal["top", "bottom", "left", "right", ""]] = None
    
    # 是否显示关闭图标
    closeable: Optional[bool] = None
    
    # 关闭图标名称或自定义图标，默认值为 cross
    close_icon: Optional[Union[str, rx.Component]] = None
    
    # 关闭图标位置，可选值为 top-left、top-right、bottom-left、bottom-right
    close_icon_position: Optional[Literal["top-left", "top-right", "bottom-left", "bottom-right"]] = None
    
    # 是否显示圆角
    round: Optional[bool] = None
    
    # 自定义弹出层内容
    content: Optional[str] = None
    
    # 是否点击遮罩层关闭
    close_on_click_overlay: Optional[bool] = None
    
    # 是否在点击遮罩层后立即关闭
    overlay_close_immediate: Optional[bool] = None
    
    # 是否显示遮罩层
    overlay: Optional[bool] = None
    
    # 遮罩层颜色
    overlay_style: Optional[dict] = None
    
    # 点击遮罩层时触发
    on_click_overlay: rx.EventHandler[_on_click_overlay_spec]
    
    # 关闭弹出层时触发
    on_close: rx.EventHandler[_on_close_spec]
    
    # 打开弹出层时触发
    on_open: rx.EventHandler[_on_open_spec]
    
    # 动画结束时触发
    on_opened: rx.EventHandler[_on_opened_spec]
    
    # 动画结束时触发
    on_closed: rx.EventHandler[_on_closed_spec]
    
    # 自定义动画
    transition: Optional[str] = None
    
    # 是否使用 z-index
    z_index: Optional[Union[str, int]] = None
    
    # 是否锁定背景滚动
    lock_scroll: Optional[bool] = None
    
    # 弹出层挂载的节点
    teleport: Optional[str] = None
    
    # 标题
    title: Optional[str] = None
    
    # 描述文字
    description: Optional[str] = None
    
    # 是否在显示时才渲染内容
    lazy_render: Optional[bool] = None
    
    @classmethod
    def create(cls, *children, **props):
        """创建Popup组件实例。"""
        return super().create(*children, **props)


def popup(*children, **props) -> rx.Component:
    """Popup 弹出层组件工厂函数。"""
    # 直接使用Popup.create方法，让组件自身处理visible状态
    return Popup.create(*children, **props)


__all__ = ["Popup", "popup"]