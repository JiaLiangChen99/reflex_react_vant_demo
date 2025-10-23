from turtle import onclick
import reflex as rx
from .reflex_react_vant import number_keyboard, cell, button


class NumberKeyboardState(rx.State):
    # 基本示例状态
    basic_keyboard_visible: bool = False
    basic_value: str = ""
    
    # 安全键盘状态
    safe_keyboard_visible: bool = False
    safe_value: str = ""
    
    # 自定义主题状态
    custom_keyboard_visible: bool = False
    custom_value: str = ""
    
    # 带小数点状态
    decimal_keyboard_visible: bool = False
    decimal_value: str = ""
    
    # 最大长度限制状态
    max_length_keyboard_visible: bool = False
    max_length_value: str = ""
    
    # 基本键盘相关事件处理
    @rx.event()
    def show_basic_keyboard(self, visible: bool = True):
        self.basic_keyboard_visible = visible
    
    @rx.event
    def handle_basic_input(self, key: str | int):
        self.basic_value += str(key)
        return rx.toast.success(f"输入: {key}")
    
    @rx.event
    def handle_basic_delete(self):
        if self.basic_value:
            self.basic_value = self.basic_value[:-1]
    
    @rx.event
    def handle_basic_close(self):
        self.basic_keyboard_visible = False
    
    # 安全键盘相关事件处理
    @rx.event()
    def show_safe_keyboard(self, visible: bool = True):
        print("右侧栏键盘出发", visible)
        self.safe_keyboard_visible = visible
    
    @rx.event
    def handle_safe_input(self, key: str | int):
        self.safe_value += str(key)
    
    @rx.event
    def handle_safe_delete(self):
        if self.safe_value:
            self.safe_value = self.safe_value[:-1]
    
    @rx.event
    def handle_safe_close(self):
        self.safe_keyboard_visible = False
    
    # 自定义主题键盘相关事件处理
    @rx.event
    def show_custom_keyboard(self, visible: bool = True):
        self.custom_keyboard_visible = visible
    
    @rx.event
    def handle_custom_input(self, key: str):
        self.custom_value += key
    
    @rx.event
    def handle_custom_delete(self):
        if self.custom_value:
            self.custom_value = self.custom_value[:-1]
    
    @rx.event
    def handle_custom_close(self):
        self.custom_keyboard_visible = False
    
    # 带小数点键盘相关事件处理
    @rx.event
    def show_decimal_keyboard(self, visible: bool = True):
        self.decimal_keyboard_visible = visible
    
    @rx.event
    def handle_decimal_input(self, key: str):
        # 处理小数点输入逻辑
        if key == '.':
            if '.' not in self.decimal_value:
                if not self.decimal_value:
                    self.decimal_value = '0.'
                else:
                    self.decimal_value += '.'
        else:
            self.decimal_value += key
    
    @rx.event
    def handle_decimal_delete(self):
        if self.decimal_value:
            self.decimal_value = self.decimal_value[:-1]
    
    @rx.event
    def handle_decimal_close(self):
        self.decimal_keyboard_visible = False
    
    # 最大长度限制键盘相关事件处理
    @rx.event
    def show_max_length_keyboard(self, visible: bool = True):
        self.max_length_keyboard_visible = visible
    
    @rx.event
    def handle_max_length_input(self, key: str):
        if len(self.max_length_value) < 6:  # 最大长度为6
            self.max_length_value += key
    
    @rx.event
    def handle_max_length_delete(self):
        if self.max_length_value:
            self.max_length_value = self.max_length_value[:-1]
    
    @rx.event
    def handle_max_length_close(self):
        self.max_length_keyboard_visible = False


def basic_keyboard_example():
    """基本数字键盘示例"""
    return rx.vstack(
        rx.text("基本数字键盘示例"),
        rx.input(
            value=NumberKeyboardState.basic_value,
            placeholder="点击输入",
            on_focus=NumberKeyboardState.show_basic_keyboard(True),
            readonly=True,
            style={"margin_bottom": "10px"}
        ),
        number_keyboard(
            visible=NumberKeyboardState.basic_keyboard_visible,
            title="数字键盘",
            on_input=NumberKeyboardState.handle_basic_input,
            on_delete=NumberKeyboardState.handle_basic_delete,
            on_close=NumberKeyboardState.handle_basic_close,
            close_button_text="完成"
        ),
        style={"margin_bottom": "20px"}
    )


