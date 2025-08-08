"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    counter = 0
    heading = "Welcome to Reflex!"

    @rx.event
    def inc(self):
        self.counter += 1

    @rx.event
    def handle_heading_input_change(self, heading):
        self.heading = heading

class SwitchState(rx.State):
    value = False

    @rx.event
    def toggle(self, value: bool):
        self.value = value


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="bottom-left"),
        rx.vstack(
            rx.heading(State.heading, size="9"),
            rx.input(default_value=State.heading, on_change=State.handle_heading_input_change),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            rx.button(State.counter, on_click=State.inc),
            rx.switch(on_change=SwitchState.toggle),
            rx.badge(SwitchState.value),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
    )


app = rx.App()
app.add_page(index)
