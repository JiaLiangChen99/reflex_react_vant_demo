import reflex as rx
from typing import List, Dict, Any
from .reflex_react_vant import picker, button, popup




class PickerState(rx.State):
    # 基础选择器状态
    base_columns = [
        {"text": "南京", "value": "0"},
        {"text": "苏州", "value": "1"},
        {"text": "常州", "value": "2"},
        {"text": "淮安", "value": "3"},
        {"text": "扬州", "value": "4"},
        {"text": "南通", "value": "5"},
        {"text": "宿迁", "value": "6"},
        {"text": "泰州", "value": "7"},
        {"text": "无锡", "value": "8"},
        {"text": "长沙", "value": "9"},
    ]
    basic_value: str = ""
    basic_result: str = ""
    
    # 多列选择器状态
    multi_value: List[str] = ["周二", "晚上"]
    multi_selected: bool = False
    multi_result: str = ""
    
    # 级联选择器状态
    cascader_value: List[str] = ["2", "2-2", "2-2-2"]
    cascader_selected: bool = False
    cascader_result: str = ""
    
    # 动态设置选项状态
    dynamic_value: List[str] = []
    dynamic_columns = [
        [{"text": "浙江", "value": "浙江", "children": []}],
        [{"text": "福建", "value": "福建", "children": []}],
    ]
    dynamic_loading: bool = False
    dynamic_selected: bool = False
    dynamic_result: str = ""
    
    # 弹出层选择器状态
    popup_value: str = "宿迁"
    popup_visible: bool = False
    popup_selected: bool = False
    popup_result: str = ""
    
    # 城市数据
    cities = {
        "浙江": ["杭州", "宁波", "温州", "嘉兴", "湖州"],
        "福建": ["福州", "厦门", "莆田", "三明", "泉州"],
    }
    
    # 级联数据
    cascader_data = [
        {
            "text": "浙江",
            "value": "1",
            "children": [
                {
                    "text": "杭州",
                    "value": "1-1",
                    "children": [
                        {"text": "西湖区", "value": "1-1-1"},
                        {"text": "余杭区", "value": "1-1-2"},
                    ],
                },
                {
                    "text": "宁波",
                    "value": "1-2",
                    "children": [
                        {"text": "海曙区", "value": "1-2-1"},
                        {"text": "江北区", "value": "1-2-2"},
                    ],
                },
            ],
        },
        {
            "text": "江苏",
            "value": "2",
            "children": [
                {
                    "text": "南京",
                    "value": "2-1",
                    "children": [
                        {"text": "玄武区", "value": "2-1-1"},
                        {"text": "秦淮区", "value": "2-1-2"},
                    ],
                },
                {
                    "text": "苏州",
                    "value": "2-2",
                    "children": [
                        {"text": "姑苏区", "value": "2-2-1"},
                        {"text": "工业园区", "value": "2-2-2"},
                    ],
                },
            ],
        },
    ]
    
    # 重置所有状态
    def reset_all(self):
        self.basic_value = ""
        self.basic_result = ""
        self.multi_value = ["周二", "晚上"]
        self.multi_selected = False
        self.multi_result = ""
        self.cascader_value = ["2", "2-2", "2-2-2"]
        self.cascader_selected = False
        self.cascader_result = ""
        self.dynamic_value = []
        self.dynamic_columns = [
            [{"text": "浙江", "value": "浙江", "children": []}],
            [{"text": "福建", "value": "福建", "children": []}],
        ]
        self.dynamic_loading = False
        self.dynamic_selected = False
        self.dynamic_result = ""
        self.popup_value = "宿迁"
        self.popup_visible = False
        self.popup_selected = False
        self.popup_result = ""
    
    # 基础选择器事件处理
    @rx.event
    def handle_basic_change(self, val: str):
        """返回的value"""
        print("选择的参数", val)
        self.basic_value = val
        for i in self.base_columns:
            if i["value"] == val:
                select_text = i["text"]
                self.basic_result = f"选中值: {select_text}"
                break
    
    @rx.event
    def handle_basic_confirm(self):
        return rx.toast.success(f"确认选择: {self.basic_value}")
    
    @rx.event
    def handle_basic_cancel(self):
        return rx.toast.info("取消选择")
    
    # 多列选择器事件处理
    @rx.event
    def handle_multi_change(self, val: List[str]):
        self.multi_value = val
    
    @rx.event
    def handle_multi_confirm(self):
        return rx.toast.success(f"确认选择: {self.multi_value}")
    
    # 级联选择器事件处理
    @rx.event
    def handle_cascader_change(self, val: List[str]):
        self.cascader_value = val
        self.cascader_result = f"选中值: {val}"
    
    @rx.event
    def handle_cascader_confirm(self):
        self.cascader_selected = True
        return rx.toast.success(f"确认选择: {self.cascader_value}")
    
    # 动态设置选项事件处理
    @rx.event
    async def handle_dynamic_change(self, values: List[str]):
        key = values[0]
        if not key:
            return
        
        # 检查是否已请求过该数据
        for column in self.dynamic_columns:
            if column[0]["text"] == key and column[0].get("children", []):
                self.dynamic_value = values
                return
        
        self.dynamic_loading = True
        
        
        # 更新列数据
        new_columns = []
        for column in self.dynamic_columns:
            if column[0]["text"] == key:
                children = [
                    {"text": city, "value": city} 
                    for city in self.cities[key]
                ]
                new_columns.append([{**column[0], "children": children}])
            else:
                new_columns.append(column)
        
        self.dynamic_columns = new_columns
        self.dynamic_loading = False
        self.dynamic_value = values
    
    @rx.event
    def handle_dynamic_confirm(self):
        self.dynamic_selected = True
        self.dynamic_result = f"选中值: {self.dynamic_value}"
        return rx.toast.success(f"确认选择: {self.dynamic_value}")
    
    # 弹出层选择器事件处理
    @rx.event
    def handle_popup_open(self):
        self.popup_visible = True
    
    @rx.event
    def handle_popup_close(self):
        self.popup_visible = False
    
    @rx.event
    def handle_popup_confirm(self, val: str):
        print("popup中修改的值 ", val)
        ...
        # self.popup_value = val
        # self.popup_selected = True
        # self.popup_result = f"选中值: {val}"
        # self.popup_visible = False
        # return rx.toast.success(f"确认选择: {val}")

    @rx.event
    def handle_popup_change(self, val: str):
        self.popup_value = val


