import reflex as rx
from .reflex_react_vant import  image, flex, flex_item, space


class ImageDemoState(rx.State):
    """Image 组件演示状态管理。"""
    pass


# 示例图片链接
SAMPLE_IMAGE_URL = "https://img.yzcdn.cn/vant/cat.jpeg"


def basic_image_demo() -> rx.Component:
    """基础用法演示。"""
    return rx.vstack(
        rx.heading("基础用法", size="5"),
        rx.text("基础用法与原生 img 标签一致，可以设置 src、width、height、alt 等原生属性"),
        rx.el.div(
            image(width="100", height="100", src=SAMPLE_IMAGE_URL),
            class_name="demo-image",
        ),
        width="100%",
    )


def image_fit_demo() -> rx.Component:
    """填充模式演示。"""
    fits = ['contain', 'cover', 'fill', 'none', 'scale-down']
    
    return rx.vstack(
        rx.heading("填充模式", size="5"),
        rx.text("通过 fit 属性可以设置图片填充模式"),
        rx.el.div(
            flex(
                [flex_item(
                    rx.vstack(
                        image(fit=fit_type, width="100%", height="27vw", src=SAMPLE_IMAGE_URL),
                        rx.text(fit_type),
                    ),
                span=8) for fit_type in fits],
                wrap="wrap", gutter=20
            ),
            class_name="demo-image",
        ),
        width="100%",
    )


def round_image_demo() -> rx.Component:
    """圆形图片演示。"""
    fits = ['contain', 'cover', 'fill', 'none', 'scale-down']
    
    return rx.vstack(
        rx.heading("圆形图片", size="5"),
        rx.text("通过 round 属性可以设置图片变圆"),
        rx.el.div(
            flex(
                [
                    flex_item( 
                        rx.vstack(
                            image(round=True, fit=fit_type, width="100%", height="27vw", src=SAMPLE_IMAGE_URL),
                            rx.text(fit_type),
                        ),
                        span=8)
                 for fit_type in fits]
                ,wrap="wrap", gutter=20),
            class_name="demo-image",
        ),
        width="100%",
    )


def loading_image_demo() -> rx.Component:
    """加载中提示演示。"""
    return rx.vstack(
        rx.heading("加载中提示", size="5"),
        rx.text("Image 组件提供了默认的加载中提示，支持通过 loadingIcon 自定义内容"),
        rx.el.div(
            flex(
                flex_item(rx.vstack(
                        image(width="100%", height="24vw"),  # 不设置src，展示加载中状态
                        rx.text("默认提示"),
                    ),span=8),
                flex_item(
                    rx.vstack(
                        image(
                            loading_icon=rx.el.div("加载中...", style={"fontSize": 14}),
                            width="100%",
                            height="24vw",
                        ),
                        rx.text("自定义提示"),
                    )
                    ,span=8),
                wrap="wrap", gutter=20),
            class_name="demo-image",
        ),
        width="100%",
    )


def error_image_demo() -> rx.Component:
    """加载失败提示演示。"""
    return rx.vstack(
        rx.heading("加载失败提示", size="5"),
        rx.text("Image 组件提供了默认的加载失败提示，支持通过 errorIcon 自定义内容"),
        rx.el.div(
            flex(
                flex_item(rx.vstack(
                        image(width="100%", height="24vw", src="x.jpg"),  # 无效的图片链接
                        rx.text("默认提示"),
                    ),span=8),
                flex_item(rx.vstack(
                        image(
                            width="100%",
                            height="24vw",
                            src="x.jpg",
                            error_icon=rx.el.div("加载失败", style={"fontSize": 14}),
                        ),
                        rx.text("自定义提示"),
                    ),span=8),
                wrap="wrap", gutter=20),
            class_name="demo-image",
        ),
        width="100%",
    )


def image_props_demo() -> rx.Component:
    """其他属性演示。"""
    return rx.vstack(
        rx.heading("其他属性", size="5"),
        rx.text("演示圆角、尺寸等其他属性"),
        space(rx.vstack(
                image(
                    src=SAMPLE_IMAGE_URL,
                    width="120",
                    height="120",
                    radius="10",
                ),
                rx.text("圆角图片"),
            ),
            rx.vstack(
                image(
                    src=SAMPLE_IMAGE_URL,
                    width="150",
                    height="100",
                    alt="示例图片",
                ),
                rx.text("指定宽高比"),
            ),
            rx.vstack(
                image(
                    src=SAMPLE_IMAGE_URL,
                    width="120",
                    height="120",
                    lazyload=True,
                ),
                rx.text("懒加载图片"),
            ),gap=20),
        width="100%",
    )


def image_page() -> rx.Component:
    """Image 组件演示页面。"""
    return rx.vstack(
        rx.heading("Image Demo", size="6"),
        rx.text("Reflex wrapper for the React-Vant UI library - Image 组件"),
        
        basic_image_demo(),
        image_fit_demo(),
        round_image_demo(),
        loading_image_demo(),
        error_image_demo(),
        image_props_demo(),
        
        spacing="6",
        padding="2em",
        align="stretch",
        max_width="800px",
        style={"backgroundColor": "#f5f5f5"},
    )