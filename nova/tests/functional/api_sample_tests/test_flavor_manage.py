# Copyright 2012 Nebula, Inc.
# Copyright 2013 IBM Corp.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from nova.tests.functional.api_sample_tests import api_sample_base


class FlavorManageSampleJsonTests(api_sample_base.ApiSampleTestBaseV21):
    ADMIN_API = True
    extension_name = 'flavor-manage'

    def _create_flavor(self):
        """Create a flavor."""
        subs = {
            'flavor_id': '10',
            'flavor_name': "test_flavor"
        }
        response = self._do_post("flavors",
                                 "flavor-create-post-req",
                                 subs)
        self._verify_response("flavor-create-post-resp", subs, response, 200)

    # TODO(sdague): remove duplication
    def test_create_flavor(self):
        # Get api sample to create a flavor.
        self._create_flavor()

    def test_delete_flavor(self):
        # Get api sample to delete a flavor.
        self._create_flavor()
        response = self._do_delete("flavors/10")
        self.assertEqual(202, response.status_code)
        self.assertEqual('', response.content)
