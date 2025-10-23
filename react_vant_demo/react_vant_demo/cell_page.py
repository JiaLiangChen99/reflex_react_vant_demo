import reflex as rx
from .reflex_react_vant import cell, cell_group, button


class CellDemoState(rx.State):
    """Cell 组件演示状态管理。"""
    pass


def basic_cell_demo() -> rx.Component:
    """基础用法演示。"""
    return rx.vstack(
        rx.heading("基础用法", size="5"),
        rx.text("Cell 可以单独使用，也可以与 Cell.Group 搭配使用"),
        cell_group(
            cell(title="单元格", value="内容"),
            cell(title="单元格", value="内容", label="描述信息"),
        ),
        width="100%",
    )


def user_list_demo() -> rx.Component:
    """用户列表演示。"""
    return rx.vstack(
        rx.heading("用户列表", size="5"),
        rx.text("通过 icon 属性可以自定义左侧内容"),
        rx.vstack(
            *[cell(
                center=True,
                key=idx,
                title=f"Avatar {idx}",
                label="Deserunt dolor ea eaque eos",
                icon=rx.image(src="https://via.placeholder.com/44", width="44px", height="44px", rounded="full"),
                is_link=True
            ) for idx in range(4)],
            spacing="0",
            style={'width': '100%'}
        ),
        width="100%",
    )


def cell_size_demo() -> rx.Component:
    """单元格大小演示。"""
    return rx.vstack(
        rx.heading("单元格大小", size="5"),
        rx.text("通过 size 属性可以控制单元格的大小"),
        cell_group(
            cell(title="单元格", value="内容", size="large"),
            cell(title="单元格", value="内容", label="描述信息", size="large"),
        ),
        width="100%",
    )


def icon_cell_demo() -> rx.Component:
    """展示图标演示。"""
    return rx.vstack(
        rx.heading("展示图标", size="5"),
        rx.text("通过 icon 属性在标题左侧展示图标"),
        cell_group(
            cell(title="单元格", icon=rx.icon(tag="map-marker")),
            cell(title="单元格", icon=rx.icon(tag="fire")),
        ),
        width="100%",
    )


def only_value_demo() -> rx.Component:
    """只设置 value 演示。"""
    return rx.vstack(
        rx.heading("只设置 value", size="5"),
        rx.text("只设置 value 时，内容会靠左对齐"),
        cell_group(
            cell(value="内容"),
        ),
        width="100%",
    )


def arrow_demo() -> rx.Component:
    """展示箭头演示。"""
    return rx.vstack(
        rx.heading("展示箭头", size="5"),
        rx.text("设置 isLink 属性后会在单元格右侧显示箭头"),
        cell_group(
            cell(title="单元格", is_link=True),
            cell(title="单元格", is_link=True, value="内容"),
            cell(title="单元格", is_link=True, arrow_direction="down", value="内容"),
        ),
        width="100%",
    )


def group_title_demo() -> rx.Component:
    """分组标题演示。"""
    return rx.vstack(
        rx.heading("分组标题", size="5"),
        rx.text("通过 Cell.Group 的 title 属性可以指定分组标题"),
        rx.vstack(
            cell_group(
                cell(title="单元格", value="内容"),
                cell(title="单元格", value="内容"),
                title="分组1",
            ),
            cell_group(
                cell(title="单元格", value="内容"),
                cell(title="单元格", value="内容"),
                title="分组2",
            ),
            spacing="4",
            style={'width': '100%'}
        ),
        width="100%",
    )


def card_type_demo() -> rx.Component:
    """卡片类型演示。"""
    return rx.vstack(
        rx.heading("卡片类型", size="5"),
        rx.text("通过 Cell.Group 的 card 属性可以展示卡片类型"),
        cell_group(
            cell(title="单元格", value="内容"),
            cell(title="单元格", value="内容"),
            card=True,
        ),
        width="100%",
    )


def custom_content_demo() -> rx.Component:
    """自定义内容演示。"""
    return rx.vstack(
        rx.heading("自定义内容", size="5"),
        rx.text("自定义单元格内容"),
        cell_group(
            cell(
                rx.text("自定义内容"),
                title="单元格",
                icon=rx.icon(tag="shop"),
            ),
            cell(
                rx.el.div(
                    button("编辑", size="small"),
                    button("删除", size="small", type="danger"),
                    style={'width': '100%'}
                ),
                title="按钮组",
            ),
        ),
        width="100%",
    )


def center_demo() -> rx.Component:
    """垂直居中演示。"""
    return rx.vstack(
        rx.heading("垂直居中", size="5"),
        rx.text("通过 center 属性可以让 Cell 的左右内容都垂直居中"),
        cell_group(
            cell(center=True, title="单元格", value="内容", label="描述信息"),
        ),
        width="100%",
    )


def cell_page() -> rx.Component:
    """Cell 组件演示页面。"""
    return rx.vstack(
        rx.heading("Cell Demo", size="6"),
        rx.text("Reflex wrapper for the React-Vant UI library - Cell 组件"),
        
        basic_cell_demo(),
        user_list_demo(),
        cell_size_demo(),
        icon_cell_demo(),
        only_value_demo(),
        arrow_demo(),
        group_title_demo(),
        card_type_demo(),
        custom_content_demo(),
        center_demo(),
        
        spacing="6",
        padding="2em",
        align="stretch",
        max_width="800px",
    )