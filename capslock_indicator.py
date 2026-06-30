#!/usr/bin/env python3
"""
Caps Lock Mouse Indicator - 在鼠标旁显示绿色小点指示大写锁定状态
"""
import os
import sys
import time
import threading
import subprocess
from typing import Optional

try:
    import tkinter as tk
    from tkinter import messagebox
except ImportError:
    print("Error: tkinter not found")
    sys.exit(1)

try:
    from pynput import mouse, keyboard
    from pynput.keyboard import Listener
except ImportError:
    print("Error: pynput not found. Install with: pip3 install pynput")
    sys.exit(1)


class CapsLockIndicator:
    """监听 Caps Lock 并在鼠标旁显示指示器"""
    
    def __init__(self):
        self.caps_lock_on = False
        self.indicator_window: Optional[tk.Tk] = None
        self.main_window: Optional[tk.Tk] = None
        self.mouse_controller = mouse.Controller()
        self.listener: Optional[Listener] = None
        self.running = True
        
    def check_caps_lock_via_event(self) -> bool:
        """通过监听键盘事件检测 Caps Lock 状态变化"""
        return self.caps_lock_on
    
    def on_press(self, key):
        """键盘按下回调"""
        try:
            # 检测到 Caps Lock 键按下时切换状态
            if key == keyboard.Key.caps_lock:
                self.caps_lock_on = not self.caps_lock_on
                print(f"Caps Lock: {'ON' if self.caps_lock_on else 'OFF'}")
                
                if self.caps_lock_on:
                    self.show_indicator()
                else:
                    self.hide_indicator()
        except AttributeError:
            pass
    
    def create_indicator_window(self):
        """创建透明的指示器窗口"""
        self.indicator_window = tk.Tk()
        self.indicator_window.attributes('-alpha', 0.85)
        self.indicator_window.attributes('-topmost', True)
        self.indicator_window.overrideredirect(True)
        
        # 创建绿色圆点画布
        canvas = tk.Canvas(
            self.indicator_window,
            width=20,
            height=20,
            bg='white',
            highlightthickness=0
        )
        canvas.pack()
        
        # 绘制绿色圆点，白色边框
        canvas.create_oval(4, 4, 16, 16, fill='#00CC44', outline='white', width=2)
        
        self.indicator_window.geometry('20x20+0+0')
        self.indicator_window.withdraw()  # 初始隐藏
    
    def show_indicator(self):
        """显示指示器"""
        if self.indicator_window is None:
            self.create_indicator_window()
        self.update_indicator_position()
    
    def hide_indicator(self):
        """隐藏指示器"""
        if self.indicator_window:
            self.indicator_window.withdraw()
    
    def update_indicator_position(self):
        """更新指示器位置（跟随鼠标）"""
        if not self.running or not self.caps_lock_on:
            return
        
        if self.indicator_window:
            try:
                x, y = self.mouse_controller.position
                # 在鼠标右下方显示小点（偏移 15, -35）
                self.indicator_window.geometry(f'20x20+{int(x+15)}+{int(y-35)}')
                self.indicator_window.deiconify()
                # 每 30ms 更新一次位置
                self.indicator_window.after(30, self.update_indicator_position)
            except Exception as e:
                print(f"Error updating indicator: {e}")
    
    def setup_listener(self):
        """设置键盘监听器"""
        self.listener = Listener(on_press=self.on_press)
        self.listener.start()
        print("Keyboard listener started")
    
    def run(self):
        """主程序"""
        print("=" * 50)
        print("Caps Lock Mouse Indicator")
        print("按下 Caps Lock 看到绿色小点跟随鼠标")
        print("按 Ctrl+C 退出")
        print("=" * 50)
        
        # 创建隐藏的主窗口
        self.main_window = tk.Tk()
        self.main_window.withdraw()
        
        # 启动键盘监听
        self.setup_listener()
        
        # 启动 GUI 主循环
        try:
            self.main_window.mainloop()
        except KeyboardInterrupt:
            self.stop()
    
    def stop(self):
        """停止程序"""
        print("\n正在关闭...")
        self.running = False
        
        if self.listener:
            self.listener.stop()
        
        if self.indicator_window:
            self.indicator_window.destroy()
        
        if self.main_window:
            self.main_window.destroy()
        
        print("已关闭")
        sys.exit(0)


if __name__ == '__main__':
    app = CapsLockIndicator()
    app.run()