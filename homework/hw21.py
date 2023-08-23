# Реализовать мини-программу для получения логина и пароля, его записи в папку,
# и создание папки через Exception, если папки не существует
import os


def create_and_save_folder_login_password(login, password, folder):
    try:
        os.makedirs(folder)

        with open(os.path.join(folder, "data1.txt"), mode="w") as file:
            file.write(f"Логин: {login}\n")
            file.write(f"Пароль: {password}\n")

        print("Логин и пароль сохранены.")
    except Exception as error:
        print(error)


def main():
    folder = "data1"
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    create_and_save_folder_login_password(login, password, folder)


if __name__ == "__main__":
    main()