def safe_keyboard_example():
    """右侧栏键盘示例（随机顺序）"""
    return rx.vstack(
        rx.text("右侧栏键盘示例（随机顺序）"),
        rx.input(
            value=NumberKeyboardState.safe_value,
            placeholder="点击输入密码",
            style={"margin_bottom": "10px"}
        ),
        number_keyboard(
            visible=NumberKeyboardState.safe_keyboard_visible,
            theme='custom',
            extra_key='.',
            title="右侧栏键盘示例",
            random_key_order=True,
            on_input=NumberKeyboardState.handle_safe_input,
            on_delete=NumberKeyboardState.handle_safe_delete,
            on_close=NumberKeyboardState.handle_safe_close,
            close_button_text="完成"
        ),
        style={"margin_bottom": "20px"}
    )


def custom_theme_example():
    """自定义主题数字键盘示例"""
    return rx.vstack(
        rx.text("自定义主题数字键盘示例"),
        rx.text_input(
            value=NumberKeyboardState.custom_value,
            placeholder="点击输入",
            on_focus=NumberKeyboardState.show_custom_keyboard,
            readonly=True,
            style={"margin_bottom": "10px"}
        ),
        number_keyboard(
            show=NumberKeyboardState.custom_keyboard_visible,
            title="自定义主题键盘",
            theme="custom",
            on_input=NumberKeyboardState.handle_custom_input,
            on_delete=NumberKeyboardState.handle_custom_delete,
            on_close=NumberKeyboardState.handle_custom_close,
            close_button_text="完成"
        ),
        style={"margin_bottom": "20px"}
    )


def decimal_keyboard_example():
    """带小数点的数字键盘示例"""
    return rx.vstack(
        rx.text("带小数点的数字键盘示例"),
        rx.text_input(
            value=NumberKeyboardState.decimal_value,
            placeholder="点击输入金额",
            on_focus=NumberKeyboardState.show_decimal_keyboard,
            readonly=True,
            style={"margin_bottom": "10px"}
        ),
        number_keyboard(
            show=NumberKeyboardState.decimal_keyboard_visible,
            title="金额输入键盘",
            extra_key=".",
            on_input=NumberKeyboardState.handle_decimal_input,
            on_delete=NumberKeyboardState.handle_decimal_delete,
            on_close=NumberKeyboardState.handle_decimal_close,
            close_button_text="完成"
        ),
        style={"margin_bottom": "20px"}
    )


def max_length_keyboard_example():
    """限制最大长度的数字键盘示例"""
    return rx.vstack(
        rx.text("限制最大长度的数字键盘示例（最大6位）"),
        rx.text_input(
            value=NumberKeyboardState.max_length_value,
            placeholder="点击输入（最多6位）",
            on_focus=NumberKeyboardState.show_max_length_keyboard,
            readonly=True,
            style={"margin_bottom": "10px"}
        ),
        rx.text(f"当前长度：{len(NumberKeyboardState.max_length_value)}/6"),
        number_keyboard(
            show=NumberKeyboardState.max_length_keyboard_visible,
            title="限制长度键盘",
            on_input=NumberKeyboardState.handle_max_length_input,
            on_delete=NumberKeyboardState.handle_max_length_delete,
            on_close=NumberKeyboardState.handle_max_length_close,
            close_button_text="完成"
        ),
        style={"margin_bottom": "20px"}
    )


def number_keyboard_page():
    """数字键盘演示页面"""
    return rx.center(
        rx.vstack(
            rx.heading("ReactVant NumberKeyboard 示例"),
            rx.button(
                "基本数字键盘",
                color_scheme="grass",
                on_click=NumberKeyboardState.show_basic_keyboard(True),
            ),
            basic_keyboard_example(),
            rx.button(
                "右侧栏键盘键盘",
                on_click=NumberKeyboardState.show_safe_keyboard(True)
            ),
            safe_keyboard_example(),
            
            # rx.button(
            #     "自定义主题键盘",
            #     onclick=NumberKeyboardState.show_custom_keyboard
            # ),
            # # custom_theme_example(),
            
            # rx.button(
            #     "金额输入键盘",
            #     onclick=NumberKeyboardState.show_decimal_keyboard
            # ),
            # # decimal_keyboard_example(),
            
            # rx.button(
            #     "限制长度键盘",
            #     onclick=NumberKeyboardState.show_max_length_keyboard
            # ),
            # max_length_keyboard_example(),
            
            style={"width": "100%", "max_width": "500px"}
        ),
        padding="2em",
        style={"min_height": "100vh"}
    )

