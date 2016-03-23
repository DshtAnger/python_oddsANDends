#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Stack():
    def __init__(self,size):
        self.__stack = []
        self.__size = size
        self.__top = -1

    def Full(self):
        return True if self.__top+1 == self.__size else False


    def Empty(self):
        return True if self.__top == -1 else False

    def push(self,content):
        if self.Full():
            print "Stack is Full!\n"
        else:
            self.__stack.append(content)
            self.__top += 1

    def pop(self):
        if self.Empty():
            print "stack is Empty!\n"
        else:
            self.__top -= 1
            return self.__stack.pop()
if __name__ == '__main__':
    print "[+]Testing…………"
    s = Stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.push(6)
    print s._Stack__stack,s._Stack__top,s.Empty(),s.Full()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    print s._Stack__stack,s._Stack__top,s.Empty(),s.Full()
