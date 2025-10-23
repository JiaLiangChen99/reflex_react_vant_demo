import reflex as rx
from .reflex_react_vant import password_input, button, cell, popup


class PasswordInputState(rx.State):
    # 基础密码状态
    basic_password: str = ""
    basic_submitted: bool = False
    basic_result: str = ""
    
    # 限制长度密码状态
    limited_password: str = ""
    limited_submitted: bool = False
    limited_result: str = ""
    
    # 格子间距密码状态
    gutter_password: str = ""
    gutter_submitted: bool = False
    gutter_result: str = ""
    
    # 明文展示密码状态
    visible_password: str = "123"
    visible_submitted: bool = False
    visible_result: str = ""
    
    # 只允许数字密码状态
    number_password: str = "12"
    number_submitted: bool = False
    number_result: str = ""
    
    # 自定义规则密码状态
    custom_rule_password: str = "123"
    custom_rule_submitted: bool = False
    custom_rule_result: str = ""
    
    # 提示信息密码状态
    info_password: str = ""
    info_submitted: bool = False
    info_result: str = ""
    
    # 重置所有状态
    def reset_all(self):
        self.basic_password = ""
        self.basic_submitted = False
        self.basic_result = ""
        self.limited_password = ""
        self.limited_submitted = False
        self.limited_result = ""
        self.gutter_password = ""
        self.gutter_submitted = False
        self.gutter_result = ""
        self.visible_password = "123"
        self.visible_submitted = False
        self.visible_result = ""
        self.number_password = "12"
        self.number_submitted = False
        self.number_result = ""
        self.custom_rule_password = "123"
        self.custom_rule_submitted = False
        self.custom_rule_result = ""
        self.info_password = ""
        self.info_submitted = False
        self.info_result = ""
    
    # 基础密码相关事件处理
    @rx.event
    def handle_basic_change(self, val: str):
        self.basic_password = val
    
    @rx.event
    def handle_basic_submit(self, val: str):
        self.basic_submitted = True
        self.basic_result = val
        return rx.toast.success(f"密码提交成功: {val}")
    
    # 限制长度密码相关事件处理
    @rx.event
    def handle_limited_change(self, val: str):
        self.limited_password = val
    
    @rx.event
    def handle_limited_submit(self, val: str):
        self.limited_submitted = True
        self.limited_result = val
        return rx.toast.success(f"4位密码提交成功: {val}")
    
    # 格子间距密码相关事件处理
    @rx.event
    def handle_gutter_change(self, val: str):
        self.gutter_password = val
    
    @rx.event
    def handle_gutter_submit(self, val: str):
        self.gutter_submitted = True
        self.gutter_result = val
        return rx.toast.success(f"带间距密码提交成功: {val}")
    
    # 明文展示密码相关事件处理
    @rx.event
    def handle_visible_change(self, val: str):
        self.visible_password = val
    
    @rx.event
    def handle_visible_submit(self, val: str):
        self.visible_submitted = True
        self.visible_result = val
        return rx.toast.success(f"明文密码提交成功: {val}")
    
    # 只允许数字密码相关事件处理
    @rx.event
    def handle_number_change(self, val: str):
        self.number_password = val
    
    @rx.event
    def handle_number_submit(self, val: str):
        self.number_submitted = True
        self.number_result = val
        return rx.toast.success(f"数字密码提交成功: {val}")
    
    # 自定义规则密码相关事件处理
    @rx.event
    def handle_custom_rule_change(self, val: str):
        self.custom_rule_password = val
    
    @rx.event
    def handle_custom_rule_submit(self, val: str):
        self.custom_rule_submitted = True
        self.custom_rule_result = val
        return rx.toast.success(f"自定义规则密码提交成功: {val}")
    
    # 提示信息密码相关事件处理
    @rx.event
    def handle_info_change(self, val: str):
        self.info_password = val
    
    @rx.event
    def handle_info_submit(self, val: str):
        self.info_submitted = True
        self.info_result = val
        return rx.toast.success(f"带提示信息密码提交成功: {val}")
    
    # 自定义验证规则函数
    def custom_validator(self, val: str) -> bool:
        # 只允许输入0-3的数字
        return True


