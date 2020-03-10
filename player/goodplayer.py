# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json

def make_guess(request):
    game = request.get_json()
    min = game['minimum']
    max = game['maximum']

    for move in game['history']:
        historic_guess = move['guess']
        
        if move['result'] == 'lower':
            if max >= historic_guess:
                max = historic_guess - 1
                
        if move['result'] == 'higher':
            if min <= historic_guess:
                min = historic_guess + 1
                
    guess = (min + max) // 2
    return json.dumps(guess)
