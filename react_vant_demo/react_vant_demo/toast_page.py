# import reflex as rx
# from .reflex_react_vant import toast_info, toast_success, toast_fail, toast_loading, toast, cell, button, flex, flex_item


# class ToastDemoState(rx.State):
#     """Toast 组件演示状态管理。"""
    
#     # 允许多个Toast同时显示
#     allow_multiple: bool = False
    
#     # Toast显示状态
#     show_info_toast: bool = False
#     show_success_toast: bool = False
#     show_fail_toast: bool = False
#     show_loading_toast: bool = False
#     show_custom_icon_toast: bool = False
#     show_custom_loading_toast: bool = False
#     show_top_toast: bool = False
#     show_bottom_toast: bool = False
#     show_dynamic_toast: bool = False
#     show_first_toast: bool = False
#     show_second_toast: bool = False
    
#     @rx.event
#     async def toggle_multiple(self, value: bool):
#         """切换是否允许多个Toast同时显示。"""
#         self.allow_multiple = value
#         # 这里应该调用allow_multiple函数，但由于是客户端API，需要在前端处理
#         pass
    
#     @rx.event
#     async def show_info(self):
#         """显示信息提示。"""
#         self.show_info_toast = True
#         # 实际项目中，这里应该通过前端JavaScript调用Toast API
    
#     @rx.event
#     # async def show_success(self):
#         """显示成功提示。"""
#         self.show_success_toast = True
    
#     @rx.event
#     async def show_fail(self):
#         """显示失败提示。"""
#         self.show_fail_toast = True
    
#     @rx.event
#     async def show_loading(self):
#         """显示加载提示。"""
#         self.show_loading_toast = True
    
#     @rx.event
#     async def show_custom_icon(self):
#         """显示自定义图标提示。"""
#         self.show_custom_icon_toast = True
    
#     @rx.event
#     async def show_custom_loading(self):
#         """显示自定义加载图标提示。"""
#         self.show_custom_loading_toast = True
    
#     @rx.event
#     async def show_top(self):
#         """显示顶部提示。"""
#         self.show_top_toast = True
    
#     @rx.event
#     async def show_bottom(self):
#         """显示底部提示。"""
#         self.show_bottom_toast = True
    
#     @rx.event
#     async def show_dynamic(self):
#         """显示动态更新的Toast。"""
#         self.show_dynamic_toast = True
    
#     @rx.event
#     async def show_first(self):
#         """显示第一个Toast。"""
#         self.show_first_toast = True
    
#     @rx.event
#     async def show_second(self):
#         """显示第二个Toast。"""
#         self.show_second_toast = True


# def basic_toast_demo() -> rx.Component:
#     """基础用法演示。"""
#     return rx.vstack(
#         rx.heading("基础用法", size="5"),
#         rx.text("通过不同方法显示不同类型的提示") ,
#         rx.el.div(
#             flex(
#                 flex_item(cell(title="文字提示", is_link=True, on_click=ToastDemoState.show_info)),
#                 flex_item(cell(title="成功提示", is_link=True, on_click=ToastDemoState.show_success)),
#                 justify="space-around",
#                 margin_bottom="1em"
#             ),
#             flex(
#                 flex_item(cell(title="失败提示", is_link=True, on_click=ToastDemoState.show_fail)),
#                 flex_item(cell(title="加载提示", is_link=True, on_click=ToastDemoState.show_loading)),
#                 justify="space-around"
#             ),
#             # 信息提示Toast
#             toast(
#                 message="提示内容",
#                 type="info",
#                 visible=ToastDemoState.show_info_toast,
#                 # on_close=rx.set_value(ToastDemoState, "show_info_toast", False)
#             ),
#             # 成功提示Toast
#             toast(
#                 message="成功文案",
#                 type="success",
#                 visible=ToastDemoState.show_success_toast,
#                 # on_close=rx.set_value(ToastDemoState, "show_success_toast", False)
#             ),
#             # 失败提示Toast
#             toast(
#                 message="失败文案",
#                 type="fail",
#                 visible=ToastDemoState.show_fail_toast,
#                 # on_close=rx.set_value(ToastDemoState, "show_fail_toast", False)
#             ),
#             # 加载提示Toast
#             toast(
#                 message="加载中...",
#                 type="loading",
#                 forbid_click=True,
#                 visible=ToastDemoState.show_loading_toast,
#                 # on_close=rx.set_value(ToastDemoState, "show_loading_toast", False)
#             ),
#         ),
#         width="100%",
#         margin_bottom="2em"
#     )


