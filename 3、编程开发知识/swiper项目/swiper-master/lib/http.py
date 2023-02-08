import json

from django.http import HttpResponse
from django.conf import settings


def render_json(data, code=200):
    """
    自定义render函数, code默认值为200, 返回正常
    """
    result = {
        'data': data,
        'code': code,
    }
    # 开发为了显示清晰使用
    if settings.DEBUG:
        json_str = json.dumps(
            result,
            indent=4,  # 缩进
            # sepatarors=[',', ':'],  # 分隔符
            ensure_ascii=False,  # 编码方式
            sort_keys=True,  # 排序
        )
    else:
        # 实际项目中使用
        json_str = json.dumps(result,
                              # sepatarors=[',', ':'],
                              ensure_ascii=False)
    return HttpResponse(json_str)