def basic_example():
    """基础用法示例"""
    return rx.vstack(
        rx.text("基础用法"),
        password_input(
            on_change=PasswordInputState.handle_basic_change,
            on_submit=PasswordInputState.handle_basic_submit,
        ),
        rx.cond(
            PasswordInputState.basic_submitted,
            rx.text(f"提交结果: {PasswordInputState.basic_result}", color="green")
        ),
        style={"width": "100%"}
    )


def limited_length_example():
    """限制长度示例"""
    return rx.vstack(
        rx.text("限制长度 (4位)", size="4"),
        password_input(
            length=4,
            on_change=PasswordInputState.handle_limited_change,
            on_submit=PasswordInputState.handle_limited_submit
        ),
        rx.cond(
            PasswordInputState.limited_submitted,
            rx.text(f"提交结果: {PasswordInputState.limited_result}", color="green")
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def gutter_example():
    """格子间距示例"""
    return rx.vstack(
        rx.text("格子间距 (10px)", size="4"),
        password_input(
            gutter=10,
            on_change=PasswordInputState.handle_gutter_change,
            on_submit=PasswordInputState.handle_gutter_submit
        ),
        rx.cond(
            PasswordInputState.gutter_submitted,
            rx.text(f"提交结果: {PasswordInputState.gutter_result}", color="green")
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def visible_example():
    """明文展示示例"""
    return rx.vstack(
        rx.text("明文展示", size="4"),
        password_input(
            value=PasswordInputState.visible_password,
            mask=False,
            on_change=PasswordInputState.handle_visible_change,
            on_submit=PasswordInputState.handle_visible_submit
        ),
        rx.cond(
            PasswordInputState.visible_submitted,
            rx.text(f"提交结果: {PasswordInputState.visible_result}", color="green")
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def number_type_example():
    """只允许数字示例"""
    return rx.vstack(
        rx.text("只允许数字", size="4"),
        password_input(
            type="number",
            value=PasswordInputState.number_password,
            mask=False,
            length=4,
            on_change=PasswordInputState.handle_number_change,
            on_submit=PasswordInputState.handle_number_submit
        ),
        rx.cond(
            PasswordInputState.number_submitted,
            rx.text(f"提交结果: {PasswordInputState.number_result}", color="green")
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def custom_rule_example():
    """自定义规则示例"""
    return rx.vstack(
        rx.text("自定义规则 (只允许输入0-3的数字)", size="4"),
        password_input(
            value=PasswordInputState.custom_rule_password,
            mask=False,
            length=4,
            validator="(val) => /^[0-3]{0,4}$/.test(val)",
            on_change=PasswordInputState.handle_custom_rule_change,
            on_submit=PasswordInputState.handle_custom_rule_submit
        ),
        rx.cond(
            PasswordInputState.custom_rule_submitted,
            rx.text(f"提交结果: {PasswordInputState.custom_rule_result}", color="green")
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def auto_focus_example():
    """自动聚焦示例"""
    return rx.vstack(
        rx.text("自动聚焦", size="4"),
        password_input(
            length=4,
            auto_focus=True,
            on_change=lambda val: rx.toast.info(f"自动聚焦输入: {val}"),
            on_submit=lambda val: rx.toast.success(f"自动聚焦提交: {val}")
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def info_example():
    """提示信息示例"""
    return rx.vstack(
        rx.text("提示信息", size="4"),
        password_input(
            info="密码为6位数字",
            on_change=PasswordInputState.handle_info_change,
            on_submit=PasswordInputState.handle_info_submit
        ),
        rx.cond(
            PasswordInputState.info_submitted,
            rx.text(f"提交结果: {PasswordInputState.info_result}", color="green")
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def password_input_page():
    """密码输入框演示页面"""
    return rx.center(
        rx.vstack(
            rx.heading("ReactVant PasswordInput 示例"),
            
            basic_example(),
            limited_length_example(),
            gutter_example(),
            visible_example(),
            number_type_example(),
            custom_rule_example(),
            auto_focus_example(),
            info_example(),
            
            button(
                "重置所有示例",
                on_click=PasswordInputState.reset_all,
                style={"margin_top": "20px"}
            ),
            
            style={"width": "100%", "max_width": "500px", "padding": "20px"}
        ),
        style={"min_height": "100vh", "padding": "2em"}
    )


__all__ = ["password_input_page"]