from typing import Optional
from pydantic.v1.errors import NoneIsAllowedError, NoneIsNotAllowedError
import reflex as rx
from .reflex_react_vant import cascader, cell, popup

# 示例数据
options = [
    {
        "text": "浙江省",
        "value": "330000",
        "children": [
            {"text": "杭州市", "value": "330100"},
            {"text": "宁波市", "value": "330200"},
        ],
    },
    {
        "text": "江苏省",
        "value": "320000",
        "children": [
            {"text": "南京市", "value": "320100"},
            {"text": "无锡市", "value": "320200"},
        ],
    },
]

class CascaderState(rx.State):
    value: list[str] = []
    selected: list[dict] = []
    show_cascader: bool = False

    @rx.event()
    def change_cascader_popup(self, open: bool = True):
        if open:
            self.show_cascader = True
        else:
            self.show_cascader = False

    def handle_change(self, data):
        """选中变化"""
        self.value = data["value"]
        self.selected = data["rows"]

    def handle_finish(self, data):
        """完成选择"""
        self.value = data["value"]
        self.selected = data["rows"]

    @rx.var
    def display_text(self) -> str:
        if not self.selected:
            return "未选择"
        return ", ".join([item.get("text", "") for item in self.selected])


def cascader_page():
    return rx.center(
        rx.vstack(
            rx.heading("ReactVant Cascader 示例", size="6"),
            cell(
                cell(
                    rx.text("自定义内容"),
                    title="单元格",
                    icon=rx.icon(tag="shop"),
                    on_click=CascaderState.change_cascader_popup(True),
                ),
            ),
            popup(
                cascader(
                    title=CascaderState.display_text,
                    options=options,
                    on_finish=CascaderState.handle_finish
                ),
                rx.button("确定", on_click=CascaderState.change_cascader_popup(False)),
                visible=CascaderState.show_cascader,
                position="bottom",
                round=True,
                closeable=True,
                on_close=CascaderState.change_cascader_popup(False),
            ),
            rx.text("当前选择:"),
            rx.text(rx.text(CascaderState.display_text)),
        ),
        padding="2em"
    )

