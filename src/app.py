from src.view.view import View
from src.model.model import Model
from src.controller.controller import Controller
import dearpygui.dearpygui as dpg

_model: Model = Model()
_view: View = View()
_controller: Controller = Controller(view=_view, model=_model)


def main() -> None:
    dpg.create_context()

    _controller.init_view()
    _controller.init_controller()

    dpg.create_viewport(title="MVC Calculator", width=300, height=220, resizable=False)
    dpg.setup_dearpygui()
    dpg.set_primary_window(window=_controller.view.get_main_window_tag(), value=True)
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
