import reflex as rx
from .reflex_react_vant import datetime_picker, popup


class DatetimePickerDemoState(rx.State):
    """日期时间选择器演示状态"""
    
    # 日期选择 - 使用更简洁的日期格式
    date_value: str = "2024-01-01"
    # 年月日时分
    datetime_value: str = "2024-01-01 12:00"
    # 年月
    year_month_value: str = "2024-01"
    # 月日
    month_day_value: str = "01-01"
    # 时间
    time_value: str = "12:00"
    # 日期小时
    datehour_value: str = "2024-01-01 12"
    
    # 弹出层日期
    popup_date_value: str = "2024-01-01"
    popup_visible: bool = False
    
    @rx.event()
    def handle_date_change(self, value: str):
        """处理日期选择变化"""
        self.date_value = value

    def handle_datetime_change(self, value: str):
        """处理日期时间选择变化"""
        self.datetime_value = value

    def handle_year_month_change(self, value: str):
        print(value)
        """处理年月选择变化"""
        self.year_month_value = value

    def handle_month_day_change(self, value: str):
        """处理月日选择变化"""
        self.month_day_value = value

    def handle_time_change(self, value: str):
        """处理时间选择变化"""
        self.time_value = value

    def handle_datehour_change(self, value: str):
        print("小时日期",value)
        """处理日期小时选择变化"""
        self.datehour_value = value

    def handle_popup_confirm(self, value: str):
        """处理弹出层确认"""
        self.popup_date_value = value
        self.popup_visible = False

    def handle_popup_cancel(self):
        """处理弹出层取消"""
        self.popup_visible = False

    @rx.event()
    def open_popup(self):
        """打开弹出层"""
        self.popup_visible = True

    def close_popup(self):
        """关闭弹出层"""
        self.popup_visible = False


def basic_date_picker():
    """基本日期选择器"""
    return rx.card(
        rx.text("选择年月日"),
        rx.text(DatetimePickerDemoState.date_value),
        datetime_picker(
            type="date",
            title="选择年月日",
            min_date="2020-01-01",
            max_date="2025-12-31",
            value=DatetimePickerDemoState.date_value,
            on_change=DatetimePickerDemoState.handle_date_change,
        ),
        padding="16px",
        margin_bottom="16px"
    )



def year_month_demo():
    """年月选择器"""
    return rx.card(
        rx.text("选择年月"),
        rx.text(DatetimePickerDemoState.year_month_value),
        datetime_picker(
            type="year-month",
            title="选择年月",
            value=DatetimePickerDemoState.year_month_value,
            on_change=DatetimePickerDemoState.handle_year_month_change,
            # 使用字符串表示formatter函数
            # formatter="(type, value) => type === 'year' ? value + '年' : value + '月'",
        ),
        padding="16px",
        margin_bottom="16px"
    )


def month_day_demo():
    """月日选择器"""
    return rx.card(
        rx.text("选择月日"),
        rx.text(DatetimePickerDemoState.month_day_value),
        datetime_picker(
            type="month-day",
            title="选择月日",
            value=DatetimePickerDemoState.month_day_value,
            on_change=DatetimePickerDemoState.handle_month_day_change,
        ),
        padding="16px",
        margin_bottom="16px"
    )


def time_picker_demo():
    """时间选择器"""
    return rx.card(
        rx.text("选择时间"),
        rx.text(DatetimePickerDemoState.time_value),
        datetime_picker(
            type="time",
            title="选择时间",
            min_hour=9,
            max_hour=18,
            value=DatetimePickerDemoState.time_value,
            on_change=DatetimePickerDemoState.handle_time_change,
        ),
        padding="16px",
        margin_bottom="16px"
    )


def datehour_demo():
    """日期小时选择器"""
    return rx.card(
        rx.text("选择日期和小时"),
        rx.text(DatetimePickerDemoState.datehour_value),
        datetime_picker(
            type="datehour",
            title="选择日期和小时",
            value=DatetimePickerDemoState.datehour_value,
            on_change=DatetimePickerDemoState.handle_datehour_change,
        ),
        padding="16px",
        margin_bottom="16px"
    )


def popup_demo():
    """弹出层模式日期选择器"""
    return rx.card(
        rx.text("弹出层模式"),
        rx.text(DatetimePickerDemoState.popup_date_value),
        rx.button(
            f"当前选择",
            on_click=DatetimePickerDemoState.open_popup,
            variant="surface",
            margin_bottom="12px"
        ),
        popup(
            datetime_picker(
                type="date",
                title="选择年月日",
                min_date="2020-01-01",
                max_date="2025-12-31",
                value=DatetimePickerDemoState.popup_date_value,
                on_confirm=DatetimePickerDemoState.handle_popup_confirm,
                on_cancel=DatetimePickerDemoState.handle_popup_cancel,
            ),
            visible=DatetimePickerDemoState.popup_visible,
            round=True,
            position="bottom",
            on_close=DatetimePickerDemoState.close_popup,
        ),
        padding="16px",
        margin_bottom="16px"
    )


def datetime_picker_page():
    """DatetimePicker演示页面"""
    return rx.container(
        rx.vstack(
            rx.heading("DatetimePicker 时间选择器", size="3"),
            basic_date_picker(),
            year_month_demo(),
            month_day_demo(),
            time_picker_demo(),
            datehour_demo(),
            popup_demo(),
            align="stretch",
            spacing="6",
            max_width="800px"
        ),
        padding="24px",
        center_content=True
    )