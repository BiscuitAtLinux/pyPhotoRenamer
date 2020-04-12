# pyPhotoRenamer
将照片重命名为YYYYMMDD-xxx格式，并且自动将对应的RAW格式照片重命名为相同的文件名，支持索尼ARW，佳能CR2，松下RW2，富士RAF，Adobe DNG等多种RAW格式

## 依赖
* Python: 2.7 或 3.x
* exiv2
	* 在Linux平台使用Python2，可以依赖 [pyexiv2](http://tilloy.net/dev/pyexiv2/overview.html) 库
		* Ubuntu下可以通过 `sudo apt install python-pyexiv2` 进行安装
		* Archlinux系列可以通过 `pacman -S python2-exiv2` 安装
	* 使用Python3或在Windows平台，或者不方便安装pyexiv2的平台，可以依赖 [exiv2命令行工具](http://www.exiv2.org/)
		* Ubuntu下可以通过 `sudo apt install exiv2` 进行安装
		* Archlinux系列可以通过 `pacman -S exiv2` 安装
		* 对于Windows下的Msys2环境，可以通过 `pacman -S mingw-w64-x86_64-exiv2` 安装
