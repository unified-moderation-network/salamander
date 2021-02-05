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

###
# Target Disadvantage Normal Advantage
# 20  0.0025  0.05    0.0975
# 19  0.01    0.1     0.19
# 18  0.0225  0.15    0.2775
# 17  0.04    0.2     0.36
# 16  0.0625  0.25    0.4375
# 15  0.09    0.3     0.51
# 14  0.1225  0.35    0.5775
# 13  0.16    0.4     0.64
# 12  0.2025  0.45    0.6975
# 11  0.25    0.5     0.75
# 10  0.3025  0.55    0.7975
# 9   0.36    0.6     0.84
# 8   0.4225  0.65    0.8775
# 7   0.49    0.7     0.91
# 6   0.5625  0.75    0.9375
# 5   0.64    0.8     0.96
# 4   0.7225  0.85    0.9775
# 3   0.81    0.9     0.99
# 2   0.9025  0.95    0.9975
# 1   1       1       1

# While I *could* manually write these structures out,
# the math for deriving them is simple, and I'm accepting a very minimal import overhead.

NORMAL_ODDS = {}
DISADVANTAGE_ODDS = {}
ADVANTAGE_ODDS = {}

for n in range(1, 21):
    base_odds = NORMAL_ODDS[n] = (21 - n) * 0.05
    ds = DISADVANTAGE_ODDS[n] = base_odds ** 2
    ADVANTAGE_ODDS[n] = base_odds * 2 - ds


def odds_with_advantage(mod: int, target: int) -> float:
    t = target - mod
    if t < 1:
        return 1
    if t > 20:
        return 0

    return ADVANTAGE_ODDS[t]


def odds(mod: int, target: int) -> float:
    t = target - mod
    if t < 1:
        return 1
    if t > 20:
        return 0

    return NORMAL_ODDS[t]


def odds_with_disadvantage(mod: int, target: int) -> float:
    t = target - mod
    if t < 1:
        return 1
    if t > 20:
        return 0

    return DISADVANTAGE_ODDS[t]


def value_imposed_disadvantage(mod: int, target: int) -> float:
    """
    How Impactful imposing disadvantage
    on a saving throw is as if it were a modifier instead.


    Functionally equivalent to:

    If the roll is guaranteed to succeed or fail -> 0
    Else:
        target = target - mod
        c = 21 - target
        c - (20 * (c/20) ** 2

    This is based on

    ((21 - n)/ 20) ** 2 = (21 - n + x) / 20 for 0 < n < 21

    """

    return ((21 - (target - mod)) - (20 * ((21 - (target - mod)) / 20) ** 2)) * (0 < target - mod < 21)
