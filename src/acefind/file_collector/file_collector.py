# -*- coding: utf-8 -*-
import os

class FileCollector(object):
    '''
	该类将会是一个支持跨平台的文件(带路径)的收集器
    '''
    def __init__(self, result_list):
        self._result_list = result_list
        # TODO gbk
        self._file_coding = 'gbk'
        
    def collect(self, search_path):
        self._collect_file_list(search_path, self._result_list)
        
    def _collect_file_list(self, search_path, result_list):
        # 文件
        if self._is_file(search_path):
            self._add_to_list(search_path, result_list)
            return
        
        # 目录
        if self._is_dir(search_path):
            child_list = self._collect_child(search_path)
            for child_path in child_list:
                self._collect_file_list(child_path, result_list)
    
    def _is_file(self, path):
        return os.path.isfile(path)
    
    def _is_dir(self, path):
        return os.path.isdir(path)
    
    def _add_to_list(self, path, result_list):
        file_path = path.decode(self._file_coding)
        result_list.append(file_path)
        
    def _collect_child(self, path):
        child_list = []
        for child in os.listdir(path):
            child_path = self._combile_path(path, child)
            child_list.append(child_path)
        return child_list
    
    def _combile_path(self, path, child):
        return os.path.join(path, child)
