import menus as ms
import contact_manager as cm


def main():
    contacts = []
    while True:
        cm.clear_screen()
        choice = ms.initial()
        match choice:
            case "1":
                cm.clear_screen(1)
                name, phone, email = ms.add_contact()
                if cm.check_infos(contacts, name, phone, email):
                    phone = cm.format_phone(phone)
                    cm.save(contacts, name=name, phone=phone, email=email, favorite=False)
                continue
            case "2":
                cm.clear_screen(1)
                name = ms.update_contact()
                index = cm.search_index_contact(contacts, name)
                cm.update(contacts, index)
                continue
            case "3":
                cm.clear_screen(1)
                name = ms.delete_contact()
                index = cm.search_index_contact(contacts, name)
                cm.delete(contacts, index)
                continue
            case "4":
                cm.clear_screen(1)
                name = ms.search_contact()
                index = cm.search_index_contact(contacts, name)
                cm.search(contacts, index)
                continue
            case "5":
                cm.clear_screen(1)
                name = ms.mark_favorite()
                index = cm.search_index_contact(contacts, name)
                cm.mark_as_favorite(contacts, index)
                continue
            case "6":
                cm.clear_screen(1)
                name = ms.unmark_favorite()
                index = cm.search_index_contact(contacts, name)
                cm.unmark_as_favorite(contacts, index)
                continue
            case "7":
                cm.clear_screen(1)
                tecla = ms.show_favorites(contacts)
                if tecla == "":
                    continue
                cm.msg_error("Opção inválida!")
                cm.clear_screen()
                return ms.show_favorites(contacts)
            case "8":
                cm.clear_screen(1)
                tecla = ms.show_all(contacts)
                if tecla == "":
                    continue
                else:
                    cm.msg_error("Opção inválida!")
                    cm.clear_screen()
                    return ms.show_all(contacts)
            case "9":
                cm.clear_screen(1)
                cm.msg_exit()
            case _:
                cm.msg_error("Opção inválida!")
                continue


if __name__ == '__main__':
    main()
