from colorama import Fore


SPACE: int = 56
COLORS = [Fore.GREEN, Fore.YELLOW, Fore.RED, Fore.CYAN, Fore.MAGENTA, Fore.BLUE]


def header(title: str) -> None:
    len_ = (abs((SPACE - len(title))) // 2) - 1
    print(f"{Fore.CYAN}{'*'*len_} {title.upper()} {'*'*len_}{Fore.RESET}")


def body(content: str, color: str = COLORS[0]) -> None:
    print(f"{color}{content}{Fore.RESET}")


def footer() -> None:
    bottom = '*' * abs(SPACE)
    print(f"{Fore.CYAN}{bottom}{Fore.RESET}")