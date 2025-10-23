import reflex as rx
from .reflex_react_vant import calendar, cell
from datetime import datetime

class CalendarState(rx.State):
    selected_date: str = ""

    first_calendar_visible: bool = False
    first_calendar_value: str = ""

    second_calendar_visible: bool = False
    second_calendar_date: list[str] = []

    third_calendar_visible: bool = False
    third_calendar_data: list[str] = []

    @rx.event
    def change_first_calendar_visible(self, visible: bool):
        self.first_calendar_visible = visible

    @rx.event
    def handle_confirm_first_calendar(self, value):
        if isinstance(value, list):
            self.first_calendar_value = ", ".join(value)
        else:
            self.first_calendar_value = value
        print("first_calendar_value", self.first_calendar_value)
        self.change_first_calendar_visible(False)

    @rx.event
    def change_second_calendar_visible(self, visible: bool):
        self.second_calendar_visible = visible
    
    @rx.event
    def handle_multify_select_calendar(self, value: list[str]):
        self.second_calendar_date = value
        self.second_calendar_visible = False

    @rx.event
    def change_third_calendar_visible(self, visible: bool):
        self.third_calendar_visible = visible
    
    @rx.event
    def handle_confirm_third_calendar(self, value: list[str]):
        self.third_calendar_data = value
        self.third_calendar_visible = False

    @rx.event
    def handle_confirm(self, value):
        if isinstance(value, list):
            self.selected_date = ", ".join(value)
        else:
            self.selected_date = value

def first_calander_example():
    return calendar(
                type="single",
                color="#1989fa",
                show_confirm=True,
                visible=CalendarState.first_calendar_visible,
                on_confirm=CalendarState.handle_confirm_first_calendar,
                on_select=CalendarState.handle_confirm_first_calendar,
            )

def second_calander_example():
    return calendar(
                type="multiple",
                color="#1989fa",
                show_confirm=True,
                visible=CalendarState.second_calendar_visible,
                on_confirm=CalendarState.handle_multify_select_calendar,
            )

def third_calander_example():
    return calendar(
                type="range",
                color="#1989fa",
                show_confirm=True,
                max_range=3,
                range_prompt="不能超过三天",
                visible=CalendarState.third_calendar_visible,
                on_confirm=CalendarState.handle_confirm_third_calendar,
                on_close=CalendarState.change_third_calendar_visible(False),
                horizontal=True
            )



def calandar_page():
    return rx.center(
        rx.vstack(
            rx.heading("ReactVant Calendar 示例"),
            first_calander_example(),
            cell(title="单个日期", icon=rx.icon(tag="map-marker"), on_click=CalendarState.change_first_calendar_visible(True)),
            rx.text("单日期选择结果", CalendarState.first_calendar_value),
            cell(title="多个日期", icon=rx.icon(tag="map-marker"), on_click=CalendarState.change_second_calendar_visible(True)),
            second_calander_example(),
            rx.vstack(rx.foreach(CalendarState.second_calendar_date, lambda date: rx.text(date))),
            cell(title="日期范围", icon=rx.icon(tag="map-marker"), on_click=CalendarState.change_third_calendar_visible(True)),
            third_calander_example(),
            rx.vstack(rx.foreach(CalendarState.third_calendar_data, lambda date: rx.text(date))),
            rx.text("当前选择日期: "),
            rx.text(rx.text(CalendarState.selected_date)),
            calendar(
                type="single",
                color="#1989fa",
                show_confirm=True,
                visible=False,
                on_confirm=CalendarState.handle_confirm,
                on_select=CalendarState.handle_confirm,
            ),
        ),
        padding="2em"
    )