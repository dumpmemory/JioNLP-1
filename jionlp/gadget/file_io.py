# -*- coding=utf-8 -*-

import os
import json

#class Tools(object):
#    '''
#    NLP 中常用的工具函数集合
#    '''


def read_file_by_line(file_path, line_num=None, 
                      skip_empty_line=True):
    """读取一个文件的前 N 行，按列表返回，
    文件中按行组织，要求 utf-8 格式编码的自然语言文本。
    若每行元素为 json 格式可自动加载。

    Args:
        file_path(str): 文件路径
        line_num(int): 读取文件中的行数，若不指定则全部按行读出
        skip_empty_line(boolean): 是否跳过空行

    Returns:
        list: line_num 行的内容列表

    Examples:
        >>> file_path = '/path/to/stopwords.txt'
        >>> print(bbd.read_file_by_line(file_path, line_num=3))
        ['在', '然后', '还有']

    """
    content_list = list()
    count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        line = f.readline()
        while True:
            if line == '':  # 整行全空，说明到文件底
                break
            if line_num is not None:
                if count >= line_num:
                    break

            if line.strip() == '':
                if skip_empty_line:
                    count += 1
                    line = f.readline()
                else:
                    try:
                        cur_obj = json.loads(line.strip())
                        content_list.append(cur_obj)
                    except:
                        content_list.append(line.strip())
                    count += 1
                    line = f.readline()
                    continue
            else:
                try:
                    cur_obj = json.loads(line.strip())
                    content_list.append(cur_obj)
                except:
                    content_list.append(line.strip())
                count += 1
                line = f.readline()
                continue
    return content_list











def write_file_by_line(data_list, file_path, start_line_idx=None,
                       end_line_idx=None, replace_slash_n=True):
    """将一个数据 list 按行写入文件中，
    文件中按行组织，以 utf-8 格式编码的自然语言文本。

    Args:
        data_list(list): 数据 list，每一个元素可以是 str, list, dict
        file_path(str): 写入的文件名，可以是绝对路径
        start_line_idx(int): 将指定行的数据写入文件，起始位置，None 指全部写入
        end_line_idx(int): 将指定行的数据写入文件，结束位置，None 指全部写入
        replace_slash_n(bool): 将每个字符串元素中的 \n 进行替换，避免干扰

    Returns:
        None

    Examples:
        >>> data_list = [{'text': '上海'}, {'text': '广州'}]
        >>> bbd.write_file_by_line(data_list, 'sample.json')

    """
    if start_line_idx is None:
        start_line_idx = 0
    if end_line_idx is None:
        end_line_idx = len(data_list)
    with open(file_path, 'w', encoding='utf-8') as f:
        for item in data_list[start_line_idx : end_line_idx]:
            if type(item) in [list, dict]:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
            elif type(item) is str:
                f.write(item.replace('\n', '') + '\n')
            elif type(item) in [int, float]:
                f.write(str(item) + '\n')
            else:
                wrong_line = 'the type of `{}` in data_list is `{}`'.format(
                    item, type(item))
                raise TypeError(wrong_line)
    
    






