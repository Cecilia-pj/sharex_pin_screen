import clr
import sys
from ctypes import windll

windll.shcore.SetProcessDpiAwareness(1)

# 添加 ShareX 程序集路径（根据实际安装位置调整）
sharex_path = r"C:\Program Files\ShareX"  # 示例路径
sys.path.append(sharex_path)

# 加载 ShareX 相关 DLL
clr.AddReference("ShareX")
clr.AddReference("ShareX.ScreenCaptureLib")
clr.AddReference("System.Drawing")

# 导入命名空间
from System.Drawing import Point
from ShareX import PinToScreenForm, PinToScreenOptions
from ShareX.ScreenCaptureLib import RegionCaptureTasks, RegionCaptureOptions, RegionCaptureMode, RegionCaptureForm


def Pin_to_screen():
	
	options = RegionCaptureOptions()
	
	
	regionCaptureForm = RegionCaptureForm(RegionCaptureMode.Default, options, )
	regionCaptureForm.ShowDialog()
	
	rect = regionCaptureForm.GetSelectedRectangle()
	resultImage = regionCaptureForm.GetResultImage()
	
	if rect is not None and resultImage is not None:
		
		form = PinToScreenForm(
			resultImage,
			PinToScreenOptions(),
			Point(rect.X, rect.Y)
		)
	
		form.ShowDialog()


if __name__ == "__main__":
	Pin_to_screen()
