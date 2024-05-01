from TermTk import TTkUtil, TTkUiLoader, TTk

# Data generated using ttkDesigner
widget = TTkUiLoader.loadDict(
{'version': '2.0.0', 'tui': {'class': 'TTkContainer', 'params': {'Name': 'MainWindow', 'Position': [4, 2], 'Size': [196, 53], 'Min Width': 0, 'Min Height': 0, 'Max Width': 65536, 'Max Height': 65536, 'Visible': True, 'Enabled': True, 'ToolTip': '', 'Padding': [0, 0, 0, 0], 'Layout': 'TTkLayout'}, 'layout': {'class': 'TTkLayout', 'params': {'Geometry': (0, 0, 196, 53)}, 'children': [{'class': 'TTkResizableFrame', 'params': {'Name': 'TTkResizableFrame', 'Position': [2, 1], 'Size': [97, 50], 'Min Width': 0, 'Min Height': 0, 'Max Width': 65536, 'Max Height': 65536, 'Visible': True, 'Enabled': True, 'ToolTip': '', 'Padding': [1, 1, 1, 1], 'Layout': 'TTkLayout', 'Border': True, 'Title': ''}, 'layout': {'class': 'TTkLayout', 'params': {'Geometry': (0, 0, 95, 48)}, 'children': []}, 'row': 0, 'col': 0, 'rowspan': 1, 'colspan': 1}]}}, 'connections': []})

root=TTk()
root.layout().addWidget(widget)
root.mainloop()
