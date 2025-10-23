import reflex as rx
from typing import Union
from react_vant_demo.reflex_react_vant import tabs, Tabs


class TabsState(rx.State):
    """Tabs组件状态管理"""
    active_key: Union[int, str] = 0
    
    def handle_change(self, key: Union[int, str]):
        """处理标签切换事件"""
        self.active_key = key
        return rx.toast.info(f"切换到标签: {key}")
    
    def handle_click(self, key: Union[int, str]):
        """处理标签点击事件"""
        return rx.toast.info(f"点击标签: {key}")
    
    def handle_disabled(self, key: Union[int, str]):
        """处理禁用标签点击事件"""
        return rx.toast.info(f"点击禁用标签: {key}")


def create_tab_pane(key, title, content=None, **props):
    """创建标签页面板"""
    return Tabs.TabPane.create(
        rx.text(content or f"内容 {key}", style={"padding": "20px", "textAlign": "center"}),
        title=title,
        name=key if props.get('use_name', False) else None,
        **{k: v for k, v in props.items() if k != 'use_name'}
    )


def basic_example() -> rx.Component:
    """基础用法示例"""
    return rx.card(
        rx.text("基础用法", size="4", style={"marginBottom": "16px"}),
        
        # 下划线风格
        rx.vstack(
            rx.text("下划线风格", size="3", style={"marginBottom": "8px"}),
            tabs(
                [create_tab_pane(i+1, f"标签{i+1}") for i in range(3)],
                default_active=2
            ),
            style={"marginBottom": "20px", 'width': '100%'}
        ),
        
        # 胶囊风格
        rx.vstack(
            rx.text("胶囊风格", size="3", style={"marginBottom": "8px"}),
            tabs(
                [create_tab_pane(i+1, f"标签{i+1}") for i in range(3)],
                type="capsule",
                border=True
            ),
            style={"marginBottom": "20px", 'width': '100%'}
        ),
        
        # 带描述信息展示
        rx.vstack(
            rx.text("带描述信息展示", size="3", style={"marginBottom": "8px"}),
            tabs(
                [
                    create_tab_pane(i+1, f"标签{i+1}", description="描述内容", badge=i+1)
                    for i in range(3)
                ],
                type="jumbo"
            ),
            style={"marginBottom": "20px", 'width': '100%'}
        ),
        
        # 卡片风格
        rx.vstack(
            rx.text("卡片风格", size="3", style={"marginBottom": "8px"}),
            tabs(
                [create_tab_pane(i+1, f"标签{i+1}") for i in range(3)],
                type="card"
            ),
            style={"marginBottom": "20px", 'width': '100%'}
        ),
        
        style={"padding": "16px", "marginBottom": "16px"}
    )


def name_matching_example() -> rx.Component:
    """通过名称匹配示例"""
    return rx.card(
        rx.text("通过名称匹配", size="4", style={"marginBottom": "16px"}),
        tabs(
            [
                create_tab_pane('a', "标签1", "内容 1", use_name=True),
                create_tab_pane('b', "标签2", "内容 2", use_name=True),
                create_tab_pane('c', "标签3", "内容 3", use_name=True)
            ],
            active='c'
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def scrollable_example() -> rx.Component:
    """标签栏滚动示例"""
    return rx.card(
        rx.text("标签栏滚动", size="4", style={"marginBottom": "16px"}),
        tabs(
            [create_tab_pane(i+1, f"标签{i+1}") for i in range(8)],
            swipeable=True
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def disabled_example() -> rx.Component:
    """禁用标签示例"""
    return rx.card(
        rx.text("禁用标签", size="4", style={"marginBottom": "16px"}),
        tabs(
            [
                create_tab_pane(1, "标签1"),
                create_tab_pane(2, "标签2", disabled=True),
                create_tab_pane(3, "标签3")
            ],
            active=1,
            on_disabled=True
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def align_example() -> rx.Component:
    """对齐方式示例"""
    return rx.card(
        rx.text("对齐方式", size="4", style={"marginBottom": "16px"}),
        tabs(
            [create_tab_pane(i+1, f"标签{i+1}") for i in range(3)],
            align="start"
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def sticky_example() -> rx.Component:
    """粘性布局示例"""
    return rx.card(
        rx.text("粘性布局", size="4", style={"marginBottom": "16px"}),
        tabs(
            [create_tab_pane(i+1, f"标签{i+1}") for i in range(4)],
            sticky=True,
            swipeable=True
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def scrollspy_example() -> rx.Component:
    """滚动导航示例"""
    return rx.card(
        rx.text("滚动导航", size="4", style={"marginBottom": "16px"}),
        tabs(
            [
                Tabs.TabPane.create(
                    rx.div(style={"height": "50vh", "display": "flex", "alignItems": "center", "justifyContent": "center"}, 
                          children=[rx.text(f"内容 {i+1}")]),
                    title=f"标签{i+1}"
                )
                for i in range(8)
            ],
            sticky=True,
            scrollspy={"autoFocusLast": True, "reachBottomThreshold": 50}
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def tabs_page() -> rx.Component:
    """Tabs标签页组件示例页面"""
    return rx.container(
        rx.vstack(
            rx.text("Tabs 标签页", size="5", weight="bold"),
            rx.text("选项卡切换组件，提供平级的区域将大块内容进行收纳和展现", size="3"),
            
            basic_example(),
            name_matching_example(),
            scrollable_example(),
            disabled_example(),
            align_example(),
            sticky_example(),
            # scrollspy_example(),  # 滚动导航示例可能需要特殊处理
            spacing="8",
            align_items="stretch",
            style={"padding": "20px 0", 'width': '100%'}
        )
    )