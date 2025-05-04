'''
Inspired by the imgui/implot demo files this file demonstrates the usage of imviz by example.
'''

from dataclasses import dataclass

import imviz as viz


@dataclass
class Demo:
	vec_2d = [0, 1]

	def __autogui__(self, name, **kwargs):
		viz.set_main_window_title('Demo')
		viz.show_imgui_demo(True)
		viz.show_implot_demo(True)

		if viz.button('Enter Fullscreen'):
			viz.enter_fullscreen()
		viz.same_line()
		if viz.button('Leave Fullscreen'):
			viz.leave_fullscreen()
		
		viz.text('Press [CTRL+K]!')
		for e in viz.get_key_events():
			if e.key == viz.KEY_K:
				if e.action == viz.PRESS and e.mod == viz.MOD_CONTROL:
					viz.open_popup('##pressed')
		
		if viz.begin_popup('##pressed'):
			viz.text('You pressed it!')
			viz.end_popup()
		
		if viz.begin_plot('2D Input', flags=viz.PlotFlags.CANVAS_ONLY):
			viz.get_plot_popup_point()
			viz.end_plot()

if __name__ == '__main__':
	demo = Demo()

	while viz.wait():
		viz.autogui(demo)
