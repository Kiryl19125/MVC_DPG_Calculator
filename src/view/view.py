import dearpygui.dearpygui as dpg
from enum import Enum, auto, unique
from typing import Callable


@unique
class Tag(str, Enum):
    MAIN_WINDOW = auto()
    INPUT_1 = auto()
    INPUT_2 = auto()
    RADIO_BUTTONS = auto()
    CALC_BUTTON = auto()
    RESULT = auto()


class View:

    @staticmethod
    def _init_font() -> None:
        with dpg.font_registry():
            default = dpg.add_font("resources/fonts/FallingSky-JKwK.otf", 24)
        dpg.bind_font(default)

    def create_view(self) -> None:
        self._init_font()
        with dpg.window(label="Calculator", tag=Tag.MAIN_WINDOW):
            with dpg.group(horizontal=True):
                with dpg.group(horizontal=False):
                    dpg.add_input_text(label="Input 1", tag=Tag.INPUT_1, width=150, on_enter=True, decimal=True)
                    dpg.add_input_text(label="Input 2", tag=Tag.INPUT_2, width=150, on_enter=True, decimal=True)
                dpg.add_radio_button(items=["+", "-", "*", "/"], default_value="+",
                                     tag=Tag.RADIO_BUTTONS, horizontal=False)

            dpg.add_button(label="Calculate", tag=Tag.CALC_BUTTON, width=-1)
            with dpg.group(horizontal=True):
                dpg.add_text("Result: ")
                dpg.add_text(tag=Tag.RESULT)

    @staticmethod
    def set_value_to_first_input(value: int):
        dpg.set_value(item=Tag.INPUT_1, value=value)

    @staticmethod
    def set_value_to_second_input(value: int):
        dpg.set_value(item=Tag.INPUT_2, value=value)

    @staticmethod
    def get_value_from_first_input() -> int:
        return int(dpg.get_value(Tag.INPUT_1).strip("+").strip("-").strip("*").strip("/"))

    @staticmethod
    def get_value_from_second_input() -> int:
        return int(dpg.get_value(Tag.INPUT_2).strip("+").strip("-").strip("*").strip("/"))

    @staticmethod
    def get_value_from_radio_buttons() -> str:
        return dpg.get_value(item=Tag.RADIO_BUTTONS)

    @staticmethod
    def set_calc_button_callback(callback: Callable):
        dpg.set_item_callback(item=Tag.CALC_BUTTON, callback=callback)
        dpg.set_item_callback(item=Tag.INPUT_1, callback=callback)
        dpg.set_item_callback(item=Tag.INPUT_2, callback=callback)

    @staticmethod
    def set_value_to_result_text(value: str):
        dpg.set_value(item=Tag.RESULT, value=value)

    @staticmethod
    def get_main_window_tag() -> Tag:
        return Tag.MAIN_WINDOW
