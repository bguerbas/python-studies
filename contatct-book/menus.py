import formart_menu as fm


def initial() -> str:
    fm.header("menu de contatos")
    fm.body("""
    1. Adicionar novo contato
    2. Atualizar um contato 
    3. Deletar um contato
    4. Procurar contato pelo nome
    5. Marcar um contato como favorito
    6. Desmarcar um contato como favorito
    7. Ver todos contatos favoritos
    8. Ver todos os contatos
    9. Sair
    """)
    fm.footer()
    return input("Digite sua escolha: ")


def infos_contact() -> tuple[str, str, str]:
    fm.body("Nome:")
    name = input()
    fm.body("Telefone com DD sem o zero (apenas dígitos):")
    phone = input()
    fm.body("Email:")
    email = input()
    return name.capitalize(), phone, email


def add_contact() -> tuple[str, str, str]:
    fm.header("adicionar novo contato")
    name, phone, email = infos_contact()
    fm.footer()
    return name.capitalize(), phone, email


def update_contact() -> str:
    fm.header("atualizar contato")
    fm.body("Qual o nome do contato que deseja atualizar?")
    name = input()
    fm.footer()
    return name.capitalize()


def delete_contact() -> str:
    fm.header("deletar contato")
    fm.body("Qual o nome do contato que deseja deletar?")
    name = input()
    fm.footer()
    return name.capitalize()


def search_contact() -> str:
    fm.header("procurar contato")
    fm.body("QUal o nome do contato que deseja encontrar?")
    name = input()
    fm.footer()
    return name.capitalize()


def mark_favorite() -> str:
    fm.header("marcar como favorito")
    fm.body("Qual o nome do contato que deseja marcar?")
    name = input()
    fm.footer()
    return name.capitalize()


def unmark_favorite() -> str:
    fm.header("desmarcar como favorito")
    fm.body("Qual o nome do contato que deseja desmarcar?")
    name = input()
    fm.footer()
    return name.capitalize()


def show_favorites(contacts) -> str:
    fm.header("contatos favoritos")
    for contact in contacts:
        if contact.get('favorite'):
            fm.body(f"""
            Nome: {contact['name']}
            Telefone: {contact['phone']}
            Email: {contact['email']}
            """)
            fm.footer()
    return input("Pressione 'Enter' para continuar...")


def show_all(contacts) -> str:
    fm.header("todos os contatos")
    for contact in contacts:
        fm.body(f"""
        Nome: {contact['name']}
        Telefone: {contact['phone']}
        Email: {contact['email']}
        """)
        fm.footer()
    return input("Pressione 'Enter' para continuar...")



