class DeleteConfirmationPage:
    """Page object for delete confirmation pages."""
    def __init__(self, page):
        self.page = page

    def is_text_visible(self, text):
        return self.page.is_visible(f"text='{text}'")
