def print_func_name_and_args(func_name, *args):
    name = func_name.__name__.title().replace("_", " ")
    print(name, *args, sep=" - ")


def open_browser(browser_name):
    print_func_name_and_args(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    print_func_name_and_args(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    print_func_name_and_args(find_registration_button_on_login_page, page_url, button_text)


if __name__ == "__main__":
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://qa.guru/")
    find_registration_button_on_login_page(page_url="https://qa.guru/", button_text="login")
