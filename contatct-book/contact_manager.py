from os import system, name
from time import sleep

import validates as vl
import formart_menu as fm
from menus import infos_contact


color_success = fm.COLORS[0]
color_warning = fm.COLORS[1]
color_error = fm.COLORS[2]


def save(contacts: list, **kwargs) -> None:
    fm.body("Salvando contato...", color_warning)
    contacts.append(kwargs)
    fm.body("Contato salvo!", color_success)


def update(contacts: list, index: int) -> None:
    fm.body("Atualizando contato...", color_warning)
    contact_update = contacts[index]
    contact_update['name'], contact_update['phone'], contact_update['email'] = infos_contact()
    # Verifica as informações do contato
    if not check_infos(contacts, contact_update['name'], contact_update['phone'], contact_update['email']):
        msg_error("Não foi possível atualizar o contato!")
        return
    fm.body(f"""
    Contato atualizado!
    Nome: {contact_update['name']}
    Telefone: {contact_update['phone']}
    E-mail: {contact_update['email']}""", color_success)


def delete(contacts: list, index: int) -> None:
    fm.body("Deletando contato...", color_warning)
    contact_delete = contacts.pop(index)
    fm.body("Contato deletado!", color_success)


def search(contacts: list, index: int) -> None:
    fm.body("Procurando contato...", color_warning)
    contact = contacts[index]
    favorite = "Sim" if contact.get('favorite') else "Não"
    fm.body(f"""
    Nome: {contact['name']}
    Telefone: {contact['phone']}
    E-mail: {contact['email']}
    Favoritos: {favorite}"
    """, color_success)


def mark_as_favorite(contacts: list, index: int) -> None:
    fm.body("Marcando como favorito...", color_warning)
    contacts[index]['favorite'] = True
    fm.body("Contato marcado!", color_success)


def unmark_as_favorite(contacts: list, index: int) -> None:
    fm.body("Desmarcando como favorito...", color_warning)
    contacts[index]['favorite'] = False
    fm.body("Contato desmarcado!", color_success)


def search_index_contact(contacts, name_) -> int | None:
    for idx, contact in enumerate(contacts):
        if contact['name'] == name_:
            return idx
    return None


def msg_error(msg: str) -> None:
    fm.body(msg, color_error)


def msg_exit() -> None:
    fm.body("Saindo do sistema...")
    clear_screen()
    exit()


def clear_screen(time: int = 3) -> None:
    sleep(time)
    system('cls' if name == 'nt' else 'clear')


def format_phone(phone: str) -> str:
    if len(phone) == 11:
        return f"({phone[:2]}) {phone[2:7]}-{phone[7:]}"
    elif len(phone) == 10:
        return f"({phone[:2]}) {phone[2:6]}-{phone[6:]}"


def check_infos(contacts: list[str], name_: str, phone: str, email: str) -> bool:
    # Verifica se o contato já existe
    if search_index_contact(contacts, name_) is not None:
        msg_error("Esse contato já existe!")
        return False
    # Verifica se o nome ou o telefone ou o email está vazio
    if name_ == "" or phone == "" or email == "":
        msg_error("Nome, telefone e email são obrigatórios!")
        return False
    # Verifica se o email é válido
    if not vl.email_ok(email):
        msg_error("Email inválido!")
        return False
    # Verifica se o telefone é válido
    if not vl.phone_ok(phone):
        msg_error("Telefone inválido!")
        return False

    return True

