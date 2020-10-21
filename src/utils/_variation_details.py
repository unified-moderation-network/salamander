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

# -------------------------------------------------------------------------------
# This file last updated at: 2020-10-2021 for Unicode Version 13.1
# based on the guidleines published by The Unicode Consortium (link below)
# https://www.unicode.org/Public/13.0.0/ucd/emoji/emoji-variation-sequences.txt
# See: http://www.unicode.org/reports/tr51/#emoji_data
# for The Unicode Consortium's current guidelines for emojis
# -------------------------------------------------------------------------------

CHARS_REQUIRING_VARIATION = {
    "\u0023",
    "\u002A",
    "\u0030",
    "\u0031",
    "\u0032",
    "\u0033",
    "\u0034",
    "\u0035",
    "\u0036",
    "\u0037",
    "\u0038",
    "\u0039",
    "\u00A9",
    "\u00AE",
    "\u203C",
    "\u2049",
    "\u2122",
    "\u2139",
    "\u2194",
    "\u2195",
    "\u2196",
    "\u2197",
    "\u2198",
    "\u2199",
    "\u21A9",
    "\u21AA",
    "\u231A",
    "\u231B",
    "\u2328",
    "\u23CF",
    "\u23E9",
    "\u23EA",
    "\u23ED",
    "\u23EE",
    "\u23EF",
    "\u23F1",
    "\u23F2",
    "\u23F3",
    "\u23F8",
    "\u23F9",
    "\u23FA",
    "\u24C2",
    "\u25AA",
    "\u25AB",
    "\u25B6",
    "\u25C0",
    "\u25FB",
    "\u25FC",
    "\u25FD",
    "\u25FE",
    "\u2600",
    "\u2601",
    "\u2602",
    "\u2603",
    "\u2604",
    "\u260E",
    "\u2611",
    "\u2614",
    "\u2615",
    "\u2618",
    "\u261D",
    "\u2620",
    "\u2622",
    "\u2623",
    "\u2626",
    "\u262A",
    "\u262E",
    "\u262F",
    "\u2638",
    "\u2639",
    "\u263A",
    "\u2640",
    "\u2642",
    "\u2648",
    "\u2649",
    "\u264A",
    "\u264B",
    "\u264C",
    "\u264D",
    "\u264E",
    "\u264F",
    "\u2650",
    "\u2651",
    "\u2652",
    "\u2653",
    "\u265F",
    "\u2660",
    "\u2663",
    "\u2665",
    "\u2666",
    "\u2668",
    "\u267B",
    "\u267E",
    "\u267F",
    "\u2692",
    "\u2693",
    "\u2694",
    "\u2695",
    "\u2696",
    "\u2697",
    "\u2699",
    "\u269B",
    "\u269C",
    "\u26A0",
    "\u26A1",
    "\u26A7",
    "\u26AA",
    "\u26AB",
    "\u26B0",
    "\u26B1",
    "\u26BD",
    "\u26BE",
    "\u26C4",
    "\u26C5",
    "\u26C8",
    "\u26CF",
    "\u26D1",
    "\u26D3",
    "\u26D4",
    "\u26E9",
    "\u26EA",
    "\u26F0",
    "\u26F1",
    "\u26F2",
    "\u26F3",
    "\u26F4",
    "\u26F5",
    "\u26F7",
    "\u26F8",
    "\u26F9",
    "\u26FA",
    "\u26FD",
    "\u2702",
    "\u2708",
    "\u2709",
    "\u270C",
    "\u270D",
    "\u270F",
    "\u2712",
    "\u2714",
    "\u2716",
    "\u271D",
    "\u2721",
    "\u2733",
    "\u2734",
    "\u2744",
    "\u2747",
    "\u2753",
    "\u2757",
    "\u2763",
    "\u2764",
    "\u27A1",
    "\u2934",
    "\u2935",
    "\u2B05",
    "\u2B06",
    "\u2B07",
    "\u2B1B",
    "\u2B1C",
    "\u2B50",
    "\u2B55",
    "\u3030",
    "\u303D",
    "\u3297",
    "\u3299",
    "\U0001F004",
    "\U0001F170",
    "\U0001F171",
    "\U0001F17E",
    "\U0001F17F",
    "\U0001F202",
    "\U0001F21A",
    "\U0001F22F",
    "\U0001F237",
    "\U0001F30D",
    "\U0001F30E",
    "\U0001F30F",
    "\U0001F315",
    "\U0001F31C",
    "\U0001F321",
    "\U0001F324",
    "\U0001F325",
    "\U0001F326",
    "\U0001F327",
    "\U0001F328",
    "\U0001F329",
    "\U0001F32A",
    "\U0001F32B",
    "\U0001F32C",
    "\U0001F336",
    "\U0001F378",
    "\U0001F37D",
    "\U0001F393",
    "\U0001F396",
    "\U0001F397",
    "\U0001F399",
    "\U0001F39A",
    "\U0001F39B",
    "\U0001F39E",
    "\U0001F39F",
    "\U0001F3A7",
    "\U0001F3AC",
    "\U0001F3AD",
    "\U0001F3AE",
    "\U0001F3C2",
    "\U0001F3C4",
    "\U0001F3C6",
    "\U0001F3CA",
    "\U0001F3CB",
    "\U0001F3CC",
    "\U0001F3CD",
    "\U0001F3CE",
    "\U0001F3D4",
    "\U0001F3D5",
    "\U0001F3D6",
    "\U0001F3D7",
    "\U0001F3D8",
    "\U0001F3D9",
    "\U0001F3DA",
    "\U0001F3DB",
    "\U0001F3DC",
    "\U0001F3DD",
    "\U0001F3DE",
    "\U0001F3DF",
    "\U0001F3E0",
    "\U0001F3ED",
    "\U0001F3F3",
    "\U0001F3F5",
    "\U0001F3F7",
    "\U0001F408",
    "\U0001F415",
    "\U0001F41F",
    "\U0001F426",
    "\U0001F43F",
    "\U0001F441",
    "\U0001F442",
    "\U0001F446",
    "\U0001F447",
    "\U0001F448",
    "\U0001F449",
    "\U0001F44D",
    "\U0001F44E",
    "\U0001F453",
    "\U0001F46A",
    "\U0001F47D",
    "\U0001F4A3",
    "\U0001F4B0",
    "\U0001F4B3",
    "\U0001F4BB",
    "\U0001F4BF",
    "\U0001F4CB",
    "\U0001F4DA",
    "\U0001F4DF",
    "\U0001F4E4",
    "\U0001F4E5",
    "\U0001F4E6",
    "\U0001F4EA",
    "\U0001F4EB",
    "\U0001F4EC",
    "\U0001F4ED",
    "\U0001F4F7",
    "\U0001F4F9",
    "\U0001F4FA",
    "\U0001F4FB",
    "\U0001F4FD",
    "\U0001F508",
    "\U0001F50D",
    "\U0001F512",
    "\U0001F513",
    "\U0001F549",
    "\U0001F54A",
    "\U0001F550",
    "\U0001F551",
    "\U0001F552",
    "\U0001F553",
    "\U0001F554",
    "\U0001F555",
    "\U0001F556",
    "\U0001F557",
    "\U0001F558",
    "\U0001F559",
    "\U0001F55A",
    "\U0001F55B",
    "\U0001F55C",
    "\U0001F55D",
    "\U0001F55E",
    "\U0001F55F",
    "\U0001F560",
    "\U0001F561",
    "\U0001F562",
    "\U0001F563",
    "\U0001F564",
    "\U0001F565",
    "\U0001F566",
    "\U0001F567",
    "\U0001F56F",
    "\U0001F570",
    "\U0001F573",
    "\U0001F574",
    "\U0001F575",
    "\U0001F576",
    "\U0001F577",
    "\U0001F578",
    "\U0001F579",
    "\U0001F587",
    "\U0001F58A",
    "\U0001F58B",
    "\U0001F58C",
    "\U0001F58D",
    "\U0001F590",
    "\U0001F5A5",
    "\U0001F5A8",
    "\U0001F5B1",
    "\U0001F5B2",
    "\U0001F5BC",
    "\U0001F5C2",
    "\U0001F5C3",
    "\U0001F5C4",
    "\U0001F5D1",
    "\U0001F5D2",
    "\U0001F5D3",
    "\U0001F5DC",
    "\U0001F5DD",
    "\U0001F5DE",
    "\U0001F5E1",
    "\U0001F5E3",
    "\U0001F5E8",
    "\U0001F5EF",
    "\U0001F5F3",
    "\U0001F5FA",
    "\U0001F610",
    "\U0001F687",
    "\U0001F68D",
    "\U0001F691",
    "\U0001F694",
    "\U0001F698",
    "\U0001F6AD",
    "\U0001F6B2",
    "\U0001F6B9",
    "\U0001F6BA",
    "\U0001F6BC",
    "\U0001F6CB",
    "\U0001F6CD",
    "\U0001F6CE",
    "\U0001F6CF",
    "\U0001F6E0",
    "\U0001F6E1",
    "\U0001F6E2",
    "\U0001F6E3",
    "\U0001F6E4",
    "\U0001F6E5",
    "\U0001F6E9",
    "\U0001F6F0",
    "\U0001F6F3",
}