from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='ecreall.edmdemo',
      version=version,
      description="EDM demo site",
      long_description=open("README.rst").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Plone",
        "Framework :: Plone :: 4.0",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ecreall'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Products.AROfficeTransforms',
          'Products.OpenXml',
          'atreal.monkeyplone',
          'collective.documentviewer',
          'collective.edm.listing',
          'collective.favorites',
          'collective.mtrsetup',
          'collective.portlet.customizablerecent',
          'collective.usernamelogger',
          'ecreall.helpers.testing',
          'ecreall.helpers.upgrade',
          'ecreall.trashcan',
          'eea.tags',
          'iw.rejectanonymous',
      ],
      extras_require = dict(
          tests=['plone.app.testing'],
      ),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
