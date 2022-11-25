"""
*************************
*  Create a frame!      *
*           __     __   *
*          /  \~~~/  \  *
*    ,----(     ..    ) *
*   /      \__     __/  *
*  /|         (\  |(    *
* ^  \  /___\  /\ |     *
*    |__|   |__|-..     *
*************************
Given an array of strings and a character to be used as border, output the frame with the content inside.

Notes:

Always keep a space between the input string and the left and right borders.
The biggest string inside the array should always fit in the frame.
The input array is never empty.
Example
frame(['Create', 'a', 'frame'], '+')

Output:

++++++++++
+ Create +
+ a      +
+ frame  +
++++++++++
"""


def frame(text, char):
    max_l = 0
    for item in text:
        if len(item) > max_l:
            max_l = len(item)

    frame_l = max_l + 4
    frame = char * frame_l + "\n"

    temp_frame = ""
    for i in range(len(text)):
        temp_frame = char + " " + text[i] + " " * (max_l - len(text[i])) + " " + char + "\n"
        frame = frame + temp_frame

    frame += char * frame_l
    return frame