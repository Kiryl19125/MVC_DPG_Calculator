from src.view.view import View, Tag
from src.model.model import Model


class Controller:
    view: View
    model: Model

    def __init__(self, view: View, model: Model):
        self.view = view
        self.model = model

    def init_view(self) -> None:
        self.view.create_view()
        self.view.set_value_to_first_input(self.model.number_1)
        self.view.set_value_to_second_input(self.model.number_2)

    def init_controller(self) -> None:
        def callback():
            self.model.number_1 = self.view.get_value_from_first_input()
            self.model.number_2 = self.view.get_value_from_second_input()
            self.view.set_value_to_result_text(self.model.calculate(self.view.get_value_from_radio_buttons()))

        self.view.set_calc_button_callback(callback)
