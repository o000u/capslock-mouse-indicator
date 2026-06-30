# Caps Lock Mouse Indicator

macOS 应用，当大写锁定（Caps Lock）打开时，在鼠标旁边显示一个绿色小点。

## 功能

✅ 实时检测 Caps Lock 状态  
✅ 在鼠标旁显示绿色小点指示  
✅ 小点跟随鼠标移动  
✅ 低 CPU 占用  
✅ 完全离线运行  

## 快速开始

### 方式 1：直接运行预编译应用（最简单）⭐

1. 进入 [Releases](../../releases) 页面
2. 下载最新的 `Caps Lock Indicator.app.zip`
3. 解压
4. 双击运行 `Caps Lock Indicator.app`

**如遇到权限问题：**
```bash
xattr -d com.apple.quarantine "Caps Lock Indicator.app"
```

### 方式 2：从源代码运行

**前置要求：**
- macOS 10.12+
- Python 3.7+

**安装：**
```bash
# 1. 克隆仓库
git clone https://github.com/o000u/capslock-mouse-indicator.git
cd capslock-mouse-indicator

# 2. 安装依赖
pip3 install pynput

# 3. 运行
python3 capslock_indicator.py
```

### 方式 3：自己构建应用

```bash
# 1. 克隆仓库
git clone https://github.com/o000u/capslock-mouse-indicator.git
cd capslock-mouse-indicator

# 2. 安装构建工具
pip3 install pyinstaller pynput

# 3. 构建
pyinstaller --onefile --windowed --name "Caps Lock Indicator" capslock_indicator.py

# 4. 应用生成在 dist/ 目录
open "dist/Caps Lock Indicator.app"
```

## 使用

1. 启动应用
2. 按下 Caps Lock 键
3. 当 Caps Lock 打开时，绿色小点会出现在鼠标旁边
4. 再次按下 Caps Lock 关闭，小点消失

## 设置开机自启（可选）

### 使用系统设置

1. 系统偏好设置 → 通用 → 登录项
2. 点击 + 添加 `Caps Lock Indicator.app`

### 使用命令行

```bash
cp -r "dist/Caps Lock Indicator.app" ~/Applications/
```

然后在系统偏好设置的登录项中添加。

## 故障排除

**问题：应用无法启动**
- 检查是否给了执行权限：`chmod +x capslock_indicator.py`
- 尝试从终端运行查看错误信息

**问题：权限被拒绝（cannot be opened because the developer cannot be verified）**
- 右键点击应用 → 打开 → 选择"打开"
- 或运行：`xattr -d com.apple.quarantine "Caps Lock Indicator.app"`

**问题：绿点不显示**
- 确保 Caps Lock 已打开
- 尝试在不同的应用中使用
- 检查系统偏好设置 → 安全性与隐私 → 辅助功能权限

## 系统要求

- macOS 10.12 或更高版本
- Python 3.7+（仅当从源代码运行时）

## 许可证

MIT License

## 反馈

有问题或建议？欢迎提 Issue 或 PR！
