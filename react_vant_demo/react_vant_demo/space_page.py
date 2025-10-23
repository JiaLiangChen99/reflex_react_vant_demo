import reflex as rx
from .reflex_react_vant import space, button


class SpaceDemoState(rx.State):
    """Space 组件演示状态管理。"""
    pass


def basic_space_demo() -> rx.Component:
    """基础用法演示。"""
    return rx.vstack(
        rx.heading("基础用法", size="5"),
        rx.text("相邻组件水平间距"),
        space(
            rx.text("Space"),
            button("Button", type="primary"),
            button("Confirm"),
            align="center",
        ),
        width="100%",
    )


def divider_space_demo() -> rx.Component:
    """分隔符演示。"""
    return rx.vstack(
        rx.heading("分隔符", size="5"),
        rx.text("相邻组件分隔符"),
        space(
            rx.link("Info", href="#"),
            rx.link("Edit", href="#"),
            rx.link("Delete", href="#"),
            align="center",
            divider=rx.divider(type="vertical"),
        ),
        width="100%",
    )


def vertical_space_demo() -> rx.Component:
    """垂直间距演示。"""
    return rx.vstack(
        rx.heading("垂直间距", size="5"),
        rx.text("相邻组件垂直间距，可以设置 width: 100% 独占一行"),
        space(
            button("Button 1", type="primary"),
            button("Button 2"),
            direction="vertical",
        ),
        width="100%",
    )


def gap_space_demo() -> rx.Component:
    """间距大小演示。"""
    return rx.vstack(
        rx.heading("间距大小", size="5"),
        rx.text("通过 gap 属性可以调整间距大小"),
        rx.vstack(
            space(
                button("Button"),
                button("Button"),
                gap=8,
            ),
            space(
                button("Button"),
                button("Button"),
                gap=20,
            ),
            space(
                button("Button"),
                button("Button"),
                gap=[8, 20],
            ),
            spacing="2",
        ),
        width="100%",
    )


def align_space_demo() -> rx.Component:
    """对齐方式演示。"""
    # 创建一个带边框的子组件
    def child(content: str) -> rx.Component:
        return rx.el.div(
            content,
            padding="15px",
            border="1px solid #eee",
            border_radius="4px",
        )
    
    return rx.vstack(
        rx.heading("对齐设置", size="5"),
        rx.text("通过 justify 和 align 属性可以调整对齐方式"),
        
        # 主轴对齐
        rx.vstack(
            rx.text("主轴对齐 - center"),
            space(
                rx.text("1"),
                rx.text("2\n2"),
                rx.text("3\n3\n3"),
                justify="center",
                block=True,
            ),
            spacing="1",
        ),
        
        # 交叉轴对齐
        rx.vstack(
            rx.text("交叉轴对齐 - end"),
            space(
                rx.text("1"),
                rx.text("2\n2"),
                rx.text("3\n3\n3"),
                align="end",
            ),
            spacing="1",
        ),
        
        width="100%",
    )


def wrap_space_demo() -> rx.Component:
    """自动换行演示。"""
    return rx.vstack(
        rx.heading("自动换行", size="5"),
        rx.text("设置 wrap 属性实现自动换行"),
        space(
            button("Button"),
            button("Button"),
            button("Button"),
            button("Button"),
            button("Button"),
            button("Button"),
            wrap=True,
            gap=[8, 20],
        ),
        width="100%",
    )


def space_page() -> rx.Component:
    """Space 组件演示页面。"""
    return rx.vstack(
        rx.heading("Space Demo", size="6"),
        rx.text("Reflex wrapper for the React-Vant UI library - Space 组件"),
        
        basic_space_demo(),
        divider_space_demo(),
        vertical_space_demo(),
        gap_space_demo(),
        align_space_demo(),
        wrap_space_demo(),
        
        spacing="6",
        padding="2em",
        align="stretch",
        max_width="800px",
    )