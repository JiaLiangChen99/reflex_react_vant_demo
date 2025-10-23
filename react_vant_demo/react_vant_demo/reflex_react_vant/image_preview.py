from typing import Optional, Union, List, Dict, Any, Callable
from reflex.vars import Var
import reflex as rx
from .base import ReactVantBase


class ImagePreview(ReactVantBase):
    """
    ImagePreview组件用于图片预览，支持函数调用和组件调用两种方式。
    """
    # 组件的标签名称
    tag = "ImagePreview"
    
    # 是否显示预览
    visible: Var[Optional[bool]] = None
    
    # 需要预览的图片 URL 数组
    images: Var[Optional[List[str]]] = None
    
    # 图片预览起始位置索引
    start_position: Var[Union[int, str]] = "0"
    
    # 动画时长，单位为 ms
    swipe_duration: Var[Union[int, str]] = "300"
    
    # 是否显示页码
    show_index: Var[bool] = True
    
    # 是否显示轮播指示器
    show_indicators: Var[bool] = False
    
    # 是否在页面回退时自动关闭
    close_on_popstate: Var[bool] = True
    
    # 是否显示关闭图标
    closeable: Var[bool] = False
    
    # 关闭图标名称或图片链接
    close_icon: Var[str] = "clear"
    
    # 关闭图标位置，可选值为 top-left bottom-left bottom-right
    close_icon_position: Var[str] = "top-right"
    
    # 只允许点击关闭图标关闭
    close_only_click_close_icon: Var[bool] = False
    
    # 是否开启懒加载
    lazyload: Var[Union[bool, Dict[str, Any]]] = False
    
    # 自定义遮罩层样式
    overlay_style: Var[Optional[Dict[str, Any]]] = None
    
    # 指定挂载的节点
    teleport: Var[Optional[Any]] = None
    
    # 关闭时的回调函数
    on_close: rx.EventHandler[lambda e: []] = None
    
    # 完全关闭时的回调
    on_closed: rx.EventHandler[lambda e: []] = None
    
    # 切换图片时的回调函数，回调参数为当前索引
    on_change: rx.EventHandler[lambda index: [index]] = None
    
    # 关闭前的回调函数，返回 false 可阻止关闭，支持返回 Promise
    before_close: rx.EventHandler[lambda active: [active]] = None

    # 静态方法 - 函数调用方式
    @staticmethod
    def open(options: Dict[str, Any]) -> Any:
        """
        静态方法，用于函数调用方式打开图片预览
        :param options: 配置选项
        :return: 实例的销毁方法
        """
        # 在reflex中，我们需要通过特殊的方式实现静态方法的功能
        # 这里我们简单返回一个空的函数引用，实际的实现会在前端通过react-vant完成
        return lambda: None


# 按照官方示例的方式定义工厂函数
image_preview = ImagePreview.create

__all__ = ["ImagePreview", "image_preview"]