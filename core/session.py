from prompt_toolkit import PromptSession

ses = PromptSession()

def get(prompt_text):
    try:
        return ses.prompt(prompt_text).strip()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
        return None
    except EOFError:
        print("\nExiting")
        return None

def get_confirm(prompt_text):
    while True:
        response = get(prompt_text + " (y/n): ")
        if response is None:
            return False
        if response.lower() in ['y', 'yes']:
            return True
        elif response.lower() in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' or 'n'.")