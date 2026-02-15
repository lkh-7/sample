#!/usr/bin/env python3
"""
간단한 Python 테스트 파일
Agent가 이 파일을 인식하고 code/ 폴더로 이동시킬 것입니다.
"""

def greet(name: str) -> str:
    """인사 메시지를 반환하는 함수"""
    return f"안녕하세요, {name}님!"

def main():
    print(greet("Agent"))
    print("Python 파일 테스트 성공! ✅")

if __name__ == "__main__":
    main()
