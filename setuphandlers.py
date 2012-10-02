# -*- encoding: utf-8 -*-
import logging
logger = logging.getLogger('ecreall.edmdemo: setuphandlers')

from zope.interface import alsoProvides


def isNotCurrentProfile(context):
    return context.readDataFile("ecreall_edmdemo_marker.txt") is None


def postInstall(context):
    """Called as at the end of the setup process. """
    if isNotCurrentProfile(context): return
    portal = context.getSite()

    # Remove dummy content
    if 'front-page' in portal:
        portal.manage_delObjects(['front-page'])

    if 'news' in portal:
        portal.manage_delObjects(['news'])

    if 'events' in portal:
        portal.manage_delObjects(['events'])

    if 'Members' in portal:
        portal.Members.setExcludeFromNav(True)
        portal.Members.reindexObject()

