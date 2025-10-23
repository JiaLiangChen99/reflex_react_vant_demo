
"""React-Vant Demo Application.

This application demonstrates the use of React-Vant components wrapped for Reflex.
Currently showcasing the Button component with various configurations.
"""

from rxconfig import config

import reflex as rx

def index() -> rx.Component:
    """Main index page."""
    return rx.center(
        rx.vstack(
                rx.heading("React-Vant Button Demo", size="6"),
                rx.text("Reflex wrapper for the React-Vant UI library"),
                rx.divider(my="4"),
                rx.el.p(rx.link('Button', href="/button")),
                rx.el.p(rx.link('Flex', href="/flex")),
        rx.el.p(rx.link('Space', href="/space")),
        rx.el.p(rx.link('Cell', href="/cell")),
        rx.el.p(rx.link('Typography', href="/typography")),
        rx.el.p(rx.link('Image', href="/image")),
        rx.el.p(rx.link('Popup', href="/popup")),
                rx.el.p(rx.link('Toast', href="/toast")),
                rx.el.p(rx.link('Calendar', href="/calendar")),
                rx.el.p(rx.link('Cascader', href="/cascader")),
                rx.el.p(rx.link('Checkbox', href="/checkbox")),
                rx.el.p(rx.link('DatetimePicker', href="/datetime-picker")),
                rx.el.p(rx.link('NumberKeyboard', href="/number-keyboard")),
                rx.el.p(rx.link('PasswordInput', href="/password-input")),
                rx.el.p(rx.link('Picker', href="/picker")),
                rx.el.p(rx.link('ActionSheet', href="/action-sheet")),
                rx.el.p(rx.link('DropdownMenu', href="/dropdown-menu")),
                rx.el.p(rx.link('Empty', href="/empty")),
                rx.el.p(rx.link('ImagePreview', href="/image-preview")),
                rx.el.p(rx.link('Swiper', href="/swiper")),
                rx.el.p(rx.link('NavBar', href="/navbar")),
                rx.el.p(rx.link('Tabs', href="/tabs")),
                rx.el.p(rx.link('Sidebar', href="/sidebar")),
                rx.el.p(rx.link('Tabbar', href="/tabbar")),
            ),
        height="100vh",
        overflow="auto",
    )


# Add state and page to the app.
app = rx.App()

# Import pages
from react_vant_demo.button_page import button_page
from react_vant_demo.cell_page import cell_page
from react_vant_demo.flex_page import flex_page
from react_vant_demo.image_page import image_page
from react_vant_demo.popup_page import popup_page
from react_vant_demo.space_page import space_page
from react_vant_demo.typography_page import typography_page
# from react_vant_demo.toast_page import toast_page
from react_vant_demo.cascader_page import cascader_page
from react_vant_demo.checkbox_page import checkbox_demo
from react_vant_demo.datetime_picker_page import datetime_picker_page
from react_vant_demo.number_keyboard_page import number_keyboard_page
from react_vant_demo.password_input_page import password_input_page
from react_vant_demo.picker_page import picker_page
from react_vant_demo.action_sheet_page import action_sheet_page
from react_vant_demo.dropdown_menu_page import dropdown_menu_page
from react_vant_demo.empty_page import empty_page
from react_vant_demo.image_preview_page import image_preview_page
from react_vant_demo.swiper_page import swiper_page
from react_vant_demo.navbar_page import navbar_page
from react_vant_demo.tabs_page import tabs_page
from react_vant_demo.sidebar_page import sidebar_page
from react_vant_demo.tabbar_page import navbar_page

# Add pages
app.add_page(index, route="/")
app.add_page(button_page, route="/button")
app.add_page(cell_page, route="/cell")
app.add_page(flex_page, route="/flex")
app.add_page(image_page, route="/image")
app.add_page(popup_page, route="/popup")
app.add_page(space_page, route="/space")
app.add_page(typography_page, route="/typography")
# app.add_page(toast_page, route="/toast")
app.add_page(cascader_page, route="/cascader")
app.add_page(checkbox_demo, route="/checkbox")
app.add_page(datetime_picker_page, route="/datetime-picker")
app.add_page(number_keyboard_page, route="/number-keyboard")
app.add_page(password_input_page, route="/password-input")
app.add_page(picker_page, route="/picker")
app.add_page(action_sheet_page, route="/action-sheet")
app.add_page(dropdown_menu_page, route="/dropdown-menu")
app.add_page(empty_page, route="/empty")
app.add_page(image_preview_page, route="/image-preview")
app.add_page(swiper_page, route="/swiper")
app.add_page(navbar_page, route="/navbar")
app.add_page(tabs_page, route="/tabs")
app.add_page(sidebar_page, route="/sidebar")
app.add_page(navbar_page, route="/tabbar")
