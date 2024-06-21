from database import add_password, user_delete, password_delete, read_password, read_user
from session import user_session
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def interactive_mode():
    while True:
        command = input("password-manager> ").strip()
        if command == 'exit':
            print("Exiting password manager.")
            break
        process_command(command)


def process_command(command):
    commands = command.split()
    if not commands:
        return

    cmd = commands[0]

    if cmd == 'add-password':
        if len(commands) != 5:
            print("Usage: add-password <site_name> <site_url> <site_username> <site_password>")
            return
        site_name, site_url, site_username, site_password = commands[1:5]
        add_password(user_session.user_id, site_name, site_url, site_username, site_password)
        logging.info(f'Password for {site_name} added successfully')

    # the delete user function should only be accessible to me and the user should only be able to delete his users
    elif cmd == 'delete-user':
        if len(commands) != 2:
            print("Usage: delete-user <username>")
            return
        second_check = ' '
        while second_check != user_session.password:
            second_check = input('Reenter your master password for confirmation: ')
        username = commands[1]
        if not read_user(commands[1]):
            print("No such user found")
            return
        user_delete(username)
        logging.info(f'User {username} deleted successfully')

    elif cmd == 'delete-password':
        if len(commands) != 2:
            print("Usage: delete-password <site_name>")
            return
        second_check = ' '
        while second_check != user_session.password:
            second_check = input('Reenter your master password for confirmation: ')
        site_name = commands[1]
        password_delete(user_session.user_id, site_name)
        logging.info(f'Password for site {site_name} deleted successfully')

    elif cmd == 'retrieve-passwords':
        if len(commands) != 2:
            print("Usage: retrieve-passwords <website>")
            return
        website = commands[1]
        passwords = read_password(user_session.user_id, website)
        if not passwords:
            print("No passwords found.")
            return
        logging.info(
            f'Site: {passwords[2]}, URL: {passwords[3]}, Username: {passwords[4]}, Password: {passwords[5]}')

    else:
        print("Unknown command:", cmd)
        print("Choose from: add-password, delete-user, delete-password, retrieve-passwords")
