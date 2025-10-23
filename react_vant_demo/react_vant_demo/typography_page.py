import reflex as rx
from .reflex_react_vant import typography_text, typography_title, typography_link


class TypographyDemoState(rx.State):
    """Typography 组件演示状态管理。"""
    pass


# 用于文本省略演示的长文本内容
LONG_TEXT = "React Vant 是一套轻量、可靠的移动端 React 组件库，提供了丰富的基础组件和业务组件，帮助开发者快速搭建移动应用，使用过程中发现任何问题都可以提 Issue 给我们，当然，我们也非常欢迎你给我们发 PR。"


def basic_typography_demo() -> rx.Component:
    """基础用法演示。"""
    return rx.vstack(
        rx.heading("基础用法", size="5"),
        rx.text("展示不同类型和样式的文本"),
        typography_text(
            "In the process of ",
            typography_text("internal", type="danger"),
            " desktop applications development, ",
            typography_text("many different", type="primary"),
            " design specs and ",
            typography_text("implementations", underline=True),
            " would be ",
            typography_text("involved", type="warning"),
        ),
        width="100%",
    )


def ellipsis_demo() -> rx.Component:
    """文本省略演示。"""
    return rx.vstack(
        rx.heading("文本省略", size="5"),
        rx.text("使用 ellipsis 属性可以定制个性化的文本省略形式"),
        
        rx.vstack(
            rx.text("单行省略"),
            typography_text(LONG_TEXT, ellipsis=True, style={"width": "100%"}),
            
            rx.divider(my="4"),
            
            rx.text("多行省略 (2行)"),
            typography_text(LONG_TEXT, ellipsis=2, style={"width": "100%"}),
            
            rx.divider(my="4"),
            
            rx.text("带展开操作"),
            typography_text(
                LONG_TEXT,
                ellipsis={
                    "rows": 2,
                    "collapseText": "收起",
                    "expandText": "展开",
                },
                style={"width": "100%"},
            ),
            
            rx.divider(my="4"),
            
            rx.text("保留末位文本"),
            typography_text(
                LONG_TEXT,
                ellipsis={
                    "rows": 2,
                    "symbol": "......",
                    "suffixCount": 10,
                },
                style={"width": "100%"},
            ),
            
            rx.divider(my="4"),
            
            rx.text("自定义文本后缀"),
            typography_text(
                LONG_TEXT,
                ellipsis={
                    "rows": 2,
                    "suffixText": "--William",
                    "expandText": "更多",
                },
                style={"width": "100%"},
            ),
            
            spacing="3",
        ),
        width="100%",
    )


def title_demo() -> rx.Component:
    """标题演示。"""
    return rx.vstack(
        rx.heading("标题", size="5"),
        rx.text("展示不同级别的标题"),
        rx.vstack(
            typography_title("一级测试标题", level=1),
            typography_title("二级测试标题", level=2),
            typography_title("三级测试标题", level=3),
            typography_title("四级测试标题", level=4),
            typography_title("五级测试标题", level=5),
            typography_title("六级测试标题", level=6),            
            rx.text("居中标题"),
            typography_title("居中的标题", level=3, center=True),
            spacing="2",
        ),
        width="100%",
    )

def link_demo() -> rx.Component:
    """链接样式演示。"""
    return rx.vstack(
        rx.heading("链接样式", size="5"),
        rx.text("展示不同类型的链接样式"),        
        rx.vstack(
            typography_link("默认链接", href="#"),
            typography_link("主要链接", type="primary", href="#"),
            typography_link("危险链接", type="danger", href="#"),
            typography_link("禁用链接", disabled=True, href="#"),
            typography_link("无下划线链接", underline=False, href="#"),
            typography_link("外部链接", href="https://github.com/3lang3/react-vant", target="_blank"),
            spacing="2",
        ),
        width="100%",
    )


def typography_variant_demo() -> rx.Component:
    """文本变体演示。"""
    return rx.vstack(
        rx.heading("文本变体", size="5"),
        rx.text("展示不同的文本变体样式"),
        rx.hstack(
            typography_text("删除线", delete=True),
            typography_text("下划线", underline=True),
            typography_text("加粗", strong=True),
            typography_text("禁用", disabled=True),
            spacing="3",
            flex_wrap="wrap",
        ),
        rx.text("不同大小的文本"),
        rx.vstack(
            typography_text("极小文本", size="xs"),
            typography_text("小文本", size="sm"),
            typography_text("中文本", size="md"),
            typography_text("大文本", size="lg"),
            typography_text("超大文本", size="xl"),
            typography_text("特大文本", size="xxl"),
            spacing="1",
        ),
        width="100%",
    )


def color_demo() -> rx.Component:
    """颜色演示。"""
    return rx.vstack(
        rx.heading("文本颜色", size="5"),
        rx.text("展示不同颜色类型的文本"),
        rx.hstack(
            typography_text("默认", type="default"),
            typography_text("主要", type="primary"),
            typography_text("成功", type="success"),
            typography_text("警告", type="warning"),
            typography_text("危险", type="danger"),
            typography_text("次要", type="secondary"),
            typography_text("浅色", type="light"),
            spacing="2",
            flex_wrap="wrap",
        ),
        width="100%",
    )


def typography_page() -> rx.Component:
    """Typography 组件演示页面。"""
    return rx.vstack(
        rx.heading("Typography Demo", size="6"),
        rx.text("Reflex wrapper for the React-Vant UI library - Typography 组件"),
        basic_typography_demo(),
        ellipsis_demo(),
        title_demo(),
        link_demo(),
        typography_variant_demo(),
        color_demo(),
        spacing="6",
        padding="2em",
        align="stretch",
        max_width="800px",
    )