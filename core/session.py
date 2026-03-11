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