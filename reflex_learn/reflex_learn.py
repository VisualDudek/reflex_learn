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

def navbar_link(text: str, url: str) -> rx.Component:
    return rx.link(
        rx.text(text, size="4", weight="medium"), href=url
    )


def navbar() -> rx.Component:
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="7", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "/#"),
                    navbar_link("About", "/#"),
                    navbar_link("Pricing", "/#"),
                    navbar_link("Contact", "/#"),
                    spacing="5",
                ),
                rx.hstack(
                    rx.button(
                        "Sign Up",
                        size="3",
                        variant="outline",
                    ),
                    rx.button("Log In", size="3"),
                    spacing="4",
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/logo.jpg",
                        width="2em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading(
                        "Reflex", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.trigger(
                        rx.icon("menu", size=30)
                    ),
                    rx.menu.content(
                        rx.menu.item("Home"),
                        rx.menu.item("About"),
                        rx.menu.item("Pricing"),
                        rx.menu.item("Contact"),
                        rx.menu.separator(),
                        rx.menu.item("Log in"),
                        rx.menu.item("Sign up"),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )

def base_page(*args, hide_navbar = False) -> rx.Component:
    return rx.container(
        ### CANNOT DO THIS WAY
        # if !hide_navbar:
            # navbar()
        rx.cond(
            not hide_navbar,
            navbar(),
        ),
        rx.color_mode.button(position="bottom-left"),
        *args,
        rx.logo(),
    )


def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
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
        hide_navbar=False,
    )


app = rx.App()
app.add_page(index)