def basic_example():
    """基础用法示例"""
    
    
    return rx.vstack(
        rx.text("基础用法", size="4"),
        picker(
            show=True,
            title="基础使用",
            value=PickerState.basic_value,
            columns=PickerState.base_columns,
            on_change=PickerState.handle_basic_change,
            on_cancel=PickerState.handle_basic_cancel,
            on_confirm=PickerState.handle_basic_confirm
        ),
        rx.text(PickerState.basic_result),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def multi_column_example():
    """多列选择示例"""
    return rx.vstack(
        rx.text("多列选择", size="4"),
        picker(
            value=PickerState.multi_value,
            on_change=PickerState.handle_multi_change,
            on_confirm=PickerState.handle_multi_confirm,
            columns=[
                ["周一", "周二", "周三", "周四", "周五"],
                ["上午", "下午", "晚上"],
            ]
        ),
        rx.cond(
            PickerState.multi_selected,
            rx.text(PickerState.multi_result, color="green")
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def cascader_example():
    """级联选择示例"""
    return rx.vstack(
        rx.text("级联选择", size="4"),
        picker(
            value=PickerState.cascader_value,
            on_change=PickerState.handle_cascader_change,
            on_confirm=PickerState.handle_cascader_confirm,
            columns=PickerState.cascader_data
        ),
        rx.cond(
            PickerState.cascader_selected,
            rx.text(PickerState.cascader_result, color="green")
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def dynamic_columns_example():
    """动态设置选项示例"""
    return rx.vstack(
        rx.text("动态设置选项", size="4"),
        picker(
            loading=PickerState.dynamic_loading,
            value=PickerState.dynamic_value,
            columns=PickerState.dynamic_columns,
            on_change=PickerState.handle_dynamic_change,
            on_confirm=PickerState.handle_dynamic_confirm
        ),
        rx.cond(
            PickerState.dynamic_selected,
            rx.text(PickerState.dynamic_result, color="green")
        ),
        rx.text("提示: 选择省份后会加载对应的城市数据", size="4", color="gray"),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def loading_example():
    """加载状态示例"""
    return rx.vstack(
        rx.text("加载状态", size="4"),
        picker(
            loading=True,
            columns=[
                ["周一", "周二", "周三", "周四", "周五"],
                ["上午", "下午", "晚上"],
            ]
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def popup_example():
    """启用弹出层示例"""
    columns = [
        "南京", "苏州", "常州", "淮安", "扬州",
        "南通", "宿迁", "泰州", "无锡"
    ]
    
    return rx.vstack(
        rx.button("启用弹出层", size="4", on_click=PickerState.handle_popup_open),
        popup(
            picker(
                    title="选择城市",
                    columns=columns,
                    on_change=PickerState.handle_popup_change,
                    on_cancel=PickerState.handle_popup_close,
            ),
            visible=PickerState.popup_visible,
            round=True,
            position="bottom",
            # on_confirm=PickerState.handle_popup_close,
            
        ),
        rx.hstack(
            rx.text(
                "选择城市",
            ),
            rx.text(
                PickerState.popup_value
            ),
        ),
        
        rx.cond(
            PickerState.popup_selected,
            rx.text(PickerState.popup_result, color="green")
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )


def picker_page():
    """Picker选择器演示页面"""
    return rx.center(
        rx.vstack(
            rx.heading("ReactVant Picker 示例"),
            basic_example(),
            multi_column_example(),
            cascader_example(),
            dynamic_columns_example(),
            loading_example(),
            popup_example(),
            button(
                "重置所有示例",
                on_click=PickerState.reset_all,
                style={"margin_top": "20px"}
            ),
            
            style={"width": "100%", "max_width": "600px", "padding": "20px"}
        ),
        style={"min_height": "100vh", "padding": "2em"}
    )


__all__ = ["picker_page"]