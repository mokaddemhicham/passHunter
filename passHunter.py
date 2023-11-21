from bruteForce import brute_force
from pathlib import Path
from colorama import init, Fore, Style

# Initialisez colorama (à appeler une seule fois)
init()


def welcome_message():
    print(f"\n{Fore.GREEN}===================================================")
    print("||      Bienvenue dans l'outil de test de        ||")
    print("||              force brute : P4ssHunt3r         ||")
    print("||                 Développé par                 ||")
    print("||                Hicham Mokaddem                ||")
    print("||       (C) 2023 Tous droits réservés.          ||")
    print(f"==================================================={Style.RESET_ALL}\n")


def get_target_url():
    return input("\n[>] Entrez l'URL de la cible : ")


def get_input_name(input_):
    """
    Demande à l'utilisateur de saisir le nom du champ 'name' d'un input et renvoie ce nom.
    """
    input_name = input(f"\n[>] Veuillez entrer le nom du champ 'name' de l'input {input_} : ")
    return input_name


def get_xpath(arg):
    """
    Demande à l'utilisateur de saisir le nom du champ 'name' d'un input et renvoie ce nom.
    """
    xpath = input(f"\n[>] Veuillez entrer le XPATH du champs {arg} : ")
    return xpath


def get_passwords_file_path():
    return input("\n[>] Entrez le chemin du fichier contenant les mots de passe : ")


def get_users_file_path():
    return input("\n[>] Entrez le chemin du fichier contenant les noms d'utilisateur : ")


def start_tool():
    input("\nP4ssHunt3r est prêt à démarrer. Appuyez sur Entrée pour lancer le test de force brute...\n")


def running_message():
    print("\nEn cours d'exécution... Veuillez patienter.\n")


def show_results(res):
    print("\n\nTest de force brute terminé. Résultats : ")
    if res[2]:
        print(f"{Fore.GREEN}" + str(res[0]) + f"{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}" + str(res[0]) + f"{Style.RESET_ALL}")
    print(f"\nCalculs terminés en {res[1]:.2f} secondes.")
    print()


def error_message(error_description):
    print("\nErreur :", error_description)
    print("Vérifiez vos paramètres et réessayez.\n")


def file_not_found_error(file_path):
    if Path(file_path).exists():
        pass
    else:
        error_message(f"Erreur : Le fichier '{file_path}' est introuvable. Veuillez vérifier le chemin et réessayer.")
        exit()


def goodbye_message():
    print(f"\nMerci d'avoir utilisé {Fore.GREEN}P4ssHunt3r{Style.RESET_ALL}, Développé par @{Fore.GREEN}mokaddemhicham{Style.RESET_ALL}. À bientôt "
          f"!\n")


try:
    if __name__ == "__main__":
        welcome_message()
        target_url = get_target_url()
        username_input_name = get_input_name("Username")
        password_input_name = get_input_name("Password")
        submit_input_name = get_input_name("Submit")
        error_xpath = get_xpath("Error Message")
        passwords_file = get_passwords_file_path()
        users_file = get_users_file_path()

        # Vous pouvez ajouter le code de votre outil ici

        start_tool()

        # Gestion d'erreur

        file_not_found_error(users_file)
        file_not_found_error(passwords_file)

        running_message()

        results = brute_force(target_url, username_input_name, password_input_name, submit_input_name, error_xpath,
                              users_file,
                              passwords_file)

        show_results(results)

        goodbye_message()
except Exception as e:
    print(f"Erreur : {e}")
    # Autres actions de gestion des erreurs si nécessaires
except KeyboardInterrupt:
    print(f"\n{Fore.RED}Interruption du programme par l'utilisateur. Nettoyage en cours...{Style.RESET_ALL}")
    # Ajoutez ici d'autres actions de nettoyage ou de gestion
finally:
    print(f"{Fore.YELLOW}Good Bye :){Style.RESET_ALL}\n")
