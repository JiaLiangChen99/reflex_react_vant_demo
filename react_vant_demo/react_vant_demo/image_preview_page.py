import reflex as rx
from typing import List, Dict, Any
from react_vant_demo.reflex_react_vant import image_preview, cell, toast

# 定义示例图片数组
images = [
    'https://img.yzcdn.cn/vant/apple-1.jpg',
    'https://img.yzcdn.cn/vant/apple-2.jpg',
    'https://img.yzcdn.cn/vant/apple-3.jpg',
]


class ImagePreviewState(rx.State):
    """
    ImagePreview 组件的状态管理
    """
    # 组件调用方式的显示状态
    visible: bool = False
    
    # 当前预览的图片索引
    current_index: int = 0
        
    @rx.event
    def handle_basic_preview(self):
        """处理基础预览"""
        # 在reflex中，静态方法的调用需要特殊处理
        # 这里我们简单模拟，实际功能需要前端react-vant支持
        print("预览图片")
        self.visible = True        
        self.current_index = 0
    
    @rx.event
    def handle_start_position(self):
        """指定初始位置"""
        print("指定初始位置为第3张")
        self.current_index = 2
        self.visible = True
    
    @rx.event
    def handle_show_close_icon(self):
        """展示关闭按钮"""
        print("展示关闭按钮")
        self.current_index = 2
        self.visible = True
    
    @rx.event
    def handle_only_close_icon(self):
        """只允许点击关闭按钮关闭"""
        print("只允许点击关闭按钮关闭")
        self.current_index = 0
        self.visible = True
    
    @rx.event
    def handle_close_event(self):
        """监听关闭事件"""
        print("预览关闭")
        self.visible = False
    
    @rx.event
    def handle_show_indicators(self):
        """展示指示点"""
        print("展示指示点")
        self.current_index = 0
        self.visible = True
    
    @rx.event
    def handle_async_close(self):
        """异步关闭"""
        print("预览将在2秒后自动关闭")
        # 在实际应用中，这里会有一个定时器来调用销毁方法
    
    @rx.event
    def toggle_component_preview(self):
        """切换组件调用方式的显示状态"""
        self.visible = not self.visible
    
    @rx.event
    def handle_change(self, index: int):
        """处理图片切换事件"""
        self.current_index = index
        print(f"当前展示第{index + 1}张")
    
    @rx.event
    def handle_component_close(self):
        """处理组件调用方式的关闭事件"""
        self.visible = False


def basic_example():
    """基础用法示例"""
    return rx.vstack(
        rx.text("基础用法", size="4"),
        cell(
            title="预览图片",
            is_link=True,
            on_click=ImagePreviewState.handle_basic_preview
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def config_example():
    """配置项示例"""
    return rx.vstack(
        rx.text("配置项", size="4"),
        cell(
            title="指定初始位置",
            is_link=True,
            on_click=ImagePreviewState.handle_start_position
        ),
        cell(
            title="展示关闭按钮",
            is_link=True,
            on_click=ImagePreviewState.handle_show_close_icon
        ),
        cell(
            title="只允许点击关闭按钮关闭",
            is_link=True,
            on_click=ImagePreviewState.handle_only_close_icon
        ),
        cell(
            title="监听关闭事件",
            is_link=True,
            on_click=ImagePreviewState.handle_close_event
        ),
        cell(
            title="展示指示点",
            is_link=True,
            on_click=ImagePreviewState.handle_show_indicators
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def async_close_example():
    """异步关闭示例"""
    return rx.vstack(
        rx.text("异步关闭", size="4"),
        cell(
            title="预览图片（2秒后自动关闭）",
            is_link=True,
            on_click=ImagePreviewState.handle_async_close
        ),
        style={"margin_bottom": "20px", "width": "100%"}
    )

def component_example():
    """组件调用示例"""
    return rx.vstack(
        rx.text("组件调用", size="4"),
        cell(
            title="组件调用",
            is_link=True,
            on_click=ImagePreviewState.toggle_component_preview
        ),
        # 组件调用方式
        style={"margin_bottom": "20px", "width": "100%"}
    )

def current_info_example():
    """显示当前预览信息"""
    return rx.vstack(
        rx.text("当前预览信息", size="4"),
        rx.text(ImagePreviewState.current_index, size="3"),
        rx.text(f"当前图片URL:" , size="3"),
        style={"margin_bottom": "20px", "width": "100%", "padding": "10px", "background_color": "#f5f5f5", "border_radius": "4px"}
    )

def image_preview_page():
    """ImagePreview 组件示例页面"""
    return rx.container(
        rx.vstack(
            rx.heading("ImagePreview 图片预览", size="2"),
            rx.divider(),
            image_preview(
                visible=ImagePreviewState.visible,
                on_close=ImagePreviewState.handle_component_close,
                images=images,
                show_indicators=True,
                show_index=False,
                on_change=ImagePreviewState.handle_change
            ),
            basic_example(),
            config_example(),
            async_close_example(),
            component_example(),
            current_info_example(),
            spacing="2",
            align_items="stretch",
            style={"max_width": "800px", "margin": "0 auto", "padding": "20px"}
        )
    )