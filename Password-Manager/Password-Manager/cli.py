import argparse


def my_parser():
    parser = argparse.ArgumentParser(description="Password Manager CLI")
    subparsers = parser.add_subparsers(dest='command')

    # Subparser for adding a new user
    parser_add_user = subparsers.add_parser('add-user', help='Add a new user')
    parser_add_user.add_argument('master_username', help='Master Username of the new user')
    parser_add_user.add_argument('master_password', help='Master password of the new user')

    # Subparser for user login
    parser_login = subparsers.add_parser('login', help='Login to the application')
    parser_login.add_argument('master_username', help='Master Username')
    parser_login.add_argument('master_password', help='Master password')

    return parser

    # # Subparser for adding a new password entry
    # parser_add_password = subparsers.add_parser('add-password', help='Add a new password entry')
    # # parser_add_password.add_argument('user_id', type=int, help='User ID')
    # parser_add_password.add_argument('website', help='Website name')
    # parser_add_password.add_argument('site_url', help='Website URL')
    # parser_add_password.add_argument('username', help='Username for the site')
    # parser_add_password.add_argument('password', help='Password for the site')
    #
    # # Subparser for deleting a user
    # parser_delete_user = subparsers.add_parser('delete-user', help='Delete a user')
    # parser_delete_user.add_argument('master_username_to_delete', help='Master Username of the user to delete')
    #
    # # Subparser for deleting a password
    # parser_delete_password = subparsers.add_parser('delete-password', help='Delete a password entry')
    # parser_delete_password.add_argument('master_pass_username', help='Master Username of the user to delete')
    # parser_delete_password.add_argument('website', help='Website name of the password to delete')
    #
    # # Subparser for retrieving a password
    # parser_read_password = subparsers.add_parser('read-password', help='Read a password')
    # parser_read_password.add_argument('master_username', help='Master Username of the user to read')
    # parser_read_password.add_argument('website', help='Website for the password to read')
    #
    # # Subparser for closing the application
    # parser_quit = subparsers.add_parser('quit', help='Quit the application')
