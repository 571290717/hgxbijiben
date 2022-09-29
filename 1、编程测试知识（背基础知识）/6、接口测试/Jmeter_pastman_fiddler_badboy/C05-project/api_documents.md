# Jmeter 附件-API文档

------

## 目标

### 文档内浏览项目API文档

------

```
API- Meta Model
版本 1.0
2018-1-11
```

### 修订记录

| 修订日期 | 章节索引 | 修订摘要 | 提出人 | 修订人 |
| -------- | -------- | -------- | ------ | ------ |
|          |          |          |        |        |
|          |          |          |        |        |
|          |          |          |        |        |

```
1.    服务版本
API- Meta Model 1.0
2.    项目说明
学生信息管理系统的功能是收集学生的个人信息，以便向老师提供每个学生在校或毕业生学籍的情况，还可以让学生用自己的学号去查看自己在校期间的表现。
2.1    学院信息（Department）及其集合（Departments）
描述
    学院信息集合
```

### 属性

| 属性        | 属性描述       | 是否必填   | 备注      |
| ----------- | -------------- | ---------- | --------- |
| dep_id      | 学院编号，主键 | 新增时必填 |           |
| dep_name    | 学院名称       | 是         | 最长20位  |
| master_name | 院长名称       | 是         | 最长20位  |
| Slogan      | 口号           | 否         | 最长100位 |

```
资源描述
{
  "collection": {
"version": "1.0",
"href":" http://127.0.0.1:8000/api/departments/",
"links": [ ],
"items": [
      {
        "href": "/T01",
        "data": {
            "dep_id": "T01",
            "dep_name": "Test学院",
            "master_name": "Test-Master",
            "slogan": "Here is Slogan"
        },
"links": [
{
"rel":"classes",
"href":"http://127.0.0.1:8000/api/departments/T01/classes/ ",
"prompt": "班级集合"
}
                ]
            }
       ],
        "templates": {
"data": [
          {
            "dep_id": "T01",
            "dep_name": "Test学院",
            "master_name": "Test-Master",
            "slogan": "Here is Slogan"
        }
  ]
 },
"queries": [
      {
"rel": "search",
"href":" http://127.0.0.1:8000/api/departments/",
"prompt": "列表查询",
"data": [
{
"name": "$dep_id_list",
"value": ""
},{
                  "name": “$dep_name_list”,
                  "value": ""
      },{
"name": "$master_name_list",
"value": ""
          },{
"name": "$slogan_list",
"value": ""
  }
]
},{
"rel": "condition",
"href":" http://127.0.0.1:8000/api/departments/",
"prompt": "条件查询（名称、简称）",
"data": [
{
"name": " dep_name",
"value": ""
},{
"name": " master_name",
"value": ""
},{
"name": " slogan",
"value": ""
  }
       ]   
}
],
"error": {
"status_code": "",
"detail": ""
    }
  }
}
```

## Queries释义

| 查询方法     | 参数规则                         | 值规则                                   |
| ------------ | -------------------------------- | ---------------------------------------- |
| 列表集合查询 | $字段名_list，如”$dep_id_list”   | 使用英文逗号分隔多个值                   |
| 单查询       | 字段名称(除主键外)，如”dep_name” |                                          |
| 模糊查询     | Blur                             | 默认不开启模糊查询，blur=1将开启模糊查询 |

```
2.2    班级信息（Class）及其集合（Classes）
描述
    学院下的班级信息集合
```

### 属性

| 属性        | 属性描述       | 是否必填   | 备注      |
| ----------- | -------------- | ---------- | --------- |
| cls_id      | 班级编号，主键 | 新增时必填 |           |
| cls_name    | 班级名称       | 是         | 最长20位  |
| master_name | 班主任名称     | 是         | 最长20位  |
| slogan      | 口号           | 否         | 最长100位 |
| dep_id      | 所属学院编号   | 是         |           |

