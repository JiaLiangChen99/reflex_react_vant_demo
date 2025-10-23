import reflex as rx
from .reflex_react_vant import flex, flex_item


class FlexDemoState(rx.State):
    """Flex组件演示的状态管理。"""
    pass


def basic_flex_demo():
    """基础用法演示。"""
    return rx.card(
        rx.heading("基础用法", size="1", mb="2"),
        rx.text("Flex 组件提供了24列栅格系统", mb="4"),
        flex(
            flex_item(rx.text("span: 12"), span=12),
            flex_item(rx.text("span: 12"), span=12),
            className="mb-4",
            bg="#f5f5f5",
            p="4"
        ),
        flex(
            flex_item(rx.text("span: 8"), span=8),
            flex_item(rx.text("span: 8"), span=8),
            flex_item(rx.text("span: 8"), span=8),
            bg="#f5f5f5",
            p="4"
        ),
    )


def gutter_flex_demo():
    """区域间隔演示。"""
    return rx.card(
        rx.heading("区域间隔", size="1", mb="2"),
        rx.text("通过gutter属性可以设置列元素之间的间距", mb="4"),
        flex(
            flex_item(rx.text("span: 8"), span=8, bg="#f5f5f5", p="4"),
            flex_item(rx.text("span: 8"), span=8, bg="#f5f5f5", p="4") ,
            flex_item(rx.text("span: 8"), span=8, bg="#f5f5f5", p="4") ,
            flex_item(rx.text("span: 8"), span=8, bg="#f5f5f5", p="4") ,
            flex_item(rx.text("span: 8"), span=8, bg="#f5f5f5", p="4") ,
            flex_item(rx.text("span: 8"), span=8, bg="#f5f5f5", p="4"),
            gutter=16,
            wrap="wrap",
            className="mb-4"
        ),
        rx.heading("垂直间距", size="1", mb="2"),
        rx.text("使用数组形式同时设置 [水平间距, 垂直间距]", mb="4"),
        flex(
            flex_item(rx.text("span: 8"), span=8, bg="#f5f5f5", p="4"),
            flex_item(rx.text("span: 8"), span=8, bg="#f5f5f5", p="4") ,
            flex_item(rx.text("span: 8"), span=8, bg="#f5f5f5", p="4") ,
            flex_item(rx.text("span: 8"), span=8, bg="#f5f5f5", p="4") ,
            flex_item(rx.text("span: 8"), span=8, bg="#f5f5f5", p="4") ,
            flex_item(rx.text("span: 8"), span=8, bg="#f5f5f5", p="4") ,
            gutter=[16, 24],
            wrap="wrap"
        ),
    )


def direction_flex_demo():
    """方向演示。"""
    return rx.card(
        rx.heading("方向设置", size="1", mb="2"),
        rx.text("通过direction属性设置弹性布局方向", mb="4"),
        rx.vstack(
            rx.text("默认方向: row", mb="2"),
            flex(
                flex_item(rx.text("span: 8-1"), span=8, p="2"),
                flex_item(rx.text("span: 8-2"), span=8, p="2"),
                flex_item(rx.text("span: 8-3"), span=8, p="2"),
                direction="row",
                bg="#f5f5f5",
                p="4",
                className="mb-4"
            ),
            rx.text("反向行: row-reverse", mb="2"),
            flex(
                flex_item(rx.text("span: 8-1"), span=8, p="2"),
                flex_item(rx.text("span: 8-2"), span=8, p="2"),
                flex_item(rx.text("span: 8-3"), span=8, p="2"),
                direction="row-reverse",
                bg="#f5f5f5",
                p="4",
                className="mb-4"
            ),
            rx.text("垂直方向: column", mb="2"),
            flex(
                flex_item(rx.text("item 1"), p="2"),
                flex_item(rx.text("item 2"), p="2"),
                flex_item(rx.text("item 3"), p="2"),
                direction="column",
                bg="#f5f5f5",
                p="4",
                className="mb-4"
            )
        )
    )


def align_flex_demo():
    """对齐方式演示。"""
    return rx.card(
        rx.heading("对齐方式", size="1", mb="2"),
        rx.text("设置垂直和水平对齐方式", mb="4"),
        rx.vstack(
            rx.text("居中对齐", mb="2"),
            flex(
                flex_item(rx.text("居中内容"), p="4", bg="#fff"),
                justify="center",
                align="center",
                bg="#f5f5f5",
                p="8",
                className="mb-4"
            ),
            rx.text("两端对齐", mb="2"),
            flex(
                flex_item(rx.text("左侧"), p="2"),
                flex_item(rx.text("右侧"), p="2"),
                justify="between",
                bg="#f5f5f5",
                p="4",
                className="mb-4"
            ),
            rx.text("底部对齐", mb="2"),
            flex(
                flex_item(rx.text("底部内容"), p="2"),
                align="end",
                bg="#f5f5f5",
                p="8",
                h="100px"
            )
        )
    )


def flex_page():
    """Flex组件演示页面。"""
    return rx.container(
        rx.heading("Flex 布局组件演示", size="2", mb="6"),
        rx.vstack(
            basic_flex_demo(),
            gutter_flex_demo(),
            direction_flex_demo(),
            align_flex_demo(),
            spacing="6",
            width="100%"
        )
    )