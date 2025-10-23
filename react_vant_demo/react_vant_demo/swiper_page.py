from typing import List
import reflex as rx
from react_vant_demo.reflex_react_vant import Swiper, swiper, image


# 示例数据
images = [
    "https://img01.yzcdn.cn/vant/apple-1.jpg",
    "https://img01.yzcdn.cn/vant/apple-2.jpg",
    "https://img01.yzcdn.cn/vant/apple-3.jpg",
    "https://img01.yzcdn.cn/vant/apple-4.jpg",
]


def create_swiper_item(index: int):
    """创建轮播项"""
    return Swiper.Item.create(
        rx.el.div(
            rx.text(f"Slide {index + 1}", style={"color": "white", "textAlign": "center", "lineHeight": "150px"}),
            style={
                "backgroundColor": ["#ff4444", "#ff9900", "#2196f3", "#009688"][index % 4],
                "height": "150px",
                "borderRadius": "8px"
            }
        )
    )


class SwiperState(rx.State):
    """Swiper组件状态管理"""
    current_index: int = 0
    visible: bool = False
    
    def handle_change(self, index: int):
        """处理轮播变化事件"""
        self.current_index = index
        
    def show_toast(self, index: int):
        """显示Toast提示当前索引"""
        self.current_index = index
        return rx.toast.info(f"当前索引: {index}")


def basic_example() -> rx.Component:
    """基础用法"""
    return rx.card(
        rx.text("基础用法", size="4", style={"marginBottom": "16px"}),
        swiper(
            [create_swiper_item(i) for i in range(4)],
            autoplay=5000,
            style={"height": "150px"}
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def lazyload_example() -> rx.Component:
    """懒加载示例"""
    return rx.card(
        rx.text("懒加载", size="4", style={"marginBottom": "16px"}),
        swiper(
            [
                Swiper.Item.create(
                    image(
                        src=img,
                        style={"width": "100%", "height": "150px", "objectFit": "cover", "borderRadius": "8px"}
                    )
                )
                for img in images
            ],
            style={"height": "150px"}
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def event_example() -> rx.Component:
    """监听onChange事件"""
    return rx.card(
        rx.text("监听onChange事件", size="4", style={"marginBottom": "16px"}),
        swiper(
            [create_swiper_item(i) for i in range(4)],
            on_change=SwiperState.show_toast,
            style={"height": "150px"}
        ),
        rx.text(f"当前索引: {SwiperState.current_index}", size="3", style={"marginTop": "12px"}),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def vertical_example() -> rx.Component:
    """纵向滚动"""
    return rx.card(
        rx.text("纵向滚动", size="4", style={"marginBottom": "16px"}),
        swiper(
            [create_swiper_item(i) for i in range(4)],
            autoplay=5000,
            vertical=True,
            style={"height": "150px"}
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def custom_size_example() -> rx.Component:
    """自定义滑块大小"""
    return rx.card(
        rx.text("自定义滑块大小", size="4", style={"marginBottom": "16px"}),
        swiper(
            [create_swiper_item(i) for i in range(4)],
            slide_size=80,
            style={"height": "150px"}
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def center_example() -> rx.Component:
    """滑块居中"""
    return rx.card(
        rx.text("滑块居中", size="4", style={"marginBottom": "16px"}),
        swiper(
            [create_swiper_item(i) for i in range(4)],
            slide_size=80,
            track_offset=10,
            style={"height": "150px"}
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def vertical_center_example() -> rx.Component:
    """垂直滑块居中"""
    return rx.card(
        rx.text("垂直滑块居中", size="4", style={"marginBottom": "16px"}),
        swiper(
            [create_swiper_item(i) for i in range(4)],
            vertical=True,
            slide_size=80,
            track_offset=10,
            style={"height": "150px"}
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def custom_indicator_example() -> rx.Component:
    """自定义指示器"""
    return rx.card(
        rx.text("自定义指示器", size="4", style={"marginBottom": "16px"}),
        swiper(
            [create_swiper_item(i) for i in range(4)],
            # 在实际实现中，这里需要特殊处理自定义指示器函数
            # 目前先用字符串模拟
            indicator="custom",
            style={"height": "150px"}
        ),
        style={"padding": "16px", "marginBottom": "16px"}
    )


def swiper_page() -> rx.Component:
    """Swiper轮播组件示例页面"""
    return rx.container(
        rx.vstack(
            rx.text("Swiper 轮播", size="5", weight="bold"),
            rx.text("用于循环播放一组图片或内容", size="3"),
            
            basic_example(),
            # lazyload_example(),
            # event_example(),
            # vertical_example(),
            # custom_size_example(),
            # center_example(),
            # vertical_center_example(),
            # custom_indicator_example(),
            
            spacing="8",
            align_items="stretch",
            style={"padding": "20px 0"}
        )
    )