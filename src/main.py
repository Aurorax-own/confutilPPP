import confutilPPP

# 此项设置为 False 时，日志不会带颜色（默认为 True）
confutilPPP.LOG_IS_COLOR = True


def test():
    # _object : dict, 包含配置对象
    # _filename : str, 配置文件名 默认为 config
    # return : dict, 配置字典
    # 首次当前位置生成 *.yml 文件，之后直接读取
    # *.yaml也可用
    CONFIG = {
        'test': 'test'
    }
    conf = confutilPPP.check_config(_object=CONFIG, _filename='config')
    print(conf)


if __name__ == '__main__':
    test()
