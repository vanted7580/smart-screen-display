# Smart Screen Display

Custom screen refresh rate on different power status.

自定义插电/离电屏幕刷新率。

## Build from source

```
pyinstaller -F "Smart Screen Display.py" --noconsole 
```

## Installation

+ Run `install.cmd` or `uninstall.cmd` with administrator privilege to install/uninstall.

+ 运行`install.cmd`进行安装，运行`uninstall.cmd`进行卸载（需要管理员权限）。

## Config [Smart Screen Display (Config Version)]

Set a proper refresh rate in config before installation!

安装前在参数内设置好你的刷新率！

#### `Smart Screen Display.ini` 
```
[screen]
dc = 60 #离电刷新率
ac = 240 #插电刷新率
```

## Issue

配置文件版本有概率在切换刷新率后会自动还原。

## License

[ smart-screen-display
](https://github.com/wqy224491/smart-screen-display) is available for [GPL-3.0 License](https://github.com/wqy224491/smart-screen-display/blob/main/LICENSE) in files.

<img src="https://upload.cc/i1/2023/01/01/0nyLFI.png" width="280">
