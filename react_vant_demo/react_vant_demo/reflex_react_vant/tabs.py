from typing import List, Union, Optional, Callable, Any, Dict
from reflex.vars import Var
from .base import ReactVantBase
import reflex as rx

def _on_change_spec(val: Union[int, str]):
    return [val]

def _on_click_spec():
    return []

class Tabs(ReactVantBase):
    """Tabs 标签页组件"""
    tag = "Tabs"
    
    # Props
    # 当前选中项的标识符
    active: Var[Optional[Union[int, str]]] = None
    
    # 默认选中项的标识符
    default_active: Var[Union[int, str]] = 0
    
    # 样式风格类型
    type: Var[str] = "line"  # line | card | capsule | jumbo
    
    # 标签栏对齐方式
    align: Var[str] = "center"  # start | center
    
    # 标签主题色
    color: Var[str] = "#ee0a24"
    
    # 标签栏背景色
    background: Var[str] = "white"
    
    # 动画时间，单位秒
    duration: Var[Union[float, str]] = "300ms"
    
    # type 为 line 时生效，底部条宽度
    line_width: Var[Union[int, str]] = "40px"
    
    # type 为 line 时生效，底部条高度
    line_height: Var[Union[int, str]] = "3px"
    
    # 是否开启切换动画
    animated: Var[bool] = True
    
    # 是否显示标签栏下划线
    border: Var[bool] = False
    
    # 是否显示标签栏背景
    show_background: Var[bool] = True
    
    # 是否在标签标题右侧显示小红点
    show_dot: Var[bool] = False
    
    # 是否禁用标签切换
    disabled: Var[bool] = False
    
    # 是否使用粘性布局
    sticky: Var[bool] = False
    
    # 是否可以滑动切换标签
    swipeable: Var[bool] = False
    
    # 滚动导航配置
    scrollspy: Var[Optional[Dict[str, Any]]] = None
    
    # 事件
    # 切换标签时触发
    on_change: rx.EventHandler[_on_change_spec]
    
    # 点击标签时触发
    on_click: rx.EventHandler[_on_click_spec]
    
    # 点击禁用标签时触发
    on_disabled: Optional[Callable[[Union[int, str]], None]] = None

    style: Var[Dict[str, Any]] = {'width': '100%'}

def tabs(*children, **props) -> Tabs:
    """创建标签页组件的工厂函数"""
    return Tabs.create(*children, **props)


class TabsTabPane(ReactVantBase):
    """标签页面板组件"""
    tag = "Tabs.TabPane"
    
    # 标签名称
    title: Var[Any] = None
    
    # 标签标识符
    name: Var[Optional[Union[int, str]]] = None
    
    # 标签描述信息，仅在 type="jumbo" 时生效
    description: Var[Optional[str]] = None
    
    # 是否禁用标签
    disabled: Var[bool] = False
    
    # 标签右上角徽标
    badge: Var[Optional[Union[int, str, bool]]] = None
    
    # 是否显示小红点
    dot: Var[bool] = False

    style: Var[Dict[str, Any]] = {'width': '100%'}

# 将TabsTabPane赋值给Tabs.TabPane
Tabs.TabPane = TabsTabPane


def tabs_tab_pane(*children, **props) -> TabsTabPane:
    """创建标签页面板组件的工厂函数"""
    return TabsTabPane.create(*children, **props)


__all__ = ["Tabs", "tabs", "TabsTabPane", "tabs_tab_pane"]
