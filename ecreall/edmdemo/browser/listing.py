from collective.edm.listing.listingoptions import DefaultListingOptions
from collective.edm.listing.listingrights import DefaultListingRights

class ListingRights(DefaultListingRights):
    """ """

    def globally_can_cut(self, brains):
        """View cut column
        """
        return self.candeletecontents

    def globally_can_delete(self, brains):
        if not self.context.isTrashcanOpened():
            return False

        return self.globally_can_cut(brains)


class ListingOptions(DefaultListingOptions):

    sort_mode = 'auto'
    default_sort_on = 'sortable_title'
    default_sort_order = 'asc'
    allow_edit_popup = True
