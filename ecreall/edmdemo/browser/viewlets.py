from plone.app.layout.viewlets.common import ViewletBase

class EmptyDocumentByLineViewlet(ViewletBase):

    def render(self):
        return ""