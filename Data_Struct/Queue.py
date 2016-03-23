#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Queue():
    
    def __init__(self,size):
        self.__queue = []
        self.__size = size
        self.__head = -1
        self.__tail = -1
        
    def Empty(self):
        return True if self.__head == self.__tail else False
    
    def Full(self):
        return True if self.__tail+1 == self.__size else False
    
    def inQueue(self,content):
        if self.Full():
            print "Queue is Full!\n"
        else:
            self.__queue.append(content)
            self.__tail += 1
            
    def outQueue(self):
        if self.Empty():
            print "Queue is Empty!\n"
        else:
            self.__tail -= 1
            return self.__queue.pop(0)

if __name__ == '__main__':
    print "[+]Testing…………"
    q = Queue(5)
    q.inQueue(1)
    q.inQueue(2)
    q.inQueue(3)
    q.inQueue(4)
    q.inQueue(5)
    q.inQueue(6)
    print q._Queue__queue,q._Queue__head,q._Queue__tail,q.Full(),q.Empty()
    q.outQueue()
    q.outQueue()
    q.outQueue()
    q.outQueue()
    q.outQueue()
    q.outQueue()
    print q._Queue__queue,q._Queue__head,q._Queue__tail,q.Full(),q.Empty()