```
资源描述
    {
  "collection": {
"version": "1.0",
"href":" http://127.0.0.1:8000/api/departments/T01/classes/",
"links": [ ],
"items": [
      {
        "href": "/2017T01C01",
        "data": {
            "cls_id": "2017T01C01",
            "dep_id": "T01",
            "cls_name": "2017级Test学院C01班",
            "master_name": "Master",
            "slogan": "slogan"
        },
"links": [
{
"rel":"students",
"href":"http://127.0.0.1:8000/api/departments/T01/classes/2017T01C01/students/ ",
"prompt": "学生集合"
}
                ]
            }
       ],
        "templates": {
"data": [
           {
            "cls_id": "2017T01C01",
            "cls_name": "2017级Test学院T01班",
            "master_name": "Master",
            "slogan": "slogan"
   }
  ]
 },
"queries": [
      {
"rel": "search",
"href":"http://127.0.0.1:8000/api/departments/T01/classes/",
"prompt": "列表查询",
"data": [
{
"name": "$cls_id_list",
"value": ""
},{
                  "name": “$cls_name_list”,
                  "value": ""
      },{
"name": "$master_name_list",
"value": ""
          },{
"name": "$slogan_list",
"value": ""
            }
]
},{
"rel": "condition",
"href":"http://127.0.0.1:8000/api/departments/T01/classes/",
"prompt": "条件查询（名称、简称）",
"data": [
{
"name": " cls_name",
"value": ""
},{
"name": " master_name",
"value": ""
},{
"name": " slogan",
"value": ""
  }
       ]   
}
],
"error": {
"status_code": "",
"detail": ""
    }
  }
}
```

### Queries释义

| 查询方法     | 参数规则                         | 值规则                 |
| ------------ | -------------------------------- | ---------------------- |
| 列表集合查询 | $字段名_list，如”$cls_id_list”   | 使用英文逗号分隔多个值 |
| 单查询       | 字段名称(除主键外)，如”cls_name” |                        |

````
2.3    学生个人信息（Student）及其集合（Students）
描述
    学生个人信息集合
```

### 属性

| 属性         | 属性描述         | 是否必填   | 备注                   |
| ------------ | ---------------- | ---------- | ---------------------- |
| stu_id       | 学号、主键       | 新增时必填 |                        |
| stu_name     | 学生姓名         | 是         | 最长20位               |
| gender       | 性别             | 是         | 值只能是0\1\false\true |
| birthday     | 出生日期         | 是         | YYYYMMDD\YYYY-MM-DD    |
| native       | 籍贯             | 是         | 最长20位               |
| cls_id       | 所属班级id、外键 | 新增时必填 |                        |
| dep_id       | 所属学院id、外键 | 新增时必填 |                        |
| phone_number | 联系方式         | 最长100位  |                        |
| address      | 住址             | 最长20位   |                        |
| zipcode      | 邮编             | 最长8位    |                        |
| email        | 邮箱             | 最长20位   |                        |
| note         | 备注说明         | 最长200位  |                        |

```
资源描述
    {
  "collection": {
"version": "1.0",
"href":"http://127.0.0.1:8000/api/departments/T01/classes/2017T01C01/students/",
"links": [ ],
"items": [
      {
        "href": "/2017T01C01001",
        "data": {
            "stu_id": "2017T01C01001",
            "dep_id": "T01",
            "cls_id": "C01",
            "stu_name": "学生姓名",
            "gender": "男",
            "birthday": "2018-01-01",
            "native": "北京",
            "phone_number": "",
            "address": "",
            "zipcode": "",
            "email": "",
            "note": ""
        },
"links": []
       ],
        "templates": {
"data": [
          {

            "dep_id": "T01",
            "cls_id": "C01",
            "stu_id": "2017T01C01001",
            "stu_name": "学生姓名",
            "gender": "男",
            "birthday": "2018-01-01",
            "native": "北京",
            "phone_number": "",
            "address": "",
            "zipcode": "",
            "email": "",
            "note": ""
 }
  ]
 },
"queries": [
      {
"rel": "search",
"href":"http://127.0.0.1:8000/api/departments/T01/classes/2017T01C01/students/",
"prompt": "列表查询",
"data": [
{
"name": "$stu_id_list",
"value": ""
},{
                  "name": “$stu_name_list”,
                  "value": ""
      }
]
},{
"rel": "condition",
"href":"http://127.0.0.1:8000/api/departments/T01/classes/2017T01C01/students/",
"prompt": "条件查询（名称、简称）",
"data": [
{
"name": " stu_name",
"value": ""
}
       ]   
}
],
"error": {
"status_code": "",
"detail": ""
    }
  }
}
```

## Queries释义

| 查询方法     | 参数规则                         | 值规则                 |
| ------------ | -------------------------------- | ---------------------- |
| 列表集合查询 | $字段名_list，如”$stu_id_list”   | 使用英文逗号分隔多个值 |
| 单查询       | 字段名称(除主键外)，如”stu_name” |                        |