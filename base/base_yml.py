#!usr/bin/env python

#-*- coding:utf-8 -*-
import yaml


def yml_data_with_file(file_name):
    with open("./data/"+ file_name + ".yml", 'r') as f:
        data = yaml.safe_load(f)
        f.close()
        return data

