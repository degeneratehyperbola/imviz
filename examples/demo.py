'''
Inspired by the imgui/implot demo files this file demonstrates the usage of imviz by example.
'''

from dataclasses import dataclass

import imviz as viz


@dataclass
class Demo:
	vec_2d = [0, 0]

	def __autogui__(self, name, **kwargs):
		viz.set_main_window_title('Demo')
		viz.show_imgui_demo(True)
		viz.show_implot_demo(True)

		if viz.button('Enter Fullscreen'):
			viz.enter_fullscreen()
		viz.same_line()
		if viz.button('Leave Fullscreen'):
			viz.leave_fullscreen()
		
		if viz.begin_window('Style Editor'):
			viz.style_editor()
		viz.end_window()

		viz.text('Press [CTRL+K]!')
		for e in viz.get_key_events():
			if e.key == viz.KEY_K:
				if e.action == viz.PRESS and e.mod == viz.MOD_CONTROL:
					viz.open_popup('##pressed')
		
		if viz.begin_popup('##pressed'):
			viz.text('You pressed it!')
			viz.end_popup()
		
		if viz.begin_plot('2D Input', flags=viz.PlotFlags.CANVAS_ONLY):
			viz.setup_axes_limits(-1, 1, -1, 1)
			viz.setup_axes('', '', viz.PlotAxisFlags.LOCK, viz.PlotAxisFlags.LOCK)

			self.vec_2d = viz.drag_point('##p', self.vec_2d)
			viz.plot_text('Point', self.vec_2d[0], self.vec_2d[1], [30, 10])
			viz.end_plot()

if __name__ == '__main__':
	viz.set_main_window_size([1440, 960])

	demo = Demo()
	while viz.wait():
		viz.autogui(demo)
