from typing import Optional, Union, List, Dict, Any
from reflex.vars import Var
import reflex as rx
from .base import ReactVantBase

# 定义Action数据结构
def _on_select_spec(action: Dict[str, Any], index: int) -> list[Var]:
    return [rx.Var(f"{action}"), rx.Var(f"{index}")]

def _on_cancel_spec() -> list[Var]:
    return []

def _on_open_spec() -> list[Var]:
    return []

def _on_close_spec() -> list[Var]:
    return []

def _on_opened_spec() -> list[Var]:
    return []

def _on_closed_spec() -> list[Var]:
    return []

def _on_click_overlay_spec(event: Any) -> list[Var]:
    return [rx.Var(f"{event}")]

class ActionSheet(ReactVantBase):
    """
    ActionSheet 动作面板组件
    底部弹起的模态面板，包含与当前情境相关的多个选项。
    """
    tag = "ActionSheet"
    _library = "react-vant"
    _component = "ActionSheet"
    
    # 是否显示动作面板
    visible: Var[bool] = False
    
    # 面板选项列表
    actions: List[Dict[str, Any]] = []
    
    # 顶部标题
    title: Var[Optional[str]] = None
    
    # 取消按钮文字
    cancel_text: Var[Optional[str]] = None
    
    # 选项上方的描述信息
    description: Var[Optional[str]] = None
    
    # 是否显示关闭图标
    closeable: Var[bool] = True
    
    # 自定义关闭图标
    close_icon: Var[Optional[Any]] = None
    
    # 动画时长，单位毫秒
    duration: Var[Union[float, str]] = 300
    
    # 是否显示圆角
    round: Var[bool] = True
    
    # 是否显示遮罩层
    overlay: Var[bool] = True
    
    # 自定义遮罩层类名
    overlay_class: Var[Optional[str]] = None
    
    # 自定义遮罩层样式
    overlay_style: Var[Optional[Dict[str, Any]]] = None
    
    # 是否锁定背景滚动
    lock_scroll: Var[bool] = True
    
    # 是否在页面回退时自动关闭
    close_on_popstate: Var[bool] = False
    
    # 是否在点击选项后关闭
    close_on_click_action: Var[bool] = False
    
    # 是否在点击遮罩层后关闭
    close_on_click_overlay: Var[bool] = True
    
    # 是否开启底部安全区适配
    safe_area_inset_bottom: Var[bool] = True
    
    # 点击选项时触发，禁用或加载状态下不会触发
    on_select: rx.EventHandler[_on_select_spec]
    
    # 点击取消按钮时触发
    on_cancel: rx.EventHandler[_on_cancel_spec]
    
    # 打开面板时触发
    on_open: rx.EventHandler[_on_open_spec]
    
    # 关闭面板时触发
    on_close: rx.EventHandler[_on_close_spec]
    
    # 打开面板且动画结束后触发
    on_opened: rx.EventHandler[_on_opened_spec]
    
    # 关闭面板且动画结束后触发
    on_closed: rx.EventHandler[_on_closed_spec]
    
    # 点击遮罩层时触发
    on_click_overlay: rx.EventHandler[_on_click_overlay_spec]

# 按照官方示例的方式定义工厂函数
action_sheet = ActionSheet.create

__all__ = ["ActionSheet", "action_sheet"]