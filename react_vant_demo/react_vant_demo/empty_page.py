import reflex as rx
from typing import List, Dict, Any
from react_vant_demo.reflex_react_vant import empty, button


def basic_example():
    """基础用法示例"""
    return empty(
            description="描述文字"
        )

def image_type_example():
    """图片类型示例"""
    return rx.vstack(
            empty(
                image="error",
                description="错误状态"
            ),
            empty(
                image="network",
                description="网络错误"
            ),
            empty(
                image="search",
                description="搜索结果为空"
            ),
            style={"width": "100%"}
        )


def custom_image_example():
    """自定义图片示例"""
    return rx.vstack(
        empty(
            image_size=90,
            image="https://img.yzcdn.cn/vant/custom-empty-image.png",
            description="自定义图片示例",
            style={"className": "custom-image"}
        ),
    )

def bottom_content_example():
    """底部内容示例"""
    return empty(
            button("点击加载", style={"width": "160px"}, round=True, type="primary"),
            description="暂无数据",
        )

def custom_size_example():
    """自定义图片大小示例"""
    return rx.vstack(
        empty(
            image_size=60,
            description="小尺寸"
        ),
        empty(
            image_size=120,
            description="中尺寸"
        ),
        empty(
            image_size=180,
            description="大尺寸"
        )
    )

def empty_page():
    """Empty 组件示例页面"""
    return rx.container(
        rx.vstack(
            rx.heading("Empty 空状态", size="2"),
            rx.divider(),
            basic_example(),
            image_type_example(),
            custom_image_example(),
            bottom_content_example(),
            custom_size_example(),
            spacing="2",
            align_items="stretch",
            style={"max_width": "800px", "margin": "0 auto", "padding": "20px"}
        )
    )