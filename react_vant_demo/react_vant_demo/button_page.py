# Import Button component from react-vant wrapper
import reflex as rx
from .reflex_react_vant import button

class ButtonDemoState(rx.State):
    """State for the Button demo."""
    
    # For tracking button clicks
    click_count: int = 0
    
    # For toggling loading state
    is_loading: bool = False
    
    @rx.event
    def increment_count(self):
        """Increment the click count."""
        self.click_count += 1
    
    @rx.event
    def toggle_loading(self):
        """Toggle the loading state."""
        self.is_loading = not self.is_loading


def button_types_demo() -> rx.Component:
    """Demo for different button types."""
    return rx.vstack(
        rx.heading("Button Types", size="5"),
        rx.hstack(
            button("Primary", type="primary", on_click=ButtonDemoState.increment_count),
            button("Info", type="info"),
            button("Default", type="default"),
            button("Warning", type="warning"),
            button("Danger", type="danger"),
            spacing="2",
            flex_wrap="wrap",
        ),
        width="100%",
    )


def button_styles_demo() -> rx.Component:
    """Demo for different button styles."""
    return rx.vstack(
        rx.heading("Button Styles", size="5"),
        
        # Plain buttons
        rx.hstack(
            button("Plain Primary", plain=True, type="primary", loading=True),
            button("Plain Info", plain=True, type="info"),
            spacing="2",
        ),
        
        # Hairline buttons
        rx.hstack(
            button("Hairline Primary", plain=True, hairline=True, type="primary"),
            button("Hairline Info", plain=True, hairline=True, type="info"),
            spacing="2",
        ),
        
        # Shape buttons
        rx.hstack(
            button("Square", square=True, type="primary"),
            button("Round", round=True, type="info"),
            button("Block Button", block=True, type="warning"),
            spacing="2",
        ),
        
        width="100%",
    )


def button_sizes_demo() -> rx.Component:
    """Demo for different button sizes."""
    return rx.vstack(
        rx.heading("Button Sizes", size="5"),
        rx.hstack(
            button("Large", size="large", type="primary"),
            button("Normal", size="normal", type="info"),
            button("Small", size="small", type="warning"),
            button("Mini", size="mini", type="danger"),
            spacing="2",
            flex_wrap="wrap",
        ),
        width="100%",
    )

def button_page() -> rx.Component:
    return rx.vstack(
        rx.heading("Button Demo", size="6"),
        rx.text("Reflex wrapper for the React-Vant UI library"),
        button_types_demo(),
        button_styles_demo(),
        button_sizes_demo(),
        rx.text(ButtonDemoState.click_count),
        spacing="6",
        padding="2em",
        align="stretch",
        max_width="800px",
    )
