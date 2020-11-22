#   Copyright 2020 Michael Hall
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from __future__ import annotations

import re
import shlex
import operator
from functools import partial


class Tracked:
    def __init__(self, *args):
        self._args = args
        self._fetched = set()

    def __getitem__(self, item):
        self._fetched.add(item)
        return self.args.__getitem__(item)

    @property
    def unfetched(self):
        return tuple(
            (
                element
                for index, element in enumerate(self.args)
                if index not in self._fetched
            )
        )


def create_func_from_spec(spec: str):
    """
    Specs should appear to be something as:

    $2 words words words $1
    """

    arg_spec = shlex.split(spec)

    patt = re.compile(r"^\$([0-9]+)$")
    escaped = re.compile(r"^\$(\$.*)$")

    def hard_val(x, args):
        return x

    transforms = []

    for index, a in enumerate(arg_spec):
        if match := patt.match(a):
            idx = int(match.group(0))
            transforms.append(partial(operator.getitem, b=idx))
        elif match := escaped.match(a):
            transforms.append(partial(hard_val, match.group(1)))
        else:
            transforms.append(partial(hard_val, a))

    def transformer(args):

        tracker = Tracked(*args)

        most = tuple((f(tracker) for f in transforms))
        return shlex.join((*most, tracker.unfetched))

    return transformer
