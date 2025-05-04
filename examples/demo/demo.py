"""
Inspired by the imgui/implot demo files this file demonstrates the usage of
imviz by example.
"""

import sys
import time
import numpy as np
from dataclasses import dataclass

import imviz as viz


class SlotClass:

	__slots__ = ('a', 'b')

	def __init__(self):

		self.a = 0
		self.b = "1"


def test_func():

	for i in range(10):
		time.sleep(1)
		print(i)

	return 42


@dataclass
class Demo:
	vec_2d = [0, 1]

	def __autogui__(self, name, **kwargs):
		viz.set_main_window_title("Demo")
		viz.show_imgui_demo(True)
		viz.show_implot_demo(True)

		for e in viz.get_key_events():
			if e.key == viz.KEY_K:
				if e.action == viz.PRESS and e.mod == viz.MOD_CONTROL:
					print("Pressed Ctrl+K")

		if viz.button("Enter Fullscreen"):
			viz.enter_fullscreen()

		viz.same_line()

		if viz.button("Leave Fullscreen"):
			viz.leave_fullscreen()

if __name__ == '__main__':
	demo = Demo()

	while viz.wait():
		viz.autogui(demo)