# def custom_icon_toast_demo() -> rx.Component:
#     """自定义图标演示。"""
#     return rx.vstack(
#         rx.heading("自定义图标", size="5"),
#         rx.text("通过 icon 选项可以自定义图标，通过loadingType 属性可以自定义加载图标类型") ,
#         rx.el.div(
#             cell(title="自定义图标", is_link=True, on_click=ToastDemoState.show_custom_icon),
#             cell(title="自定义加载图标", is_link=True, on_click=ToastDemoState.show_custom_loading),
#             # 自定义图标Toast
#             toast(
#                 message="自定义图标",
#                 icon="fire",
#                 visible=ToastDemoState.show_custom_icon_toast,
#                 # on_close=rx.set_value(ToastDemoState, "show_custom_icon_toast", False)
#             ),
#             # 自定义加载图标Toast
#             toast(
#                 message="加载中...",
#                 type="loading",
#                 loading_type="spinner",
#                 forbid_click=True,
#                 visible=ToastDemoState.show_custom_loading_toast,
#                 # on_close=rx.set_value(ToastDemoState, "show_custom_loading_toast", False)
#             ),
#         ),
#         width="100%",
#         margin_bottom="2em"
#     )


# def custom_position_toast_demo() -> rx.Component:
#     """自定义位置演示。"""
#     return rx.vstack(
#         rx.heading("自定义位置", size="5"),
#         rx.text("Toast 默认渲染在屏幕正中位置，通过 position 属性可以控制 Toast 展示的位置") ,
#         rx.el.div(
#             flex(
#                 flex_item(cell(title="顶部展示", is_link=True, on_click=ToastDemoState.show_top)),
#                 flex_item(cell(title="底部展示", is_link=True, on_click=ToastDemoState.show_bottom)),
#                 justify="space-around"
#             ),
#             # 顶部位置Toast
#             toast(
#                 message="顶部展示",
#                 position="top",
#                 visible=ToastDemoState.show_top_toast,
#                 # on_close=rx.set_value(ToastDemoState, "show_top_toast", False)
#             ),
#             # 底部位置Toast
#             toast(
#                 message="底部展示",
#                 position="bottom",
#                 visible=ToastDemoState.show_bottom_toast,
#                 # on_close=rx.set_value(ToastDemoState, "show_bottom_toast", False)
#             ),
#         ),
#         width="100%",
#         margin_bottom="2em"
#     )


# def dynamic_toast_demo() -> rx.Component:
#     """动态更新演示。"""
#     return rx.vstack(
#         rx.heading("动态更新提示", size="5"),
#         rx.text("执行 Toast 方法时会返回对应的 Toast 实例，通过修改实例上的 message 属性可以实现动态更新提示的效果") ,
#         rx.el.div(
#             cell(title="动态更新提示", is_link=True, on_click=ToastDemoState.show_dynamic),
#             # 动态更新Toast示例（注意：实际的动态更新需要在前端JavaScript中处理）
#             toast(
#                 message="动态更新提示示例",
#                 visible=ToastDemoState.show_dynamic_toast,
#                 # on_close=rx.set_value(ToastDemoState, "show_dynamic_toast", False)
#             ),
#         ),
#         width="100%",
#         margin_bottom="2em"
#     )


# def multiple_toast_demo() -> rx.Component:
#     """多例模式演示。"""
#     return rx.vstack(
#         rx.heading("多例模式", size="5"),
#         rx.text("Toast 默认采用单例模式，即同一时间只会存在一个 Toast，如果需要在同一时间弹出多个 Toast，可以开启多例模式") ,
#         rx.el.div(
#             flex(
#                 flex_item(rx.text("开启多例模式")),
#                 flex_item(rx.switch(checked=ToastDemoState.allow_multiple, on_change=ToastDemoState.toggle_multiple)),
#                 align="center",
#                 margin_bottom="1em"
#             ),
#             flex(
#                 flex_item(cell(title="第一个Toast", is_link=True, on_click=ToastDemoState.show_first)),
#                 flex_item(cell(title="第二个Toast", is_link=True, on_click=ToastDemoState.show_second)),
#                 justify="space-around"
#             ),
#             # 第一个Toast
#             toast(
#                 message="第一个Toast",
#                 type="loading",
#                 duration=0,  # 持续显示
#                 position="top",
#                 visible=ToastDemoState.show_first_toast,
#                 # on_close=rx.set_value(ToastDemoState, "show_first_toast", False)
#             ),
#             # 第二个Toast
#             toast(
#                 message="第二个Toast",
#                 duration=0,  # 持续显示
#                 position="bottom",
#                 visible=ToastDemoState.show_second_toast,
#                 # on_close=rx.set_value(ToastDemoState, "show_second_toast", False)
#             ),
#         ),
#         width="100%"
#     )


# def toast_page() -> rx.Component:
#     """Toast 组件演示页面。"""
#     return rx.vstack(
#         rx.heading("Toast Demo", size="6"),
#         rx.text("Reflex wrapper for the React-Vant UI library - Toast 轻提示组件"),
#         basic_toast_demo(),
#         custom_icon_toast_demo(),
#         custom_position_toast_demo(),
#         dynamic_toast_demo(),
#         multiple_toast_demo(),
#         spacing="6",
#         padding="2em",
#         align="stretch",
#         max_width="800px",
#     )