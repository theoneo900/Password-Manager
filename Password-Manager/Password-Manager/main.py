# import argparse
import logging
from database import add_new_user, authenticate_user
from session import user_session
from cli import my_parser
from cli_display import print_big_letters
from utils import interactive_mode

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def main():
    # intro letters
    print_big_letters()

    # add the parser args
    parser = my_parser()
    args = parser.parse_args()

    # check for commands that do not require log in
    if args.command is None:
        parser.print_help()
        return

    elif args.command == 'add-user':
        add_new_user(args.master_username, args.master_password)
        logging.info(f'User {args.master_username} added successfully')

    # before sensitive functions request login
    elif args.command == 'login':
        user_id = authenticate_user(args.master_username, args.master_password)

        if user_id:
            print('authenticated')
            user_session.authenticate(user_id, args.master_username, args.master_password)
            logging.info(f'User {args.master_username} logged in successfully')
            interactive_mode()
        else:
            logging.error('Invalid username or password')
        return

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
