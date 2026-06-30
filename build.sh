#!/bin/bash
# 构建 macOS 应用的脚本

set -e

echo "🔨 构建 Caps Lock Mouse Indicator..."

# 检查 Python 3
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 未找到，请先安装 Python 3"
    exit 1
fi

# 安装依赖
echo "📦 安装依赖..."
pip3 install pynput pyinstaller

# 构建应用
echo "🏗️  构建应用..."
pyinstaller \
    --onefile \
    --windowed \
    --name "Caps Lock Indicator" \
    --osx-bundle-identifier "com.capslock.indicator" \
    capslock_indicator.py

echo "✅ 构建完成！"
echo "📍 应用位置: dist/Caps Lock Indicator.app"
echo ""
echo "使用方法:"
echo "1. 双击运行: dist/Caps Lock Indicator.app"
echo "2. 或命令行: open 'dist/Caps Lock Indicator.app'"
