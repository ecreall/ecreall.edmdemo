from plone.testing import z2

from plone.app.testing import *
import ecreall.edmdemo

FIXTURE = PloneWithPackageLayer(zcml_filename="configure.zcml",
                                zcml_package=ecreall.edmdemo,
                                additional_z2_products=[],
                                gs_profile_id='ecreall.edmdemo:default',
                                name="ecreall.edmdemo:FIXTURE")

INTEGRATION = IntegrationTesting(bases=(FIXTURE,),
                        name="ecreall.edmdemo:Integration")

FUNCTIONAL = FunctionalTesting(bases=(FIXTURE,),
                        name="ecreall.edmdemo:Functional")

