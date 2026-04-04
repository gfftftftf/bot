#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Base64转换小程序
支持编码和解码
"""

import base64
import sys

def encode_to_base64(text):
    """将文本转换为base64"""
    text_bytes = text.encode('utf-8')
    encoded_bytes = base64.b64encode(text_bytes)
    return encoded_bytes.decode('utf-8')

def decode_from_base64(encoded_text):
    """将base64解码为文本"""
    try:
        decoded_bytes = base64.b64decode(encoded_text)
        return decoded_bytes.decode('utf-8')
    except Exception as e:
        return f"解码失败: {e}"

def main():
    print("=== Base64转换小程序 ===")
    print("1. 编码文本为Base64")
    print("2. 解码Base64为文本")
    print("3. 退出")
    
    while True:
        try:
            choice = input("\n请选择操作 (1/2/3): ").strip()
            
            if choice == '1':
                text = input("请输入要编码的文本: ")
                encoded = encode_to_base64(text)
                print(f"Base64编码结果: {encoded}")
                
            elif choice == '2':
                encoded_text = input("请输入要解码的Base64字符串: ")
                decoded = decode_from_base64(encoded_text)
                print(f"解码结果: {decoded}")
                
            elif choice == '3':
                print("再见！")
                break
                
            else:
                print("无效选择，请重新输入")
                
        except KeyboardInterrupt:
            print("\n程序已退出")
            break
        except Exception as e:
            print(f"发生错误: {e}")

if __name__ == "__main__":
    main()
