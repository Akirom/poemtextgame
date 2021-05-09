BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def color_print(text: str, *effects: str) -> None:
    """
    Prints `text` using the ANSI sequences to change color, etc.

    :param text:The inputted `text` that will be changed
    :param effects:One of ANSI constants defined earlier in the module
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


def banner_text(text: str = " ", screen_width: int = 80) -> None:
    """
    Creates banner format border.

    :param text: Message in banner.
        `*` will result in a row of *'s.
        Provided Value error is text is longer than screen_length.
        Default is a blank line.

    :param screen_width: Length of the banner.
        Two spaces on each side replaced with `*` to make border.
    :return: None
    """
    if len(text) > screen_width - 4:
        raise ValueError("string {0} is longer than specified width {1}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        print("**{0}**".format(text.center(screen_width - 4)))